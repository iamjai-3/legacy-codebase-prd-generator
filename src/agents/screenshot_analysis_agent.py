"""
Screenshot Analysis Agent for analyzing UI screenshots and extracting UI/UX insights.

Uses vision capabilities to analyze UI components, layout, and user interactions
from legacy application screenshots.
"""

from dataclasses import dataclass, field
from typing import Any

from src.agents.base_agent import AgentContext, AgentResult, BaseAgent
from src.extractors.minio_extractor import MinioExtractor, Screenshot
from src.prompts.screenshot_analysis import ScreenshotAnalysisPrompts
from src.utils.logging_config import ExecutionTimer


@dataclass
class UIElement:
    """Represents a detected UI element."""
    
    element_type: str  # button, input, table, form, etc.
    label: str
    description: str
    location: str  # top, bottom, left, right, center
    interactions: list[str] = field(default_factory=list)


@dataclass
class ScreenAnalysis:
    """Analysis result for a single screen."""
    
    screen_name: str
    screen_type: str
    purpose: str
    ui_elements: list[UIElement]
    layout_description: str
    user_actions: list[str]
    data_displayed: list[str]
    validation_rules: list[str]
    accessibility_notes: list[str]


@dataclass
class ScreenshotAnalysisResult:
    """Complete screenshot analysis result."""
    
    form_name: str
    total_screens: int
    screen_analyses: list[ScreenAnalysis]
    ui_flow_summary: str
    common_patterns: list[str]
    component_inventory: dict[str, int]
    recommendations: list[str]


class ScreenshotAnalysisAgent(BaseAgent[ScreenshotAnalysisResult]):
    """
    Agent for analyzing UI screenshots using vision capabilities.
    Extracts UI components, layout information, and user interaction patterns.
    """
    
    def __init__(self) -> None:
        """Initialize the screenshot analysis agent."""
        super().__init__("ScreenshotAnalysisAgent")
        self.minio_extractor = MinioExtractor()
        # Override LLM to use vision-capable model
        from langchain_openai import ChatOpenAI

        from src.config.settings import get_settings

        settings = get_settings()
        # Use configured model if it supports vision, otherwise default to gpt-4o
        vision_model = settings.openai.model if "gpt-4o" in settings.openai.model else "gpt-4o"
        self._llm = ChatOpenAI(
            model=vision_model,
            openai_api_key=settings.openai.api_key,
            temperature=settings.openai.temperature,
            max_tokens=settings.openai.max_tokens,
        )
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt for screenshot analysis."""
        return ScreenshotAnalysisPrompts.system_prompt(context.form_name)
    
    async def analyze(
        self,
        context: AgentContext,
        screenshots: list[Screenshot] | None = None,
        bucket: str | None = None,
        **kwargs: Any,
    ) -> AgentResult[ScreenshotAnalysisResult]:
        """
        Analyze screenshots for a form.
        
        Args:
            context: Agent execution context
            screenshots: Optional pre-loaded screenshots
            bucket: Optional Minio bucket name
            
        Returns:
            AgentResult with ScreenshotAnalysisResult
        """
        timer = ExecutionTimer()

        self.logger.info(
            "Starting screenshot analysis",
            form_name=context.form_name,
            screenshots_provided=screenshots is not None,
        )
        
        try:
            # Get screenshots if not provided
            if screenshots is None:
                screenshots = self.minio_extractor.get_form_screenshots(
                    form_name=context.form_name, bucket=bucket
                )
            
            if not screenshots:
                return self.create_error_result(
                    f"No screenshots found for form: {context.form_name}", timer
                )
            
            # Analyze each screenshot and build component inventory
            screen_analyses, component_inventory = await self._analyze_all_screenshots(
                context, screenshots
            )
            
            # Generate overall analysis
            ui_flow_summary = await self._generate_flow_summary(context, screen_analyses)
            common_patterns = self._identify_common_patterns(screen_analyses)
            recommendations = await self._generate_recommendations(
                context, screen_analyses, component_inventory
            )
            
            result = ScreenshotAnalysisResult(
                form_name=context.form_name,
                total_screens=len(screenshots),
                screen_analyses=screen_analyses,
                ui_flow_summary=ui_flow_summary,
                common_patterns=common_patterns,
                component_inventory=component_inventory,
                recommendations=recommendations,
            )
            
            self.logger.info(
                "Screenshot analysis complete",
                form_name=context.form_name,
                screens_analyzed=len(screen_analyses),
                components_found=sum(component_inventory.values()),
                duration_ms=timer.elapsed_ms(),
            )
            
            return self.create_success_result(result, timer)
            
        except Exception as e:
            return self.create_error_result(e, timer)

    async def _analyze_all_screenshots(
        self, context: AgentContext, screenshots: list[Screenshot]
    ) -> tuple[list[ScreenAnalysis], dict[str, int]]:
        """Analyze all screenshots and build component inventory."""
        screen_analyses: list[ScreenAnalysis] = []
        component_inventory: dict[str, int] = {}

        for screenshot in screenshots:
            analysis = await self._analyze_single_screenshot(context, screenshot)
            if analysis:
                screen_analyses.append(analysis)
                for element in analysis.ui_elements:
                    component_inventory[element.element_type] = (
                        component_inventory.get(element.element_type, 0) + 1
                    )

        return screen_analyses, component_inventory
    
    async def _analyze_single_screenshot(
        self, context: AgentContext, screenshot: Screenshot
    ) -> ScreenAnalysis | None:
        """Analyze a single screenshot."""
        try:
            # Convert image to base64
            image_b64 = self.minio_extractor.get_image_base64(screenshot)
            
            prompt = f"""Analyze this screenshot from the "{context.form_name}" application.

Provide a detailed analysis in the following JSON structure:
{{
    "screen_name": "Name for this screen",
    "screen_type": "form|list|detail|dialog|report|navigation",
    "purpose": "Brief description of the screen's purpose",
    "layout_description": "Description of the layout",
    "ui_elements": [
        {{
            "element_type": "button|input|dropdown|table|label|checkbox|radio|etc",
            "label": "Element label or identifier",
            "description": "What this element does",
            "location": "Where on screen",
            "interactions": ["click", "input", "select", etc]
        }}
    ],
    "user_actions": ["List of actions user can perform"],
    "data_displayed": ["Types of data shown"],
    "validation_rules": ["Inferred validation rules"],
    "accessibility_notes": ["Accessibility observations"]
}}

Be thorough in identifying all UI elements."""

            response = await self.invoke_llm(context, prompt, images=[image_b64])
            
            # Parse the response
            import json
            import re
            
            # Extract JSON from response
            json_match = re.search(r"\{[\s\S]*\}", response)
            if json_match:
                data = json.loads(json_match.group())
                
                ui_elements = [
                    UIElement(
                        element_type=elem.get("element_type", "unknown"),
                        label=elem.get("label", ""),
                        description=elem.get("description", ""),
                        location=elem.get("location", ""),
                        interactions=elem.get("interactions", []),
                    )
                    for elem in data.get("ui_elements", [])
                ]
                
                return ScreenAnalysis(
                    screen_name=data.get("screen_name", screenshot.object_name),
                    screen_type=data.get("screen_type", screenshot.screen_type),
                    purpose=data.get("purpose", ""),
                    ui_elements=ui_elements,
                    layout_description=data.get("layout_description", ""),
                    user_actions=data.get("user_actions", []),
                    data_displayed=data.get("data_displayed", []),
                    validation_rules=data.get("validation_rules", []),
                    accessibility_notes=data.get("accessibility_notes", []),
                )
            
            return None
            
        except Exception as e:
            self.logger.warning(
                "Failed to analyze screenshot", screenshot=screenshot.object_name, error=str(e)
            )
            return None
    
    async def _generate_flow_summary(
        self, context: AgentContext, analyses: list[ScreenAnalysis]
    ) -> str:
        """Generate a summary of the UI flow."""
        if not analyses:
            return "No screens analyzed."
        
        screen_descriptions = "\n".join(
            [f"- {a.screen_name} ({a.screen_type}): {a.purpose}" for a in analyses]
        )
        
        prompt = f"""Based on these screens from the "{context.form_name}" module:

{screen_descriptions}

Provide a concise summary of the overall UI flow and user journey through this module.
Focus on how screens connect and the primary user workflow."""

        return await self.invoke_llm(context, prompt)
    
    def _identify_common_patterns(self, analyses: list[ScreenAnalysis]) -> list[str]:
        """Identify common UI patterns across screens."""
        patterns: list[str] = []
        
        # Check for common patterns
        has_list_detail = any(a.screen_type == "list" for a in analyses) and any(
            a.screen_type == "detail" for a in analyses
        )
        if has_list_detail:
            patterns.append("List-Detail pattern: Master list with detail views")
        
        has_forms = any(a.screen_type == "form" for a in analyses)
        if has_forms:
            patterns.append("Form-based data entry screens")
        
        has_dialogs = any(a.screen_type == "dialog" for a in analyses)
        if has_dialogs:
            patterns.append("Modal dialogs for focused interactions")
        
        # Check for common elements
        all_elements = [e for a in analyses for e in a.ui_elements]
        element_types = [e.element_type for e in all_elements]
        
        if element_types.count("table") > 1:
            patterns.append("Heavy use of tabular data display")
        
        if element_types.count("dropdown") > 3:
            patterns.append("Multiple dropdown selections")
        
        return patterns
    
    async def _generate_recommendations(
        self,
        context: AgentContext,
        analyses: list[ScreenAnalysis],
        component_inventory: dict[str, int],
    ) -> list[str]:
        """Generate modernization recommendations."""
        inventory_str = ", ".join([f"{k}: {v}" for k, v in component_inventory.items()])
        
        prompt = f"""Based on the UI analysis of "{context.form_name}":

Component inventory: {inventory_str}
Number of screens: {len(analyses)}

Provide 5-7 specific recommendations for modernizing this interface.
Consider modern UI/UX best practices, component libraries, and user experience improvements.
Format as a simple list."""

        response = await self.invoke_llm(context, prompt)
        
        # Parse recommendations from response
        lines = response.strip().split("\n")
        recommendations = [
            line.strip().lstrip("0123456789.-) ")
            for line in lines
            if line.strip() and not line.strip().startswith("#")
        ]
        
        return recommendations[:7]  # Limit to 7 recommendations
