# ATA Chapter Codes (LE07) - Source Tables Analysis Results

## Identified Source Oracle Tables

Based on comprehensive source code analysis of the COBOL application, Java desktop application, and microservices, the following Oracle database tables are used by the ATA Chapter Codes (LE07) feature:

### Primary Tables

| Table Name | Description | Primary Purpose | Key Evidence |
|------------|-------------|-----------------|---------------|
| `CHAPTERS` | Main ATA chapter definitions | Stores basic chapter code and description information | Referenced directly in the microservices codebase (`ChaptersRepo.java`) and COBOL code |
| `SUBCHAPTERS` | Sub-chapter definitions | Stores sub-chapter information linked to main chapters | Referenced in the microservices codebase (`SubchaptersRepo.java`) |
| `CHAPTER_ALERT_RATES` | Alert rate configurations | Stores alert rate settings for each chapter code | Referenced in `ChapterAlertRates.java` and via stored procedure calls |
| `FLEET_CHAPTER` | Fleet-specific chapter configurations | Links chapters to specific fleets and stores fleet-specific settings | Referenced in the microservices as `FLEET_CHAPTER` table and in COBOL as 'FLEET/CHAP' key prefix |
| `FLEET_CHAPTER_PART_AIRCRAFT` | Fleet-specific part tracking | Tracks removals by fleet, chapter, part and aircraft | Used for tracking removal counts in reliability reporting |

### Table Relationships

The analysis revealed the following relationships between the tables:

1. **One-to-Many**: `CHAPTERS` to `SUBCHAPTERS`
   - Each main chapter can have multiple subchapters
   - Referenced in the code through joined queries and object relationships

2. **One-to-Many**: `CHAPTERS` to `FLEET_CHAPTERS`
   - Each chapter can be associated with multiple fleets
   - Fleet-specific configurations are stored in this relationship

## Data Structure Details

### CHAPTERS Table

```
Key columns:
- CHAPTER (PK): VARCHAR2(3) - The chapter code (e.g., "21")
- LEBDES: VARCHAR2(25) - Chapter description
- LEBNCH: VARCHAR2(3) - Next chapter in chain
```

Evidence: The COBOL code in `LAZRRD.CBL` and other modules directly references these fields when reading chapter records.

### SUBCHAPTERS Table

```
Key columns:
- FLEET: VARCHAR2 - Associated fleet code
- CHAPTER: VARCHAR2 - Associated chapter code
- SUBCHAPTER: VARCHAR2 - Subchapter identifier (1-2 characters)
```

Evidence: The `SubchaptersRepo.java` class in the microservices codebase shows these key fields when querying subchapters.

### CHAPTER_ALERT_RATES Table

```
Key columns:
- CHAPTER: VARCHAR2 - Chapter code
- REMOVAL_ALERT_RATE: NUMBER - Alert rate for removals
- SYSTEM_ALERT_RATE: NUMBER - System-level alert rate
- CLASSIFICATION: VARCHAR2 - Chapter classification
```

Evidence: Referenced in `ChapterAlertRates.java` in the Java application.

### FLEET_CHAPTER Table

```
Key columns:
- FLEET: CHARACTER(1) NOT NULL - Fleet code
- CHAPTER: CHARACTER(3) NOT NULL - Chapter code
- PIREP_RATE_LIMIT: DOUBLE PRECISION - Pirep rate limit
- REMOVAL_RATE_LIMIT: DOUBLE PRECISION - Removal rate limit
- FIRST_AIRCRAFT_CODE: CHARACTER(2) - First aircraft code in chain
- NEXT_CHAPTER: CHARACTER(3) - Next chapter in chain
- FIRST_PART_NUMBER: CHARACTER(19) - First part number
```

Evidence: The exact table structure matches the one provided and is referenced directly in the `FleetChapterRepo.java` class with matching column names. In the COBOL code, modules like `LAZRR9.CBL`, `LAZRW7.CBL`, `LAZRU7.CBL`, and `LAZRX6.CBL` operate on this table using the key prefix 'FLEET/CHAP'.

### FLEET_CHAPTER_PART_AIRCRAFT Table

```
Key columns:
- FLEET: CHARACTER(1) NOT NULL - Fleet code
- CHAPTER: CHARACTER(3) NOT NULL - Chapter code
- PART_NUMBER: CHARACTER(19) NOT NULL - Part number
- AIRCRAFT_CODE: CHARACTER(2) NOT NULL - Aircraft code
- Various REMOVAL_COUNT_n fields for tracking removals
```

Evidence: Referenced in removal tracking code and reliability reporting. This is used for more detailed tracking than just the chapter-level information.

## SQL Operations

The following SQL operations are performed on these tables:

### SELECT Operations

```sql
-- Basic chapter retrieval
SELECT * FROM CHAPTERS WHERE CHAPTER = ?

-- Fleet-specific chapter retrieval
SELECT * FROM FLEET_CHAPTER 
WHERE FLEET = ? AND CHAPTER = ?

-- Subchapter retrieval 
SELECT * FROM SUBCHAPTERS
WHERE FLEET = ? AND CHAPTER = ?

-- Alert rates retrieval
-- (Called via stored procedure)
CALL graphical_reports_pkg.getChapterAlertRates(?)
```

### INSERT/UPDATE Operations

```sql
-- Create new chapter
INSERT INTO CHAPTERS (CHAPTER, LEBDES) VALUES (?, ?)

-- Update chapter
UPDATE CHAPTERS SET LEBDES = ? WHERE CHAPTER = ?

-- Create fleet-specific chapter
INSERT INTO FLEET_CHAPTER (FLEET, CHAPTER, PIREP_RATE_LIMIT, REMOVAL_RATE_LIMIT, 
                          FIRST_AIRCRAFT_CODE, NEXT_CHAPTER, FIRST_PART_NUMBER) 
VALUES (?, ?, ?, ?, ?, ?, ?)

-- Update fleet-specific chapter
UPDATE FLEET_CHAPTER 
SET PIREP_RATE_LIMIT = ?, REMOVAL_RATE_LIMIT = ?, 
    FIRST_AIRCRAFT_CODE = ?, NEXT_CHAPTER = ?, FIRST_PART_NUMBER = ? 
WHERE FLEET = ? AND CHAPTER = ?

-- Create subchapter
INSERT INTO SUBCHAPTERS (FLEET, CHAPTER, SUBCHAPTER) VALUES (?, ?, ?)
```

### DELETE Operations

```sql
-- Delete dummy chapter
DELETE FROM CHAPTERS WHERE CHAPTER = ? AND LEBNCH = '***'

-- Delete subchapter
DELETE FROM SUBCHAPTERS WHERE FLEET = ? AND CHAPTER = ? AND SUBCHAPTER = ?
```

## Data Flow

Based on the code analysis, the typical data flow for ATA chapter operations is:

1. **Creation of a new chapter**
   - User enters chapter code and description
   - System validates the input
   - New record is created in CHAPTERS
   - If applicable, fleet-specific records are created in FLEET_CHAPTERS

2. **Adding a sub-chapter**
   - User selects a chapter and enters subchapter
   - System validates the input and fleet applicability
   - New record is created in SUBCHAPTERS

3. **Configuring fleet exclusions**
   - User selects a chapter/subchapter combination
   - User specifies fleet exclusions
   - System updates FLEET_CHAPTERS to reflect exclusions

## Validation Rules

The following validation rules were identified in the code:

1. Chapter codes are typically 2-3 characters
2. Subchapter codes were upgraded from 1 to 2 characters (referenced in `LAZRA4.CBL`)
3. Fleet-specific validations ensure subchapters are applicable to the current fleet

## Normalization Considerations

The current Oracle schema has some normalization issues:

1. Some data duplication exists between tables
2. Fleet-specific configurations are not fully normalized
3. There appears to be a mix of data storage approaches (tables vs. stored procedures)

These considerations will be important when mapping to the normalized PostgreSQL schema.

## Note on Fleet_Chap_Part Tables

The `FLEET_CHAP_PART_HEADER_1`, `FLEET_CHAP_PART_HEADER_2` and `FLEET_CHAP_PART_HEADER_3` tables are not directly used by the core ATA Chapter Codes management feature. These tables appear to be used for related functionality around part tracking and reliability reporting, but they are not integral to the basic chapter/subchapter management functions.

These tables use a different access pattern and are primarily accessed through specialized reporting functions rather than through the direct chapter code management interfaces.

## Conclusion

The ATA Chapter Codes feature primarily relies on the following Oracle tables:

1. `CHAPTERS` - Core chapter definitions
2. `SUBCHAPTERS` - Subchapter management
3. `CHAPTER_ALERT_RATES` - Alert rate configurations
4. `FLEET_CHAPTER` - Fleet-specific chapter configurations
5. `FLEET_CHAPTER_PART_AIRCRAFT` - Used for removal tracking in reliability functions

These tables store the core data for chapter and subchapter management, including fleet-specific configurations and alert rates. The more specialized `FLEET_CHAP_PART_HEADER_*` tables are used for extended functionality but are not central to the basic ATA chapter codes management.

When implementing the PostgreSQL data access layer, these tables will need to be mapped to the corresponding normalized tables in the new schema, with appropriate consideration for data types, constraints, and relationships.
