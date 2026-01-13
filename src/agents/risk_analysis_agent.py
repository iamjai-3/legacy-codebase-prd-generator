"""
Risk Analysis Agent for identifying migration risks and mitigation strategies.

Analyzes code and requirements to identify technical, business, and resource
risks associated with legacy system migration.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any

from src.agents.base_agent import AgentContext, AgentResult, BaseAgent
from src.prompts.risk_analysis import RiskAnalysisPrompts
from src.utils.logging_config import ExecutionTimer
from src.utils.serialization import extract_json_array


class RiskSeverity(Enum):
    """Risk severity levels."""

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RiskCategory(Enum):
    """Risk category types."""

    TECHNICAL = "technical"
    BUSINESS = "business"
    RESOURCE = "resource"
    TIMELINE = "timeline"
    INTEGRATION = "integration"
    DATA = "data"
    SECURITY = "security"


@dataclass
class Risk:
    """A single identified risk."""

    risk_id: str
    title: str
    description: str
    category: str
    severity: str
    likelihood: str  # high, medium, low
    impact: str
    affected_areas: list[str]
    mitigation_strategies: list[str]
    contingency_plan: str
    owner: str
    status: str  # identified, mitigating, resolved, accepted


@dataclass
class RiskMatrix:
    """Risk assessment matrix."""

    critical_count: int
    high_count: int
    medium_count: int
    low_count: int
    risk_score: float  # Overall risk score 0-100


@dataclass
class RiskAnalysisResult:
    """Complete risk analysis result."""

    form_name: str
    risks: list[Risk]
    risk_matrix: RiskMatrix
    top_risks: list[str]
    migration_complexity: str  # low, medium, high, very_high
    recommended_approach: str
    dependencies_risks: list[str]
    technical_debt_items: list[str]
    success_factors: list[str]
    executive_summary: str


class RiskAnalysisAgent(BaseAgent[RiskAnalysisResult]):
    """
    Agent for analyzing migration risks and developing mitigation strategies.
    Identifies technical, business, and resource risks.
    """

    def __init__(self) -> None:
        """Initialize the risk analysis agent."""
        super().__init__("RiskAnalysisAgent")

    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt for risk analysis."""
        return RiskAnalysisPrompts.system_prompt(context.form_name)

    async def analyze(
        self,
        context: AgentContext,
        code_analysis: dict[str, Any] | None = None,
        requirements_analysis: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> AgentResult[RiskAnalysisResult]:
        """
        Perform risk analysis for migration.

        Args:
            context: Agent execution context
            code_analysis: Results from code analysis
            requirements_analysis: Results from requirements analysis

        Returns:
            AgentResult with RiskAnalysisResult
        """
        timer = ExecutionTimer()

        self.logger.info(
            "Starting risk analysis",
            form_name=context.form_name,
            has_code_analysis=code_analysis is not None,
        )

        try:
            # Retrieve context from vector store
            stored_context = self.retrieve_context(
                context.form_name, "dependencies complexity integration legacy technical", limit=10
            )

            # Identify and analyze risks
            risks = await self._identify_risks(context, stored_context, code_analysis)
            risk_matrix = self._calculate_risk_matrix(risks)
            top_risks = self._get_top_risks(risks)

            # Assess complexity and approach
            migration_complexity = self._assess_complexity(risks)
            recommended_approach = await self._recommend_approach(
                context, risks, migration_complexity
            )

            # Identify additional risk factors
            dependency_risks = await self._identify_dependency_risks(context, stored_context)
            technical_debt = await self._identify_technical_debt(context, code_analysis)
            success_factors = await self._identify_success_factors(context, risks)

            # Generate executive summary
            executive_summary = await self._generate_summary(
                context, risks, risk_matrix, migration_complexity
            )

            result = RiskAnalysisResult(
                form_name=context.form_name,
                risks=risks,
                risk_matrix=risk_matrix,
                top_risks=top_risks,
                migration_complexity=migration_complexity,
                recommended_approach=recommended_approach,
                dependencies_risks=dependency_risks,
                technical_debt_items=technical_debt,
                success_factors=success_factors,
                executive_summary=executive_summary,
            )

            self.logger.info(
                "Risk analysis complete",
                form_name=context.form_name,
                total_risks=len(risks),
                critical_risks=risk_matrix.critical_count,
                complexity=migration_complexity,
                duration_ms=timer.elapsed_ms(),
            )

            return self.create_success_result(result, timer)

        except Exception as e:
            return self.create_error_result(e, timer)

    async def _identify_risks(
        self, context: AgentContext, stored_context: list[str], code_analysis: dict[str, Any] | None
    ) -> list[Risk]:
        """Identify all risks for the migration."""
        context_text = self.format_context_for_prompt(stored_context, max_contexts=5)
        code_info = self._format_code_metrics(code_analysis)

        prompt = f"""Identify risks for migrating "{context.form_name}":

{context_text}
{code_info}

Generate risks in JSON array format:
[
    {{
        "risk_id": "RISK-001",
        "title": "Risk title",
        "description": "Detailed description",
        "category": "technical|business|resource|timeline|integration|data|security",
        "severity": "critical|high|medium|low",
        "likelihood": "high|medium|low",
        "impact": "Description of impact",
        "affected_areas": ["Area 1", "Area 2"],
        "mitigation_strategies": ["Strategy 1", "Strategy 2"],
        "contingency_plan": "What to do if risk materializes",
        "owner": "Role responsible",
        "status": "identified"
    }}
]

Identify 8-12 risks across different categories."""

        data = extract_json_array(await self.invoke_llm(context, prompt))

        if data:
            return [
                Risk(
                    risk_id=r.get("risk_id", f"RISK-{i:03d}"),
                    title=r.get("title", ""),
                    description=r.get("description", ""),
                    category=r.get("category", "technical"),
                    severity=r.get("severity", "medium"),
                    likelihood=r.get("likelihood", "medium"),
                    impact=r.get("impact", ""),
                    affected_areas=r.get("affected_areas", []),
                    mitigation_strategies=r.get("mitigation_strategies", []),
                    contingency_plan=r.get("contingency_plan", ""),
                    owner=r.get("owner", "Project Manager"),
                    status=r.get("status", "identified"),
                )
                for i, r in enumerate(data, 1)
            ]

        # Return default risk if parsing fails
        return [self._create_default_risk()]

    def _format_code_metrics(self, code_analysis: dict[str, Any] | None) -> str:
        """Format code analysis metrics for prompt."""
        if not code_analysis:
            return ""

        return f"""
Code metrics:
- Files: {code_analysis.get("file_count", "Unknown")}
- Languages: {code_analysis.get("languages", "Unknown")}
- Dependencies: {code_analysis.get("dependencies", [])}
"""

    def _create_default_risk(self) -> Risk:
        """Create a default risk when analysis fails."""
        return Risk(
            risk_id="RISK-001",
            title="Unknown Legacy Code Behavior",
            description="Undocumented functionality in legacy code may be missed during migration",
            category="technical",
            severity="high",
            likelihood="medium",
            impact="Missing features in new system",
            affected_areas=["All modules"],
            mitigation_strategies=[
                "Thorough code review",
                "Stakeholder interviews",
                "Parallel testing",
            ],
            contingency_plan="Extended testing period with rollback capability",
            owner="Technical Lead",
            status="identified",
        )

    def _calculate_risk_matrix(self, risks: list[Risk]) -> RiskMatrix:
        """Calculate the risk assessment matrix."""
        severity_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}

        for risk in risks:
            severity = risk.severity.lower()
            if severity in severity_counts:
                severity_counts[severity] += 1

        # Calculate weighted risk score (0-100)
        weights = {"critical": 10, "high": 5, "medium": 2, "low": 1}
        total_weight = sum(weights[s] * c for s, c in severity_counts.items())
        max_weight = len(risks) * 10 if risks else 1
        risk_score = min(100, (total_weight / max_weight) * 100)

        return RiskMatrix(
            critical_count=severity_counts["critical"],
            high_count=severity_counts["high"],
            medium_count=severity_counts["medium"],
            low_count=severity_counts["low"],
            risk_score=round(risk_score, 1),
        )

    def _get_top_risks(self, risks: list[Risk], limit: int = 5) -> list[str]:
        """Get the top risks by severity."""
        severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        sorted_risks = sorted(
            risks, key=lambda r: (severity_order.get(r.severity.lower(), 4), r.likelihood != "high")
        )
        return [f"{r.risk_id}: {r.title}" for r in sorted_risks[:limit]]

    def _assess_complexity(self, risks: list[Risk]) -> str:
        """Assess the overall migration complexity based on risk profile."""
        critical_count = sum(1 for r in risks if r.severity == "critical")
        high_count = sum(1 for r in risks if r.severity == "high")

        if critical_count >= 2 or (critical_count >= 1 and high_count >= 3):
            return "very_high"
        elif critical_count >= 1 or high_count >= 3:
            return "high"
        elif high_count >= 1:
            return "medium"
        return "low"

    async def _recommend_approach(
        self, context: AgentContext, risks: list[Risk], complexity: str
    ) -> str:
        """Recommend a migration approach based on risks."""
        risk_summary = ", ".join([f"{r.risk_id}: {r.severity}" for r in risks[:5]])

        prompt = f"""Based on the risk assessment for "{context.form_name}":

Complexity: {complexity}
Key risks: {risk_summary}

Recommend a migration approach. Consider:
- Big bang vs phased migration
- Strangler pattern
- Parallel running
- Data migration strategy
- Rollback strategy

Provide a 2-paragraph recommendation."""

        return await self.invoke_llm(context, prompt)

    async def _identify_dependency_risks(
        self, context: AgentContext, stored_context: list[str]
    ) -> list[str]:
        """Identify risks related to dependencies."""
        context_text = self.format_context_for_prompt(stored_context, max_contexts=3)

        prompt = f"""For "{context.form_name}", identify dependency-related risks:

{context_text}

Consider:
- External system dependencies
- Library/framework dependencies
- Data dependencies
- Timing dependencies
- Circular dependencies

List each as a specific risk statement."""

        items = await self.invoke_llm_for_list(context, prompt)
        return [item for item in items if len(item) > 10][:10]

    async def _identify_technical_debt(
        self, context: AgentContext, code_analysis: dict[str, Any] | None
    ) -> list[str]:
        """Identify technical debt items."""
        prompt = f"""For migrating "{context.form_name}", list technical debt items that should be addressed:

Consider:
- Code quality issues
- Missing documentation
- Hardcoded values
- Deprecated technologies
- Security vulnerabilities
- Performance bottlenecks
- Test coverage gaps

List each item with a brief description."""

        items = await self.invoke_llm_for_list(context, prompt)
        return [item for item in items if len(item) > 10][:10]

    async def _identify_success_factors(
        self, context: AgentContext, risks: list[Risk]
    ) -> list[str]:
        """Identify critical success factors."""
        risk_categories = ", ".join({r.category for r in risks})

        prompt = f"""For successful migration of "{context.form_name}", identify critical success factors.

Risk areas to address: {risk_categories}

List 5-8 critical success factors that will determine project success."""

        items = await self.invoke_llm_for_list(context, prompt)
        return [item for item in items if len(item) > 10][:8]

    async def _generate_summary(
        self, context: AgentContext, risks: list[Risk], risk_matrix: RiskMatrix, complexity: str
    ) -> str:
        """Generate executive summary of risk analysis."""
        prompt = f"""Provide an executive summary of the risk analysis for "{context.form_name}" migration:

Risk Matrix:
- Critical risks: {risk_matrix.critical_count}
- High risks: {risk_matrix.high_count}
- Medium risks: {risk_matrix.medium_count}
- Low risks: {risk_matrix.low_count}
- Overall risk score: {risk_matrix.risk_score}/100

Migration complexity: {complexity}

Top risks:
{chr(10).join([f"- {r.title}: {r.severity}" for r in risks[:5]])}

Write a 2-3 paragraph executive summary suitable for senior stakeholders."""

        return await self.invoke_llm(context, prompt)
