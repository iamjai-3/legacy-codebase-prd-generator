"""
User Flow Agent for analyzing and documenting user journeys and workflows.

Analyzes screenshots and code to generate comprehensive user flow documentation
including user journeys, entry/exit points, and flow diagrams.
"""

from dataclasses import dataclass
from typing import Any

from src.agents.base_agent import AgentContext, AgentResult, BaseAgent
from src.prompts.user_flow import UserFlowPrompts
from src.utils.logging_config import ExecutionTimer
from src.utils.serialization import extract_json_array


@dataclass
class UserFlowStep:
    """A single step in a user flow."""

    step_number: int
    action: str
    screen: str
    input_data: list[str]
    expected_result: str
    alternative_paths: list[str]
    error_scenarios: list[str]


@dataclass
class UserFlow:
    """A complete user flow/journey."""

    flow_id: str
    name: str
    description: str
    actor: str
    preconditions: list[str]
    steps: list[UserFlowStep]
    postconditions: list[str]
    success_criteria: str
    estimated_time: str


@dataclass
class UserFlowResult:
    """Complete user flow analysis result."""

    form_name: str
    user_flows: list[UserFlow]
    primary_actors: list[str]
    entry_points: list[str]
    exit_points: list[str]
    cross_module_flows: list[str]
    user_journey_map: str
    flow_diagram_mermaid: str


class UserFlowAgent(BaseAgent[UserFlowResult]):
    """
    Agent for analyzing user flows and journeys from screenshots and code.
    Documents step-by-step user interactions and workflows.
    """

    def __init__(self) -> None:
        """Initialize the user flow agent."""
        super().__init__("UserFlowAgent")

    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt for user flow analysis."""
        return UserFlowPrompts.system_prompt(context.form_name)

    async def analyze(
        self,
        context: AgentContext,
        screenshot_analysis: dict[str, Any] | None = None,
        code_analysis: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> AgentResult[UserFlowResult]:
        """
        Analyze user flows for a form.

        Args:
            context: Agent execution context
            screenshot_analysis: Results from screenshot analysis agent
            code_analysis: Results from code analysis

        Returns:
            AgentResult with UserFlowResult
        """
        timer = ExecutionTimer()

        self.logger.info(
            "Starting user flow analysis",
            form_name=context.form_name,
            has_screenshots=screenshot_analysis is not None,
        )

        try:
            # Retrieve context from vector store
            stored_context = self.retrieve_context(
                context.form_name, "user flow workflow steps actions screens", limit=10
            )

            # Identify actors and boundaries
            primary_actors = await self._identify_actors(context, stored_context)
            entry_points, exit_points = await self._identify_flow_boundaries(
                context, screenshot_analysis
            )

            # Generate flows and analysis
            user_flows = await self._generate_user_flows(
                context, primary_actors, entry_points, stored_context
            )
            cross_module_flows = await self._identify_cross_module_flows(context, stored_context)
            journey_map = await self._generate_journey_map(context, user_flows)
            flow_diagram = await self._generate_flow_diagram(context, user_flows)

            result = UserFlowResult(
                form_name=context.form_name,
                user_flows=user_flows,
                primary_actors=primary_actors,
                entry_points=entry_points,
                exit_points=exit_points,
                cross_module_flows=cross_module_flows,
                user_journey_map=journey_map,
                flow_diagram_mermaid=flow_diagram,
            )

            self.logger.info(
                "User flow analysis complete",
                form_name=context.form_name,
                flows_documented=len(user_flows),
                actors=len(primary_actors),
                duration_ms=timer.elapsed_ms(),
            )

            return self.create_success_result(result, timer)

        except Exception as e:
            return self.create_error_result(e, timer)

    async def _identify_actors(self, context: AgentContext, stored_context: list[str]) -> list[str]:
        """Identify user types who interact with this module."""
        context_text = self.format_context_for_prompt(stored_context, max_contexts=5)

        prompt = f"""Based on the context for "{context.form_name}":

{context_text}

Identify all user types (actors) who would interact with this module.
Consider:
- Primary users who perform main operations
- Secondary users who review/approve
- Administrative users
- System actors (automated processes)

List each actor with a brief description."""

        items = await self.invoke_llm_for_list(context, prompt)

        # Extract just the actor name (before any colon description)
        actors = [
            item.split(":")[0].strip()
            for item in items
            if item and len(item.split(":")[0].strip()) < 50
        ]

        return actors if actors else ["Standard User", "Administrator"]

    async def _identify_flow_boundaries(
        self, context: AgentContext, screenshot_analysis: dict[str, Any] | None
    ) -> tuple[list[str], list[str]]:
        """Identify entry and exit points for the module."""
        prompt = f"""For the "{context.form_name}" module, identify:

1. ENTRY POINTS - How users access this module:
   - Menu items
   - Links from other modules
   - Direct URLs
   - System triggers

2. EXIT POINTS - How users leave this module:
   - Save and close actions
   - Navigation to other modules
   - Logout/timeout
   - Cancel operations

Format response as:
ENTRY POINTS:
- Entry point 1
- Entry point 2

EXIT POINTS:
- Exit point 1
- Exit point 2"""

        response = await self.invoke_llm(context, prompt)

        entry_points: list[str] = []
        exit_points: list[str] = []
        current_section = None

        for line in response.split("\n"):
            upper_line = line.upper()
            if "ENTRY" in upper_line:
                current_section = "entry"
            elif "EXIT" in upper_line:
                current_section = "exit"
            elif line.strip().startswith("-"):
                item = line.strip().lstrip("- ")
                if current_section == "entry":
                    entry_points.append(item)
                elif current_section == "exit":
                    exit_points.append(item)

        return entry_points or ["Main Menu"], exit_points or ["Save", "Cancel"]

    async def _generate_user_flows(
        self,
        context: AgentContext,
        actors: list[str],
        entry_points: list[str],
        stored_context: list[str],
    ) -> list[UserFlow]:
        """Generate detailed user flows."""
        context_text = self.format_context_for_prompt(stored_context, max_contexts=5)

        prompt = f"""Generate detailed user flows for "{context.form_name}".

Actors: {", ".join(actors[:3])}
Entry points: {", ".join(entry_points[:3])}

Context:
{context_text}

Generate 3-5 key user flows in JSON format:
[
    {{
        "flow_id": "UF-001",
        "name": "Flow name",
        "description": "Brief description",
        "actor": "Primary actor",
        "preconditions": ["User is logged in"],
        "steps": [
            {{
                "step_number": 1,
                "action": "User action",
                "screen": "Screen name",
                "input_data": ["Field 1", "Field 2"],
                "expected_result": "What happens",
                "alternative_paths": ["If X, then Y"],
                "error_scenarios": ["Error case"]
            }}
        ],
        "postconditions": ["Data is saved"],
        "success_criteria": "How to verify success",
        "estimated_time": "5 minutes"
    }}
]

Include:
1. Main CRUD operations
2. Search/filter flow
3. Approval/workflow (if applicable)"""

        data = extract_json_array(await self.invoke_llm(context, prompt))
        default_actor = actors[0] if actors else "User"

        return [
            self._parse_user_flow(flow_data, i, default_actor)
            for i, flow_data in enumerate(data, 1)
        ]

    def _parse_user_flow(
        self, flow_data: dict[str, Any], index: int, default_actor: str
    ) -> UserFlow:
        """Parse a single user flow from JSON data."""
        steps = [
            UserFlowStep(
                step_number=s.get("step_number", i),
                action=s.get("action", ""),
                screen=s.get("screen", ""),
                input_data=s.get("input_data", []),
                expected_result=s.get("expected_result", ""),
                alternative_paths=s.get("alternative_paths", []),
                error_scenarios=s.get("error_scenarios", []),
            )
            for i, s in enumerate(flow_data.get("steps", []), 1)
        ]

        return UserFlow(
            flow_id=flow_data.get("flow_id", f"UF-{index:03d}"),
            name=flow_data.get("name", ""),
            description=flow_data.get("description", ""),
            actor=flow_data.get("actor", default_actor),
            preconditions=flow_data.get("preconditions", []),
            steps=steps,
            postconditions=flow_data.get("postconditions", []),
            success_criteria=flow_data.get("success_criteria", ""),
            estimated_time=flow_data.get("estimated_time", "N/A"),
        )

    async def _identify_cross_module_flows(
        self, context: AgentContext, stored_context: list[str]
    ) -> list[str]:
        """Identify flows that span multiple modules."""
        context_text = self.format_context_for_prompt(stored_context, max_contexts=5)

        prompt = f"""For "{context.form_name}", identify any cross-module workflows:

{context_text}

List workflows that:
- Start in this module and continue elsewhere
- Start elsewhere and involve this module
- Require data from other modules

Format: [Module A] -> [Module B]: Description"""

        items = await self.invoke_llm_for_list(context, prompt)
        return [item for item in items if "->" in item or "→" in item]

    async def _generate_journey_map(self, context: AgentContext, user_flows: list[UserFlow]) -> str:
        """Generate a textual user journey map."""
        flow_summaries = "\n".join(
            [f"- {f.name}: {len(f.steps)} steps, {f.estimated_time}" for f in user_flows]
        )

        prompt = f"""Create a user journey map for "{context.form_name}":

User flows:
{flow_summaries}

Create a narrative journey map that describes:
1. User's goal when entering the module
2. Key touchpoints and interactions
3. Emotional states at each stage (frustration, satisfaction)
4. Opportunities for improvement in the modernized version

Write 3-4 paragraphs in a narrative style."""

        return await self.invoke_llm(context, prompt)

    async def _generate_flow_diagram(
        self, context: AgentContext, user_flows: list[UserFlow]
    ) -> str:
        """Generate a Mermaid flowchart diagram."""
        if not user_flows:
            return "flowchart TD\n    A[Start] --> B[No flows documented]"

        main_flow = user_flows[0]
        steps_text = chr(10).join(f"{s.step_number}. {s.action}" for s in main_flow.steps)

        prompt = f"""Create a Mermaid flowchart for "{main_flow.name}":

Steps:
{steps_text}

Generate a valid Mermaid flowchart diagram.
Use format:
```mermaid
flowchart TD
    A[Start] --> B[Step 1]
    B --> C[Step 2]
    ...
```

Include decision points where there are alternative paths."""

        response = await self.invoke_llm(context, prompt)
        return self._extract_mermaid_diagram(response, main_flow)

    def _extract_mermaid_diagram(self, response: str, flow: UserFlow) -> str:
        """Extract Mermaid diagram from LLM response."""
        import re

        # Try to find mermaid code block
        mermaid_match = re.search(r"```mermaid\s*([\s\S]*?)```", response)
        if mermaid_match:
            return mermaid_match.group(1).strip()

        # Try to find flowchart directly
        flowchart_match = re.search(r"(flowchart\s+\w+[\s\S]+)", response)
        if flowchart_match:
            return flowchart_match.group(1).strip()

        # Return basic diagram as fallback
        first_action = flow.steps[0].action if flow.steps else "Process"
        return f"""flowchart TD
    A[Start: {flow.name}] --> B[{first_action}]
    B --> C[End]"""
