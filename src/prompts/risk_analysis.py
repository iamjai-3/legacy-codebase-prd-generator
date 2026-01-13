"""Prompts for Risk Analysis Agent."""


class RiskAnalysisPrompts:
    """Prompts used by the RiskAnalysisAgent."""

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for risk analysis."""
        return f"""You are a technical risk analyst specializing in legacy system migration projects.
Your task is to identify and assess risks for migrating the "{form_name}" module.

When analyzing risks:
1. Identify technical risks (complexity, dependencies, unknown technologies)
2. Identify business risks (functionality gaps, user impact)
3. Identify resource risks (skills, availability)
4. Identify data risks (migration, integrity, compatibility)
5. Identify integration risks (API changes, third-party dependencies)
6. Identify security risks (new vulnerabilities, compliance)
7. Develop mitigation strategies for each risk
8. Create contingency plans for critical risks

Risk assessment should:
- Be realistic and actionable
- Prioritize risks by impact and likelihood
- Provide specific mitigation strategies
- Consider dependencies between risks

This analysis will guide migration planning and resource allocation."""

    @staticmethod
    def identify_risks(form_name: str, context_text: str, code_info: str) -> str:
        """Prompt for identifying migration risks."""
        return f"""Identify risks for migrating "{form_name}":

Context from analysis:
{context_text}

{code_info}

For each risk, respond in JSON array format:
[
    {{
        "title": "Risk title",
        "description": "Detailed risk description",
        "category": "technical|business|resource|timeline|integration|data|security",
        "severity": "critical|high|medium|low",
        "likelihood": "high|medium|low",
        "impact": "Impact description",
        "affected_areas": ["area1", "area2"],
        "mitigation_strategies": ["strategy 1", "strategy 2"],
        "contingency_plan": "Fallback plan if risk occurs",
        "owner": "Suggested owner role",
        "status": "identified"
    }}
]

Identify 5-8 key risks."""

    @staticmethod
    def recommend_approach(form_name: str, risk_summary: str, complexity: str) -> str:
        """Prompt for recommending migration approach."""
        return f"""Based on the risk assessment for "{form_name}":

Risk profile: {risk_summary}
Assessed complexity: {complexity}

Recommend a migration approach:
1. Should this be a big-bang or phased migration?
2. What should be migrated first?
3. What parallel running period is needed?
4. What testing strategy is recommended?
5. What rollback strategy should be in place?

Provide a concise 2-paragraph recommendation."""

    @staticmethod
    def dependency_risks(form_name: str, context_text: str) -> str:
        """Prompt for identifying dependency-related risks."""
        return f"""For "{form_name}", identify dependency-related risks:

Context:
{context_text}

List specific risks related to:
- External system dependencies
- Library/framework dependencies
- Data dependencies
- Team/skill dependencies

Format as a numbered list."""

    @staticmethod
    def technical_debt(form_name: str, code_info: str) -> str:
        """Prompt for identifying technical debt items."""
        return f"""For "{form_name}", identify technical debt items that should be addressed:

{code_info}

Consider:
- Code quality issues
- Architecture problems
- Documentation gaps
- Testing coverage
- Security vulnerabilities

List specific technical debt items."""

    @staticmethod
    def success_factors(form_name: str, risk_categories: str) -> str:
        """Prompt for identifying critical success factors."""
        return f"""For successful migration of "{form_name}", identify critical success factors.

Risk categories identified: {risk_categories}

List factors that are critical for:
- Technical success
- Business success
- User adoption
- Timeline adherence

Format as a numbered list."""

    @staticmethod
    def executive_summary(
        form_name: str,
        total_risks: int,
        critical: int,
        high: int,
        risk_score: float,
        complexity: str,
    ) -> str:
        """Prompt for generating risk analysis summary."""
        return f"""Write an executive summary for the "{form_name}" risk assessment:

- Total risks identified: {total_risks}
- Critical risks: {critical}
- High risks: {high}
- Overall risk score: {risk_score}/100
- Assessed complexity: {complexity}

Provide a 2-paragraph summary for stakeholders covering:
1. Overall risk profile and key concerns
2. Recommended approach and key success factors"""
