"""
Field Mapping Extractor for Legacy to Normalized Schema Mapping.

Extracts field mappings between legacy DTO classes and normalized database schema.
"""

import re
from dataclasses import dataclass
from typing import Any


@dataclass
class FieldMapping:
    """Represents a field mapping from legacy to normalized schema."""
    
    legacy_field: str
    legacy_type: str
    legacy_column: str | None
    normalized_field: str
    normalized_type: str
    normalized_column: str
    transformation: str
    default_value: str | None = None
    validation: str | None = None
    constraints: list[str] | None = None


@dataclass
class EntityMapping:
    """Represents complete entity mapping from legacy to normalized."""
    
    entity_name: str
    legacy_class: str
    legacy_table: str | None
    normalized_table: str
    primary_key_transformation: str | None = None
    field_mappings: list[FieldMapping] | None = None


class FieldMappingExtractor:
    """Extracts field mappings from DTO classes and normalized schema."""
    
    def __init__(self):
        """Initialize the extractor."""
        pass
    
    def extract_dto_fields(self, java_content: str, class_name: str) -> list[dict[str, Any]]:
        """
        Extract all fields from a DTO class.
        
        Args:
            java_content: Java source code
            class_name: Name of the DTO class
            
        Returns:
            List of field dictionaries with name, type, and getter/setter info
        """
        fields = []
        
        # Find the class definition
        class_pattern = rf'class\s+{re.escape(class_name)}\s*[{{]'
        class_match = re.search(class_pattern, java_content)
        
        if not class_match:
            return fields
        
        # Extract fields (private fields with types)
        field_pattern = r'private\s+(\w+(?:<[^>]+>)?)\s+(\w+)\s*;'
        
        matches = re.finditer(field_pattern, java_content[class_match.start():])
        for match in matches:
            field_type = match.group(1)
            field_name = match.group(2)
            
            # Check for getter and setter
            has_getter = bool(re.search(rf'get{self._capitalize(field_name)}\s*\(', java_content))
            has_setter = bool(re.search(rf'set{self._capitalize(field_name)}\s*\(', java_content))
            
            fields.append({
                "name": field_name,
                "type": field_type,
                "java_type": field_type,
                "has_getter": has_getter,
                "has_setter": has_setter,
            })
        
        return fields
    
    def map_to_normalized_schema(
        self, 
        dto_fields: list[dict[str, Any]], 
        normalized_schema: str,
        entity_name: str
    ) -> list[FieldMapping]:
        """
        Map DTO fields to normalized schema columns.
        
        Args:
            dto_fields: List of DTO field dictionaries
            normalized_schema: Normalized schema SQL
            entity_name: Name of the entity (e.g., "subchapters")
            
        Returns:
            List of FieldMapping objects
        """
        mappings = []
        
        # Extract columns from normalized schema
        table_pattern = rf'CREATE TABLE[^{{]*{re.escape(entity_name)}[^{{]*\{{([^}}]+)}}'
        table_match = re.search(table_pattern, normalized_schema, re.IGNORECASE | re.DOTALL)
        
        if not table_match:
            return mappings
        
        table_def = table_match.group(1)
        
        # Extract column definitions
        column_pattern = r'(\w+)\s+(\w+(?:\([^)]+\))?)'
        schema_columns = {}
        for col_match in re.finditer(column_pattern, table_def):
            col_name = col_match.group(1)
            col_type = col_match.group(2)
            schema_columns[col_name] = col_type
        
        # Map DTO fields to schema columns
        for dto_field in dto_fields:
            field_name = dto_field["name"]
            field_type = dto_field["type"]
            
            # Try to find matching column (exact match or camelCase to snake_case)
            normalized_column = self._find_matching_column(field_name, schema_columns)
            
            if normalized_column:
                normalized_type = schema_columns[normalized_column]
                transformation = self._determine_transformation(
                    field_name, field_type, normalized_column, normalized_type
                )
            else:
                # New field in normalized schema
                normalized_column = self._camel_to_snake(field_name)
                normalized_type = "VARCHAR"  # Default
                transformation = "New field in normalized schema"
            
            mapping = FieldMapping(
                legacy_field=field_name,
                legacy_type=field_type,
                legacy_column=None,  # Would need to extract from legacy schema
                normalized_field=normalized_column,
                normalized_type=normalized_type,
                normalized_column=normalized_column,
                transformation=transformation,
                default_value="NULL",
            )
            
            mappings.append(mapping)
        
        return mappings
    
    def _find_matching_column(self, field_name: str, schema_columns: dict[str, str]) -> str | None:
        """Find matching column in schema for a DTO field."""
        # Try exact match
        if field_name in schema_columns:
            return field_name
        
        # Try camelCase to snake_case conversion
        snake_case = self._camel_to_snake(field_name)
        if snake_case in schema_columns:
            return snake_case
        
        # Try partial matches
        for col_name in schema_columns.keys():
            if field_name.lower() in col_name.lower() or col_name.lower() in field_name.lower():
                return col_name
        
        return None
    
    def _camel_to_snake(self, name: str) -> str:
        """Convert camelCase to snake_case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
    def _capitalize(self, name: str) -> str:
        """Capitalize first letter."""
        return name[0].upper() + name[1:] if name else name
    
    def _determine_transformation(
        self, 
        legacy_field: str, 
        legacy_type: str, 
        normalized_column: str, 
        normalized_type: str
    ) -> str:
        """Determine the transformation rule between legacy and normalized."""
        # Check for ID transformation
        if "id" in normalized_column.lower() and "String" in legacy_type:
            return "VARCHAR code → INTEGER ID via lookup"
        
        # Check for type changes
        if legacy_type != normalized_type:
            return f"{legacy_type} → {normalized_type}"
        
        # Direct mapping
        return "Direct mapping"
    
    def create_mapping_table(
        self, 
        entity_mapping: EntityMapping
    ) -> str:
        """
        Create a markdown table showing field mappings.
        
        Args:
            entity_mapping: EntityMapping object
            
        Returns:
            Markdown formatted table
        """
        if not entity_mapping.field_mappings:
            return ""
        
        table = f"### {entity_mapping.entity_name} Field Mapping\n\n"
        table += "| Legacy Field | Legacy Type | Legacy Column | Normalized Field | Normalized Type | Normalized Column | Transformation | Default |\n"
        table += "|--------------|------------|---------------|-----------------|----------------|------------------|----------------|----------|\n"
        
        for mapping in entity_mapping.field_mappings:
            table += f"| `{mapping.legacy_field}` | {mapping.legacy_type} | {mapping.legacy_column or 'N/A'} | `{mapping.normalized_field}` | {mapping.normalized_type} | `{mapping.normalized_column}` | {mapping.transformation} | {mapping.default_value or 'NULL'} |\n"
        
        return table
