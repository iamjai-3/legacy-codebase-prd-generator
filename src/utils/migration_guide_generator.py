"""
Migration Guide Generator for Legacy to Normalized Schema Migration.

Generates step-by-step migration guides with field mappings and transformation rules.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class MigrationStep:
    """Represents a single migration step."""
    
    step_number: int
    title: str
    description: str
    actions: list[str]
    validation: str | None = None
    rollback: str | None = None


@dataclass
class MigrationGuide:
    """Complete migration guide for an entity."""
    
    entity_name: str
    complexity: str  # LOW, MEDIUM, HIGH
    estimated_time: str
    prerequisites: list[str]
    steps: list[MigrationStep]
    validation_checklist: list[str]
    rollback_procedures: list[str]


class MigrationGuideGenerator:
    """Generates migration guides for legacy to normalized schema migration."""
    
    def __init__(self):
        """Initialize the generator."""
        pass
    
    def generate_migration_guide(
        self,
        entity_name: str,
        legacy_table: str | None,
        normalized_table: str,
        field_mappings: list[dict[str, Any]],
        primary_key_transformation: str | None = None,
    ) -> MigrationGuide:
        """
        Generate a complete migration guide.
        
        Args:
            entity_name: Name of the entity
            legacy_table: Legacy table name (if applicable)
            normalized_table: Normalized table name
            field_mappings: List of field mapping dictionaries
            primary_key_transformation: Description of PK transformation
            
        Returns:
            MigrationGuide object
        """
        # Assess complexity
        complexity = self._assess_complexity(field_mappings, primary_key_transformation)
        
        # Generate steps
        steps = self._generate_migration_steps(
            entity_name, legacy_table, normalized_table, field_mappings, primary_key_transformation
        )
        
        # Generate validation checklist
        validation_checklist = self._generate_validation_checklist(
            entity_name, field_mappings, primary_key_transformation
        )
        
        # Generate rollback procedures
        rollback_procedures = self._generate_rollback_procedures(
            entity_name, legacy_table, normalized_table
        )
        
        return MigrationGuide(
            entity_name=entity_name,
            complexity=complexity,
            estimated_time=self._estimate_time(complexity, len(field_mappings)),
            prerequisites=self._generate_prerequisites(normalized_table),
            steps=steps,
            validation_checklist=validation_checklist,
            rollback_procedures=rollback_procedures,
        )
    
    def _assess_complexity(
        self, 
        field_mappings: list[dict[str, Any]], 
        primary_key_transformation: str | None
    ) -> str:
        """Assess migration complexity."""
        has_pk_transformation = primary_key_transformation is not None
        has_lookups = any("lookup" in m.get("transformation", "").lower() for m in field_mappings)
        has_new_fields = any("new field" in m.get("transformation", "").lower() for m in field_mappings)
        has_type_changes = any(
            m.get("legacy_type") != m.get("normalized_type") 
            for m in field_mappings 
            if m.get("legacy_type") and m.get("normalized_type")
        )
        
        score = 0
        if has_pk_transformation:
            score += 3
        if has_lookups:
            score += 2
        if has_new_fields:
            score += 1
        if has_type_changes:
            score += 1
        
        if score >= 5:
            return "HIGH"
        elif score >= 2:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _generate_migration_steps(
        self,
        entity_name: str,
        legacy_table: str | None,
        normalized_table: str,
        field_mappings: list[dict[str, Any]],
        primary_key_transformation: str | None,
    ) -> list[MigrationStep]:
        """Generate migration steps."""
        steps = []
        
        # Step 1: Preparation
        steps.append(MigrationStep(
            step_number=1,
            title="Preparation and Analysis",
            description="Analyze legacy data and prepare migration scripts",
            actions=[
                "Review legacy table structure and data",
                "Identify all fields to be migrated",
                "Document data quality issues",
                "Create backup of legacy data",
            ],
            validation="Verify backup is complete and accessible",
        ))
        
        # Step 2: Schema Creation (if needed)
        if normalized_table:
            steps.append(MigrationStep(
                step_number=2,
                title="Create Normalized Schema",
                description="Ensure normalized table exists with correct structure",
                actions=[
                    f"Verify {normalized_table} table exists",
                    "Check all columns are present",
                    "Verify foreign key constraints",
                    "Create indexes if needed",
                ],
                validation=f"Run: SELECT * FROM {normalized_table} LIMIT 0 (should not error)",
            ))
        
        # Step 3: Key Transformation (if needed)
        if primary_key_transformation:
            steps.append(MigrationStep(
                step_number=3,
                title="Primary Key Transformation",
                description=primary_key_transformation,
                actions=[
                    "Create lookup mapping table (legacy_key → normalized_id)",
                    "Populate lookup table from legacy data",
                    "Verify all legacy keys have corresponding IDs",
                ],
                validation="Check for orphaned records (legacy keys without IDs)",
            ))
        
        # Step 4: Data Migration
        steps.append(MigrationStep(
            step_number=4,
            title="Data Migration",
            description="Migrate data from legacy to normalized schema",
            actions=self._generate_migration_actions(field_mappings, primary_key_transformation),
            validation="Row count matches between legacy and normalized",
        ))
        
        # Step 5: Validation
        steps.append(MigrationStep(
            step_number=5,
            title="Data Validation",
            description="Validate migrated data integrity",
            actions=[
                "Compare row counts",
                "Validate foreign key relationships",
                "Check for data type mismatches",
                "Verify business rules are maintained",
            ],
            validation="All validation checks pass",
        ))
        
        return steps
    
    def _generate_migration_actions(
        self,
        field_mappings: list[dict[str, Any]],
        primary_key_transformation: str | None,
    ) -> list[str]:
        """Generate specific migration actions based on field mappings."""
        actions = []
        
        for mapping in field_mappings:
            transformation = mapping.get("transformation", "")
            legacy_field = mapping.get("legacy_field", "")
            normalized_field = mapping.get("normalized_field", "")
            
            if "lookup" in transformation.lower():
                actions.append(
                    f"Map {legacy_field} to {normalized_field} using lookup table"
                )
            elif "new field" in transformation.lower():
                actions.append(
                    f"Set {normalized_field} to default value (new field in normalized schema)"
                )
            elif "direct mapping" in transformation.lower():
                actions.append(
                    f"Copy {legacy_field} directly to {normalized_field}"
                )
            else:
                actions.append(
                    f"Transform {legacy_field} to {normalized_field}: {transformation}"
                )
        
        return actions
    
    def _generate_validation_checklist(
        self,
        entity_name: str,
        field_mappings: list[dict[str, Any]],
        primary_key_transformation: str | None,
    ) -> list[str]:
        """Generate validation checklist."""
        checklist = [
            f"All {entity_name} records migrated successfully",
            "Row counts match between legacy and normalized",
            "No data loss during migration",
            "Foreign key constraints are satisfied",
        ]
        
        if primary_key_transformation:
            checklist.append("Primary key transformation completed correctly")
            checklist.append("No orphaned records in lookup tables")
        
        # Add field-specific validations
        for mapping in field_mappings:
            if mapping.get("validation"):
                checklist.append(
                    f"{mapping.get('normalized_field')}: {mapping.get('validation')}"
                )
        
        return checklist
    
    def _generate_rollback_procedures(
        self,
        entity_name: str,
        legacy_table: str | None,
        normalized_table: str,
    ) -> list[str]:
        """Generate rollback procedures."""
        procedures = [
            f"Stop all writes to {normalized_table} table",
            f"Restore {normalized_table} from backup (if backup was taken)",
            f"Or truncate {normalized_table} if migration needs to be restarted",
            "Verify legacy system is still functional",
            "Document rollback reason and issues encountered",
        ]
        
        return procedures
    
    def _generate_prerequisites(self, normalized_table: str) -> list[str]:
        """Generate prerequisites for migration."""
        return [
            f"{normalized_table} table created in target database",
            "All foreign key reference tables exist and are populated",
            "Backup of legacy data completed",
            "Migration scripts tested in development environment",
            "Rollback plan documented and tested",
        ]
    
    def _estimate_time(self, complexity: str, field_count: int) -> str:
        """Estimate migration time."""
        base_time = {
            "LOW": 2,
            "MEDIUM": 4,
            "HIGH": 8,
        }
        
        hours = base_time.get(complexity, 4)
        hours += field_count * 0.5  # Add time per field
        
        if hours < 4:
            return f"{int(hours)} hours"
        elif hours < 8:
            return f"{int(hours)} hours (1 day)"
        else:
            return f"{int(hours)} hours ({int(hours/8)} days)"
    
    def format_migration_guide(self, guide: MigrationGuide) -> str:
        """Format migration guide as markdown."""
        md = f"""# Migration Guide: {guide.entity_name}

**Complexity:** {guide.complexity}  
**Estimated Time:** {guide.estimated_time}

## Prerequisites

{chr(10).join([f"- {p}" for p in guide.prerequisites])}

## Migration Steps

"""
        
        for step in guide.steps:
            md += f"""### Step {step.step_number}: {step.title}

**Description:** {step.description}

**Actions:**
{chr(10).join([f"1. {a}" for a in step.actions])}

"""
            if step.validation:
                md += f"**Validation:** {step.validation}\n\n"
            if step.rollback:
                md += f"**Rollback:** {step.rollback}\n\n"
        
        md += f"""## Validation Checklist

{chr(10).join([f"- [ ] {item}" for item in guide.validation_checklist])}

## Rollback Procedures

{chr(10).join([f"1. {proc}" for proc in guide.rollback_procedures])}
"""
        
        return md
