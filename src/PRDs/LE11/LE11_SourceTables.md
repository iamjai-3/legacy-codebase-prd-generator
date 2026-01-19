# LE11 - ATA Chapter Alert Rate Management - Source Tables

## Database Schema

### Primary Tables

#### 1. `CHAPTER_ALERT_RATES`
Stores alert rate configurations for ATA chapters

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| FLEET | VARCHAR2(10) | PK, NOT NULL | Fleet identifier |
| CHAPTER | VARCHAR2(4) | PK, NOT NULL | ATA chapter code |
| REMOVAL_ALERT_RATE | NUMBER | | Alert threshold for part removals |
| SYSTEM_ALERT_RATE | NUMBER | | Alert threshold for system/defect reports |
| CLASSIFICATION | VARCHAR2(50) | | Classification of the alert |
| LAST_UPDATED | TIMESTAMP | | Timestamp of last update |
| UPDATED_BY | VARCHAR2(50) | | User who last updated the record |

#### 2. `FLEET_CHAPTER`
Maps chapters to fleets with fleet-specific configurations

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| FLEET | VARCHAR2(10) | PK, NOT NULL | Fleet identifier |
| CHAPTER | VARCHAR2(4) | PK, NOT NULL | ATA chapter code |
| PIREP_RATE_LIMIT | NUMBER | | PIREP rate limit for the fleet/chapter |
| REMOVAL_RATE_LIMIT | NUMBER | | Removal rate limit for the fleet/chapter |
| FIRST_AIRCRAFT_CODE | VARCHAR2(10) | | First aircraft code in the chain |
| NEXT_CHAPTER | VARCHAR2(4) | | Next chapter in sequence |
| FIRST_PART_NUMBER | VARCHAR2(50) | | First part number in the chapter |

### Supporting Tables

#### 1. `FLEET`
Master table for fleet information

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| FLEET_CODE | VARCHAR2(10) | PK | Unique fleet identifier |
| DESCRIPTION | VARCHAR2(100) | | Fleet description |
| ACTIVE | CHAR(1) | | Active status flag |

#### 2. `CHAPTERS`
Master table for ATA chapters

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| CHAPTER | VARCHAR2(4) | PK | ATA chapter code |
| DESCRIPTION | VARCHAR2(100) | | Chapter description |
| ACTIVE | CHAR(1) | | Active status flag |

## Table Relationships

1. **FLEET_CHAPTER to FLEET**
   - One-to-many relationship (one fleet can have many chapter configurations)
   - Foreign Key: `FLEET_CHAPTER.FLEET` → `FLEET.FLEET_CODE`

2. **FLEET_CHAPTER to CHAPTERS**
   - One-to-many relationship (one chapter can be assigned to many fleets)
   - Foreign Key: `FLEET_CHAPTER.CHAPTER` → `CHAPTERS.CHAPTER`

3. **CHAPTER_ALERT_RATES to FLEET_CHAPTER**
   - One-to-one relationship (each fleet/chapter combination has one set of alert rates)
   - Foreign Key: `(CHAPTER_ALERT_RATES.FLEET, CHAPTER_ALERT_RATES.CHAPTER)` → `(FLEET_CHAPTER.FLEET, FLEET_CHAPTER.CHAPTER)`

## Stored Procedures

### 1. `graphical_reports_pkg.getChapterAlertRates`
Retrieves alert rates for a specific fleet

**Parameters:**
- `p_fleet` - Fleet code to retrieve alert rates for

**Returns:**
Cursor containing alert rate information for the specified fleet

## Data Flow

1. **Configuration Flow**
   - User selects a fleet in the LE11 interface
   - System loads existing alert rate configurations for the fleet
   - User modifies alert thresholds as needed
   - Changes are saved to the `CHAPTER_ALERT_RATES` table

2. **Alert Generation Flow**
   - System monitors PIREPs and removal data
   - Compares rates against configured thresholds
   - Generates alerts when thresholds are exceeded

## Data Validation Rules

1. Alert rates must be positive numbers
2. Fleet and chapter combinations must exist in the `FLEET_CHAPTER` table
3. Only authorized users can modify alert rate configurations
4. Historical alert data is maintained for auditing purposes

## Migration Considerations

1. **Data Migration**
   - Existing alert rate configurations must be migrated from the legacy system
   - Data mapping between legacy and new schemas required
   - Validation of migrated data against business rules

2. **Performance**
   - Indexes should be created on frequently queried columns
   - Consider partitioning large tables by fleet for better performance
   - Implement caching for frequently accessed alert rate configurations

3. **Data Integrity**
   - Implement referential integrity constraints
   - Set up cascading deletes where appropriate
   - Implement database triggers for audit logging
