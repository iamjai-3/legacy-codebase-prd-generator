# ATA Chapter Codes (LE07) - Source Tables Analysis Prompt

## Objective
Conduct a thorough analysis of the legacy COBOL, Java desktop application, and microservices code to identify **all** Oracle database tables used by the ATA Chapter Codes (LE07) feature. The identified tables will form the basis for mapping to the normalized PostgreSQL schema.

## Feature Overview
LE07 allows users to set up, amend, and manage ATA (Air Transport Association) Chapter Codes and their sub-chapters, which are industry-standard codes used for categorizing aircraft systems and components.

### Key Functionality to Guide Analysis

#### Creation and Management of ATA Chapters
- Set up new chapter codes
- Customize existing chapter codes
- Delete chapter codes (including functionality to delete dummy chapter headers)

#### Sub-chapter Management
- Supports 2-character sub-chapters (upgraded from earlier versions)
- Allows sub-chapters to be defined at both system and fleet levels
- Provides validation of sub-chapter codes

#### Fleet-Specific Configuration
- Allows chapters/sub-chapters to be associated with specific fleet types
- Supports fleet-level exclusions (excluding specific sub-chapters from certain fleets)
- Enables validation that sub-chapters are applicable to the current fleet

## Source Code Locations to Analyze

### COBOL Application (oases-cobol)
- Search for program files related to ATA chapter management
- Look for data sections that define record structures related to chapters
- Identify any SQL statements or file operations for chapter data

### Java Desktop Application (oases)
- Search for classes and packages related to ATA chapters
- Look for DAO (Data Access Object) classes
- Examine SQL queries and stored procedure calls

### Microservices
- Identify any microservices related to chapter code management
- Examine API endpoints that might be manipulating chapter data
- Look for database interaction code

## What to Look For

### SQL Statements
Look for SQL statements that reference table names, particularly:
- SELECT statements revealing which tables store ATA chapter data
- INSERT, UPDATE, or DELETE operations on chapter-related tables
- JOIN operations showing relationships between tables

### Code Patterns
Search for code patterns that might indicate database table usage:
- Variable names containing "chapter", "ata", "subchapter", or "fleet"
- Record definitions or DTOs (Data Transfer Objects) representing tables
- Data mapping code between database and application objects

### Database Operations
Analyze how data is manipulated:
- How are new chapters created and stored?
- How are relationships between chapters and sub-chapters maintained?
- How are fleet-specific exclusions implemented?
- What validation rules are applied before database operations?

## Specific Tables to Investigate
Based on initial analysis, the following tables may be relevant (verify through code analysis):

- `CHAPTERS` - Possibly stores the main ATA chapter code definitions
- `CHAPTER_ALERT_RATES` - May contain alert rate configurations for chapter codes
- Tables related to sub-chapters (naming might vary)
- Tables related to fleet-specific configurations

## Expected Output
The final output should include:

1. **Confirmed Source Tables List**  
   A comprehensive list of all Oracle tables used by the LE07 feature, including:
   - Table name
   - Primary purpose
   - Key columns
   - Relationships with other tables

2. **Data Flow Diagrams**  
   Diagrams showing how data moves between tables during key operations:
   - Creating a new chapter
   - Adding a sub-chapter
   - Configuring fleet exclusions

3. **SQL Evidence**  
   Examples of actual SQL statements found in the code that confirm table usage.

4. **Structural Insights**  
   Observations about the data structure that will inform PostgreSQL mapping:
   - Normalization issues in the original schema
   - Validation rules enforced at the database level
   - Indexing and performance considerations

## Analysis Methodology

1. **Keyword Search**  
   Start with keyword searches in the codebase for:
   - "ATA" or "chapter" in combination with SQL keywords
   - Table names from the Oracle schema (referenced in `docs/database/SourceOracleTables.md`)
   - Function or procedure names related to chapter management

2. **Call Hierarchy Analysis**  
   For any identified entry points:
   - Trace the call hierarchy to find database interaction code
   - Follow data objects through the application flow

3. **UI to Database Mapping**  
   Using the provided screenshots:
   - Map UI fields to potential database columns
   - Trace how user inputs are transformed into database operations

4. **Cross-Reference Analysis**  
   Look for references to the ATA chapter feature from other modules:
   - How do other parts of the system query or use chapter data?
   - Are there any triggers or cascade operations?

## Coding Standards and Patterns to Consider

### COBOL Patterns
- Record structures defined in the DATA DIVISION
- File operations using READ, WRITE, REWRITE
- EXEC SQL blocks for database operations

### Java Patterns
- JPA annotations indicating entity mappings
- JDBC code with explicit SQL statements
- DAO pattern implementations
- Service layer code that manipulates data

### Microservice Patterns
- Repository pattern implementations
- ORM configurations
- API endpoints that reveal data structure

## Reference Materials
- Oracle Database Schema: `docs/database/SourceOracleTables.md`
- Target PostgreSQL Schema: `docs/database/lumina.sql`
- LE07 Feature Description: `docs/PRDs/CAMO/LE07/LE07.md`

NOTE: output the list of source tables into another document next to this one called LE07_SourceTables.md.