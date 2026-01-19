# LE11 Source Tables Analysis

## Objective
Analyze the legacy codebase to identify all database tables used by the LE11 feature in the CAMO domain. This analysis will help in understanding the data model and planning the migration to the new Lumina platform.

## Analysis Scope

### 1. Codebase Analysis
- Search for SQL queries, stored procedures, and data access code related to LE11 in:
  - COBOL programs (oases-cobol directory)
  - Java code (oases and microservices directories)
  - Configuration files
  - Data access layers

### 2. Database Objects to Identify
- Primary tables used by the feature
- Lookup/reference tables
- Views and materialized views
- Stored procedures and functions
- Triggers and constraints
- Sequences and indexes

### 3. Relationships and Dependencies
- Primary and foreign key relationships
- Data flow between tables
- Dependencies on other features or modules

## Expected Output
Create a file named `LE11_SourceTables.md` with the following sections:

1. **Primary Tables**
   - Table name
   - Purpose/description
   - Key columns and data types
   - Estimated row count (if available)

2. **Reference Tables**
   - Table name
   - Purpose/description
   - Relationship to primary tables

3. **Data Model**
   - ER diagram (if possible)
   - Description of key relationships
   - Any data quality observations

4. **Special Considerations**
   - Performance-sensitive queries
   - Complex business logic in database
   - Known data quality issues
   - Integration points with other systems
