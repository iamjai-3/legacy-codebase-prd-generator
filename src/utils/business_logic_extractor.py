"""
Business Logic Extractor for Java Legacy Code.

This module provides utilities to extract structured business logic patterns
from Java source code, specifically targeting Java Swing legacy applications.
"""

import re
from dataclasses import dataclass, field


@dataclass
class ExtractedBusinessRule:
    """Represents an extracted business rule from code."""
    rule_type: str  # validation, calculation, workflow, condition
    description: str
    source_method: str
    source_file: str
    line_range: str
    code_snippet: str


@dataclass
class ExtractedFieldMapping:
    """Represents a field code to description mapping."""
    field_code: str
    description: str
    source_file: str


class JavaBusinessLogicExtractor:
    """Extracts business logic patterns from Java Swing legacy code."""
    
    def __init__(self):
        """Initialize the extractor."""
        pass
    
    def extract_validation_rules(self, java_content: str, file_path: str = "") -> list[ExtractedBusinessRule]:
        """
        Extract validation rules from Java code.
        
        Looks for patterns like:
        - if (condition) { showMessage/setInfo/JOptionPane }
        - validateXxx methods
        - setMandatory calls
        """
        rules = []
        
        # Pattern 1: Find validation messages with conditions
        # Matches: if (condition) { .setInfo("message", "E/W"); }
        validation_pattern = r'if\s*\(([^)]+)\)\s*\{[^}]*(?:setInfo|showMessage|JOptionPane\.showMessageDialog)\s*\([^"]*"([^"]+)"'
        
        matches = re.finditer(validation_pattern, java_content, re.MULTILINE | re.DOTALL)
        for match in matches:
            condition = match.group(1).strip()
            message = match.group(2).strip()
            
            # Find the line number
            line_num = java_content[:match.start()].count('\n') + 1
            
            rules.append(ExtractedBusinessRule(
                rule_type="validation",
                description=f"Validation: {message}",
                source_method=self._find_enclosing_method(java_content, match.start()),
                source_file=file_path,
                line_range=str(line_num),
                code_snippet=match.group(0)[:200]
            ))
        
        # Pattern 2: Find parseInt/parseDouble validations
        numeric_pattern = r'try\s*\{[^}]*(?:parseInt|parseDouble)\s*\([^)]*\)[^}]*\}\s*catch[^}]+\{[^}]*(?:warningMessage|setInfo|showMessage)\s*\([^"]*"([^"]+)"'
        
        matches = re.finditer(numeric_pattern, java_content, re.MULTILINE | re.DOTALL)
        for match in matches:
            message = match.group(1).strip()
            line_num = java_content[:match.start()].count('\n') + 1
            
            rules.append(ExtractedBusinessRule(
                rule_type="validation",
                description=f"Numeric validation: {message}",
                source_method=self._find_enclosing_method(java_content, match.start()),
                source_file=file_path,
                line_range=str(line_num),
                code_snippet=match.group(0)[:200]
            ))
        
        return rules
    
    def extract_conditional_logic(self, java_content: str, file_path: str = "") -> list[ExtractedBusinessRule]:
        """
        Extract conditional business logic from Java code.
        
        Looks for patterns like:
        - if (getData().equals("Y")) { ... }
        - switch statements on business conditions
        """
        rules = []
        
        # Pattern: if statements with business data checks
        business_if_pattern = r'if\s*\(\s*([^)]*(?:getData|getText|getSelectedItem|equals|trim)[^)]*)\s*\)\s*\{([^}]{20,200})'
        
        matches = re.finditer(business_if_pattern, java_content, re.MULTILINE)
        for match in matches:
            condition = match.group(1).strip()
            body_preview = match.group(2).strip()[:100]
            line_num = java_content[:match.start()].count('\n') + 1
            
            rules.append(ExtractedBusinessRule(
                rule_type="condition",
                description=f"Condition: {condition}",
                source_method=self._find_enclosing_method(java_content, match.start()),
                source_file=file_path,
                line_range=str(line_num),
                code_snippet=f"if ({condition}) {{ {body_preview}... }}"
            ))
        
        return rules
    
    def extract_field_mappings(self, java_content: str, file_path: str = "") -> list[ExtractedFieldMapping]:
        """
        Extract legacy field code mappings from Java code.
        
        Looks for patterns like:
        - setFD("LEBDES")
        - getData("WCHDES")
        - setDataList(new String[][] {{"WCHAPT", "W2CHSB"}})
        """
        mappings = []
        
        # Pattern 1: setFD with field codes
        fd_pattern = r'(\w+)\.setFD\s*\(\s*"([A-Z0-9_]{4,20})"\s*\)'
        
        matches = re.finditer(fd_pattern, java_content)
        for match in matches:
            component = match.group(1)
            field_code = match.group(2)
            
            mappings.append(ExtractedFieldMapping(
                field_code=field_code,
                description=f"Component: {component}",
                source_file=file_path
            ))
        
        # Pattern 2: getData/setData with field codes
        data_pattern = r'(?:getData|setData)\s*\(\s*"([A-Z0-9_]{4,20})"\s*\)'
        
        matches = re.finditer(data_pattern, java_content)
        for match in matches:
            field_code = match.group(1)
            mappings.append(ExtractedFieldMapping(
                field_code=field_code,
                description="Data field",
                source_file=file_path
            ))
        
        # Pattern 3: Field codes in setDataList arrays
        datalist_pattern = r'setDataList\s*\(\s*new\s+String\[\]\[\]\s*\{\s*\{([^}]+)\}'
        
        matches = re.finditer(datalist_pattern, java_content)
        for match in matches:
            fields_str = match.group(1)
            # Extract individual field codes from the array
            field_codes = re.findall(r'"([A-Z0-9_]{4,20})"', fields_str)
            for fc in field_codes:
                mappings.append(ExtractedFieldMapping(
                    field_code=fc,
                    description="DataBlock field",
                    source_file=file_path
                ))
        
        # Remove duplicates
        seen = set()
        unique_mappings = []
        for m in mappings:
            if m.field_code not in seen:
                seen.add(m.field_code)
                unique_mappings.append(m)
        
        return unique_mappings
    
    def extract_action_handlers(self, java_content: str, file_path: str = "") -> list[ExtractedBusinessRule]:
        """
        Extract action handler methods (actionPerformed patterns).
        """
        rules = []
        
        # Find actionPerformed methods
        action_pattern = r'(\w+ActionPerformed)\s*\([^)]*\)\s*\{[^}]{20,500}'
        
        matches = re.finditer(action_pattern, java_content, re.MULTILINE)
        for match in matches:
            method_name = match.group(1)
            body_preview = match.group(0)[len(method_name):].strip()[:200]
            line_num = java_content[:match.start()].count('\n') + 1
            
            rules.append(ExtractedBusinessRule(
                rule_type="action_handler",
                description=f"UI Action: {method_name}",
                source_method=method_name,
                source_file=file_path,
                line_range=str(line_num),
                code_snippet=body_preview
            ))
        
        return rules
    
    def extract_save_methods(self, java_content: str, file_path: str = "") -> list[ExtractedBusinessRule]:
        """
        Extract save/persist methods containing business logic.
        """
        rules = []
        
        # Find save methods
        save_pattern = r'(?:public|private|protected)?\s*(?:boolean|void)?\s*(save\w*|persist\w*|update\w*)\s*\([^)]*\)\s*\{([^}]{50,1000})'
        
        matches = re.finditer(save_pattern, java_content, re.MULTILINE | re.DOTALL)
        for match in matches:
            method_name = match.group(1)
            body = match.group(2).strip()[:300]
            line_num = java_content[:match.start()].count('\n') + 1
            
            rules.append(ExtractedBusinessRule(
                rule_type="save_operation",
                description=f"Save method: {method_name}",
                source_method=method_name,
                source_file=file_path,
                line_range=str(line_num),
                code_snippet=body
            ))
        
        return rules
    
    def extract_configuration_checks(self, java_content: str, file_path: str = "") -> list[ExtractedBusinessRule]:
        """
        Extract configuration check methods like usingSubChapters(), usingRepDefs().
        
        Looks for patterns like:
        - usingSubChapters()
        - usingRepDefs()
        - checkUsingXxx()
        - isXxxEnabled()
        """
        rules = []
        
        # Pattern 1: Configuration check methods
        config_pattern = r'(?:public|private|protected)?\s*static\s+boolean\s+(using\w+|check\w+|is\w+Enabled)\s*\([^)]*\)\s*\{([^}]{50,500})'
        
        matches = re.finditer(config_pattern, java_content, re.MULTILINE | re.DOTALL)
        for match in matches:
            method_name = match.group(1)
            body = match.group(2).strip()[:300]
            line_num = java_content[:match.start()].count('\n') + 1
            
            rules.append(ExtractedBusinessRule(
                rule_type="configuration_check",
                description=f"Configuration check: {method_name}",
                source_method=method_name,
                source_file=file_path,
                line_range=str(line_num),
                code_snippet=body
            ))
        
        return rules
    
    def extract_validation_functions(self, java_content: str, file_path: str = "") -> list[ExtractedBusinessRule]:
        """
        Extract validation functions like doesChapterRecordExist(), doesSubChapterRecordExist().
        
        Looks for patterns like:
        - doesXxxRecordExist()
        - doesXxxExist()
        - checkXxxExists()
        """
        rules = []
        
        # Pattern: Validation/existence check methods
        validation_func_pattern = r'(?:public|private|protected)?\s*static\s+boolean\s+(does\w+RecordExist|does\w+Exist|check\w+Exists)\s*\([^)]*\)\s*\{([^}]{50,500})'
        
        matches = re.finditer(validation_func_pattern, java_content, re.MULTILINE | re.DOTALL)
        for match in matches:
            method_name = match.group(1)
            body = match.group(2).strip()[:300]
            line_num = java_content[:match.start()].count('\n') + 1
            
            rules.append(ExtractedBusinessRule(
                rule_type="validation_function",
                description=f"Validation function: {method_name}",
                source_method=method_name,
                source_file=file_path,
                line_range=str(line_num),
                code_snippet=body
            ))
        
        return rules
    
    def extract_fleet_specific_logic(self, java_content: str, file_path: str = "") -> list[ExtractedBusinessRule]:
        """
        Extract fleet-specific logic patterns.
        
        Looks for patterns like:
        - Methods with 'fleet' parameter
        - Fleet-specific conditions
        - Fleet-based filtering or validation
        """
        rules = []
        
        # Pattern 1: Methods with fleet parameter
        fleet_method_pattern = r'(?:public|private|protected)?\s+(?:\w+\s+)?(\w+)\s*\([^)]*fleet[^)]*\)\s*\{'
        
        matches = re.finditer(fleet_method_pattern, java_content, re.MULTILINE | re.IGNORECASE)
        for match in matches:
            method_name = match.group(1)
            # Extract method body
            method_start = match.end()
            brace_count = 1
            method_end = method_start
            while method_end < len(java_content) and brace_count > 0:
                if java_content[method_end] == '{':
                    brace_count += 1
                elif java_content[method_end] == '}':
                    brace_count -= 1
                method_end += 1
            
            if method_end > method_start:
                body = java_content[method_start:method_end][:500]
                line_num = java_content[:match.start()].count('\n') + 1
                
                rules.append(ExtractedBusinessRule(
                    rule_type="fleet_specific",
                    description=f"Fleet-specific method: {method_name}",
                    source_method=method_name,
                    source_file=file_path,
                    line_range=str(line_num),
                    code_snippet=body
                ))
        
        # Pattern 2: Fleet-specific conditions
        fleet_condition_pattern = r'if\s*\([^)]*fleet[^)]*\)\s*\{([^}]{20,300})'
        
        matches = re.finditer(fleet_condition_pattern, java_content, re.MULTILINE | re.IGNORECASE)
        for match in matches:
            condition_body = match.group(1).strip()[:200]
            line_num = java_content[:match.start()].count('\n') + 1
            
            rules.append(ExtractedBusinessRule(
                rule_type="fleet_condition",
                description=f"Fleet-specific condition",
                source_method=self._find_enclosing_method(java_content, match.start()),
                source_file=file_path,
                line_range=str(line_num),
                code_snippet=f"if (fleet condition) {{ {condition_body} }}"
            ))
        
        return rules
    
    def extract_alert_rate_management(self, java_content: str, file_path: str = "") -> list[ExtractedBusinessRule]:
        """
        Extract alert rate management logic.
        
        Looks for patterns like:
        - alertLimit calculations
        - alert rate validations
        - removalAlertRate logic
        """
        rules = []
        
        # Pattern: Alert limit related code
        alert_pattern = r'(?:alertLimit|removalAlertRate|alertRate|alert_limit)[\s\S]{0,200}'
        
        matches = re.finditer(alert_pattern, java_content, re.MULTILINE | re.IGNORECASE)
        for match in matches:
            snippet = match.group(0)[:300]
            line_num = java_content[:match.start()].count('\n') + 1
            
            # Check if it's in a method context
            method_name = self._find_enclosing_method(java_content, match.start())
            
            rules.append(ExtractedBusinessRule(
                rule_type="alert_rate",
                description="Alert rate management logic",
                source_method=method_name,
                source_file=file_path,
                line_range=str(line_num),
                code_snippet=snippet
            ))
        
        return rules
    
    def extract_field_dependencies(self, java_content: str, file_path: str = "") -> list[ExtractedBusinessRule]:
        """
        Extract field dependency logic (when field A changes, field B updates).
        
        Looks for patterns like:
        - ActionPerformed methods that update other fields
        - Field change listeners
        - Dependent field updates
        """
        rules = []
        
        # Pattern: ActionPerformed methods that might update dependent fields
        action_pattern = r'(\w+ActionPerformed)\s*\([^)]*\)\s*\{([^}]{100,1000})'
        
        matches = re.finditer(action_pattern, java_content, re.MULTILINE | re.DOTALL)
        for match in matches:
            method_name = match.group(1)
            body = match.group(2)
            
            # Check if body contains setData, setText, or similar update calls
            if re.search(r'(?:setData|setText|setValue|setEnabled|setVisible)\s*\(', body):
                line_num = java_content[:match.start()].count('\n') + 1
                
                rules.append(ExtractedBusinessRule(
                    rule_type="field_dependency",
                    description=f"Field dependency in {method_name}",
                    source_method=method_name,
                    source_file=file_path,
                    line_range=str(line_num),
                    code_snippet=body[:300]
                ))
        
        return rules
    
    def extract_state_transitions(self, java_content: str, file_path: str = "") -> list[ExtractedBusinessRule]:
        """
        Extract state transition logic (enabled/disabled, visible/invisible).
        
        Looks for patterns like:
        - setEnabled(true/false)
        - setVisible(true/false)
        - Component state changes
        """
        rules = []
        
        # Pattern: State transition calls
        state_pattern = r'(?:setEnabled|setVisible|setEditable|setMandatory)\s*\(\s*(true|false|!?\w+)\s*\)'
        
        matches = re.finditer(state_pattern, java_content, re.MULTILINE)
        for match in matches:
            state_call = match.group(0)
            state_value = match.group(1)
            line_num = java_content[:match.start()].count('\n') + 1
            
            # Get context around the call
            context_start = max(0, match.start() - 100)
            context_end = min(len(java_content), match.end() + 100)
            context = java_content[context_start:context_end]
            
            rules.append(ExtractedBusinessRule(
                rule_type="state_transition",
                description=f"State transition: {state_call}",
                source_method=self._find_enclosing_method(java_content, match.start()),
                source_file=file_path,
                line_range=str(line_num),
                code_snippet=context
            ))
        
        return rules
    
    def _find_enclosing_method(self, content: str, position: int) -> str:
        """Find the method that contains the given position."""
        # Look backwards for method signature
        search_text = content[:position]
        
        # Find the last method definition before this position
        method_pattern = r'(?:public|private|protected)?\s*(?:\w+\s+)?(\w+)\s*\([^)]*\)\s*\{'
        
        matches = list(re.finditer(method_pattern, search_text))
        if matches:
            return matches[-1].group(1)
        
        return "unknown"


def extract_business_logic_summary(java_content: str, file_path: str = "") -> str:
    """
    Extract a comprehensive business logic summary from Java code.
    
    Returns a formatted string suitable for LLM prompting.
    """
    extractor = JavaBusinessLogicExtractor()
    
    sections = []
    
    # Extract validation rules
    validations = extractor.extract_validation_rules(java_content, file_path)
    if validations:
        sections.append("## Validation Rules")
        for v in validations:
            sections.append(f"- **{v.description}** in `{v.source_method}` (line {v.line_range})")
            sections.append(f"  ```java\n  {v.code_snippet}\n  ```")
    
    # Extract validation functions (NEW)
    validation_funcs = extractor.extract_validation_functions(java_content, file_path)
    if validation_funcs:
        sections.append("\n## Validation Functions")
        for vf in validation_funcs:
            sections.append(f"- **{vf.description}** in `{vf.source_method}` (line {vf.line_range})")
            sections.append(f"  ```java\n  {vf.code_snippet}\n  ```")
    
    # Extract configuration checks (NEW)
    config_checks = extractor.extract_configuration_checks(java_content, file_path)
    if config_checks:
        sections.append("\n## Configuration Checks")
        for cc in config_checks:
            sections.append(f"- **{cc.description}** in `{cc.source_method}` (line {cc.line_range})")
            sections.append(f"  ```java\n  {cc.code_snippet}\n  ```")
    
    # Extract fleet-specific logic (NEW)
    fleet_logic = extractor.extract_fleet_specific_logic(java_content, file_path)
    if fleet_logic:
        sections.append("\n## Fleet-Specific Logic")
        for fl in fleet_logic[:10]:  # Limit to 10
            sections.append(f"- **{fl.description}** in `{fl.source_method}` (line {fl.line_range})")
    
    # Extract alert rate management (NEW)
    alert_rates = extractor.extract_alert_rate_management(java_content, file_path)
    if alert_rates:
        sections.append("\n## Alert Rate Management")
        for ar in alert_rates[:10]:  # Limit to 10
            sections.append(f"- **{ar.description}** in `{ar.source_method}` (line {ar.line_range})")
    
    # Extract field dependencies (NEW)
    field_deps = extractor.extract_field_dependencies(java_content, file_path)
    if field_deps:
        sections.append("\n## Field Dependencies")
        for fd in field_deps[:10]:  # Limit to 10
            sections.append(f"- **{fd.description}** (line {fd.line_range})")
    
    # Extract state transitions (NEW)
    state_trans = extractor.extract_state_transitions(java_content, file_path)
    if state_trans:
        sections.append("\n## State Transitions")
        for st in state_trans[:10]:  # Limit to 10
            sections.append(f"- **{st.description}** in `{st.source_method}` (line {st.line_range})")
    
    # Extract conditional logic
    conditions = extractor.extract_conditional_logic(java_content, file_path)
    if conditions:
        sections.append("\n## Conditional Logic")
        for c in conditions[:10]:  # Limit to 10 most relevant
            sections.append(f"- **{c.description}** in `{c.source_method}`")
    
    # Extract field mappings
    mappings = extractor.extract_field_mappings(java_content, file_path)
    if mappings:
        sections.append("\n## Field Code Mappings")
        for m in mappings:
            sections.append(f"- `{m.field_code}`: {m.description}")
    
    # Extract action handlers
    actions = extractor.extract_action_handlers(java_content, file_path)
    if actions:
        sections.append("\n## Action Handlers")
        for a in actions:
            sections.append(f"- **{a.description}**")
    
    # Extract save methods
    saves = extractor.extract_save_methods(java_content, file_path)
    if saves:
        sections.append("\n## Save Operations")
        for s in saves:
            sections.append(f"- **{s.description}** (line {s.line_range})")
    
    return "\n".join(sections) if sections else "No business logic patterns detected."
