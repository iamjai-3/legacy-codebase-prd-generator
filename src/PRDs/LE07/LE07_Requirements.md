# ATA Chapter Codes Management (LE07) - Requirements Specification

## Executive Summary

The ATA Chapter Codes Management feature (LE07) provides a robust system for creating, managing, and configuring ATA (Air Transport Association) Chapter Codes and their sub-chapters. These industry-standard codes are critical for categorizing aircraft systems and components throughout the Lumina platform. This document details the requirements for implementing this feature in the Lumina .NET/Angular platform, ensuring a modern, user-friendly experience while maintaining all functional capabilities of the legacy system.

## Functional Requirements

### 1. Chapter Management

#### 1.1 Chapter Creation
- **FR1.1.1:** Users shall be able to create new chapter codes through a dedicated "New Chapter" interface
- **FR1.1.2:** Chapter codes shall be configurable as 2-digit numeric identifiers (00-99)
- **FR1.1.3:** Each chapter must support a descriptive text field of at least 50 characters
- **FR1.1.4:** The system shall validate chapter codes to prevent duplicates

#### 1.2 Chapter Modification
- **FR1.2.1:** Users shall be able to modify existing chapter descriptions
- **FR1.2.2:** The system shall support changing alert configuration parameters for chapters
- **FR1.2.3:** Chapter modifications shall be tracked with timestamp and user information

#### 1.3 Chapter Deletion
- **FR1.3.1:** Users shall be able to delete chapter codes if they are not referenced elsewhere in the system
- **FR1.3.2:** The system shall provide warnings before deletion if chapters are in use
- **FR1.3.3:** Support deletion of dummy chapter headers as per legacy functionality

### 2. Sub-chapter Management

#### 2.1 Sub-chapter Creation
- **FR2.1.1:** Users shall be able to create sub-chapters associated with specific chapters
- **FR2.1.2:** Sub-chapter codes shall be configurable as 2-character alphanumeric identifiers
- **FR2.1.3:** Each sub-chapter must support a descriptive text field of at least 50 characters
- **FR2.1.4:** The system shall validate sub-chapter codes to prevent duplicates within a chapter

#### 2.2 Sub-chapter Configuration
- **FR2.2.1:** Sub-chapters shall be configurable at both system-wide and fleet-specific levels
- **FR2.2.2:** Users shall be able to set alert limits for sub-chapters (in landings and days)
- **FR2.2.3:** The system shall support ETOPS configuration for applicable sub-chapters

### 3. Fleet-Specific Configuration

#### 3.1 Fleet Association
- **FR3.1.1:** Users shall be able to associate chapters/sub-chapters with specific fleet types
- **FR3.1.2:** The system shall provide a fleet selection interface from existing fleet codes
- **FR3.1.3:** Fleet-specific configurations shall override system-wide defaults when applicable

#### 3.2 Fleet Exclusions
- **FR3.2.1:** Users shall be able to exclude specific sub-chapters from certain fleets
- **FR3.2.2:** The system shall provide an "Exclude from fleet" option for each chapter/sub-chapter
- **FR3.2.3:** Users shall be able to view and manage all exclusions for a given fleet

#### 3.3 Fleet Validation
- **FR3.3.1:** The system shall validate that sub-chapters are applicable to the current fleet
- **FR3.3.2:** Error messages shall be displayed when attempting to use excluded sub-chapters

### 4. Alert Configuration

#### 4.1 Alert Parameters
- **FR4.1.1:** Users shall be able to configure alert limits in landings
- **FR4.1.2:** Users shall be able to configure alert limits in days
- **FR4.1.3:** Alert configurations shall be configurable at chapter and sub-chapter levels

#### 4.2 ETOPS Configuration
- **FR4.2.1:** The system shall support ETOPS (Extended Twin Operations) configuration
- **FR4.2.2:** ETOPS settings shall be configurable for applicable chapters/sub-chapters

## Data Model

### 1. Entity Relationships

#### 1.1 Core Entities
- **Chapter**: Represents an ATA chapter code with its metadata
- **Subchapter**: Represents a sub-chapter within an ATA chapter with fleet-specific configurations
- **Fleet**: Represents an aircraft fleet type with detailed maintenance parameters
- **FleetChapter**: Maps the relationship between fleets and chapters with rate limits
- **ChapterAlertRate**: Stores alert configuration for chapters per fleet

#### 1.2 Entity Relationships Diagram
```
Chapter (1) -----< (many) Subchapter
Chapter (1) -----< (many) FleetChapter
Fleet (1) -----< (many) FleetChapter
Fleet (1) -----< (many) Subchapter
Chapter (1) -----< (many) ChapterAlertRate
```

#### 1.3 Special Relationships
- Chapters can reference other chapters via next_chapter_id (self-referencing)
- Fleets can reference other fleets via next_fleet (linear list structure)
- FleetChapter includes direct aircraft reference via first_aircraft_code

### 2. Database Schema Details

#### 2.1 Chapter Table
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| chapter_id | INTEGER | PK, NOT NULL, AUTO_INCREMENT | Unique chapter identifier |
| chapter_description | CHARACTER(25) | | Chapter description |
| next_chapter_id | INTEGER | FK (self-reference) | Reference to the next chapter in sequence |
| dbt_updated_at | TIMESTAMP | | DBT update timestamp |
| dbt_invocation_id | VARCHAR(50) | | DBT invocation identifier |

#### 2.2 Subchapter Table
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| subchapter_id | INTEGER | PK, NOT NULL, AUTO_INCREMENT | Unique identifier |
| fleet_code | VARCHAR | FK, NULL | Reference to fleet |
| chapter_id | INTEGER | FK, NULL | Reference to parent chapter |
| subchapter | VARCHAR | | Subchapter code |
| description | VARCHAR | | Subchapter description |
| alert_limit_landings | INTEGER | | Alert threshold in landings |
| alert_limit_days | INTEGER | | Alert threshold in days |
| exclusion_flag | VARCHAR | | Flag for exclusions |
| etops | VARCHAR | | ETOPS configuration flag |
| dbt_updated_at | TIMESTAMP | | DBT update timestamp |
| dbt_invocation_id | VARCHAR(50) | | DBT invocation identifier |

#### 2.3 Fleet Table
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| fleet_code | VARCHAR | PK, NOT NULL | Unique fleet identifier |
| fleet_description | VARCHAR | | Fleet description |
| first_aircraft_code | VARCHAR | FK | Reference to first aircraft |
| first_chapter | VARCHAR | | Reference to first chapter |
| next_fleet | VARCHAR | | Reference to next fleet |
| period_0_time | INTEGER | | Period 0 time |
| period_0_landings | INTEGER | | Period 0 landings |
| period_0_aircraft | INTEGER | | Period 0 aircraft |
| period_1_time | INTEGER | | Period 1 time |
| period_1_landings | INTEGER | | Period 1 landings |
| period_1_aircraft | INTEGER | | Period 1 aircraft |
| period_2_time | INTEGER | | Period 2 time |
| period_2_landings | INTEGER | | Period 2 landings |
| period_2_aircraft | INTEGER | | Period 2 aircraft |
| engine_part_number | VARCHAR | | Engine part number |
| total_engines | INTEGER | | Total number of engines |
| oil_alert_level | DOUBLE PRECISION | | Oil alert level |
| delta_tit_alert | CHARACTER(2) | | Delta TIT alert |
| percent_engine_effic | CHARACTER(3) | | Engine efficiency percentage |
| access_authority | VARCHAR | | Access authority |
| date_of_last_month_end | TIMESTAMP | | Date of last month end |
| record_derate_data | CHARACTER(1) | | Record derate data flag |
| mel_revision_number | VARCHAR | | MEL revision number |
| current_fleet_indicator | VARCHAR | | Current fleet indicator |
| interval_type | VARCHAR | | Interval type |
| mro_approval_number | VARCHAR | | MRO approval number |
| variation_control_on_due | VARCHAR | | Variation control on due |
| weight_uom | VARCHAR | | Weight UOM |
| centre_of_gravity_uom | VARCHAR | | Centre of gravity UOM |
| current_year_month | VARCHAR | | Current year month |
| dbt_updated_at | TIMESTAMP | | DBT update timestamp |
| dbt_invocation_id | VARCHAR(50) | | DBT invocation identifier |

#### 2.4 FleetChapter Table
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| fleet_chapters_id | INTEGER | PK, NOT NULL, AUTO_INCREMENT | Unique identifier |
| fleet_code | VARCHAR | FK, NULL | Reference to fleet |
| chapter_id | INTEGER | FK, NULL | Reference to chapter |
| pirep_rate_limit | NUMERIC(4,1) | | PIREP rate limit |
| removal_rate_limit | NUMERIC(4,1) | | Removal rate limit |
| first_aircraft_code | VARCHAR | FK | Reference to first aircraft |
| next_chapter | VARCHAR | | Reference to next chapter |
| first_part_number | VARCHAR | | First part number |
| dbt_updated_at | TIMESTAMP | | DBT update timestamp |
| dbt_invocation_id | VARCHAR(50) | | DBT invocation identifier |

#### 2.5 ChapterAlertRate Table
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| alert_rate_id | INTEGER | PK, NOT NULL, AUTO_INCREMENT | Unique identifier |
| chapter_id | INTEGER | FK, NULL | Reference to chapter |
| fleet | VARCHAR(1) | | Fleet code character |
| alert_rate_value | NUMERIC(5,2) | | Alert rate value |
| dbt_updated_at | TIMESTAMP | | DBT update timestamp |
| dbt_invocation_id | VARCHAR(50) | | DBT invocation identifier |

## Technical Architecture

### 1. System Components

#### 1.1 Data Access Layer (Lumina.Data)
- Entity Framework Core models for all database entities
- Repository interfaces and implementations for data access
- DbContext configuration for PostgreSQL with proper schema mapping
- Dynamic table and column name detection for resilience
- Fallback mechanisms for handling schema variations

#### 1.2 Business Logic Layer (Lumina.CAMO)
- Models defined in Core project to prevent circular dependencies
- Extension methods for model conversion
- Service interfaces and implementations with fully-qualified type names
- Validation services with explicit null handling
- Integration with other modules (reliability reporting, etc.)
- DTOs for data transfer between layers

#### 1.3 API Layer (Lumina.API)
- RESTful controllers for all CRUD operations
- Authentication and authorization middleware
- Input validation and error handling with validation middleware
- Swagger/OpenAPI documentation
- Performance metrics and structured logging

#### 1.4 Frontend Application (Lumina.Web)
- Angular components for chapter and subchapter management
- Reactive forms with client-side validation
- State management for complex interactions
- Responsive UI with Angular Material components
- Error handling with user-friendly messages

### 2. Component Interaction Diagram

```
User Interface (Angular)
       ↑↓
RESTful API Controllers
       ↑↓
Business Services
       ↑↓
Repository Layer
       ↑↓
Database (PostgreSQL)
```

## API Specifications

### 1. Chapters API

#### 1.1 GET /api/chapters
- **Description**: Retrieves all chapters
- **Parameters**: 
  - `search` (optional): Filter by chapter code or description
  - `page` & `pageSize` (optional): For pagination
- **Response**: 200 OK with array of chapter objects
- **Authentication**: Required (User role)

#### 1.2 GET /api/chapters/{id}
- **Description**: Retrieves a specific chapter by ID
- **Parameters**: 
  - `id`: Chapter ID
- **Response**: 
  - 200 OK with chapter object
  - 404 Not Found if chapter doesn't exist
- **Authentication**: Required (User role)

#### 1.3 POST /api/chapters
- **Description**: Creates a new chapter
- **Request Body**: Chapter object
- **Response**: 
  - 201 Created with created chapter
  - 400 Bad Request for validation errors
- **Authentication**: Required (Admin role)

#### 1.4 PUT /api/chapters/{id}
- **Description**: Updates an existing chapter
- **Parameters**: 
  - `id`: Chapter ID
- **Request Body**: Updated chapter object
- **Response**: 
  - 200 OK with updated chapter
  - 400 Bad Request for validation errors
  - 404 Not Found if chapter doesn't exist
- **Authentication**: Required (Admin role)

#### 1.5 DELETE /api/chapters/{id}
- **Description**: Deletes a chapter
- **Parameters**: 
  - `id`: Chapter ID
- **Response**: 
  - 204 No Content on success
  - 400 Bad Request if chapter is in use
  - 404 Not Found if chapter doesn't exist
- **Authentication**: Required (Admin role)

### 2. Subchapters API

[Detailed API endpoints for subchapters would be specified here, following the same pattern as chapters]

### 3. Fleet Chapter Configuration API

[Detailed API endpoints for fleet chapter configuration would be specified here]

## UI/UX Requirements

### 1. Chapter Management Screen

#### 1.1 Chapter List View
- Display chapters in a sortable, filterable table
- Show chapter code and description
- Include actions for edit and delete operations
- Provide a "New Chapter" button prominently displayed
- Support pagination for large numbers of chapters

#### 1.2 Chapter Detail View
- Provide fields for chapter code and description
- Show related subchapters in a nested table
- Include alert configuration fields
- Display associated fleets
- Provide save, cancel, and delete actions

#### 1.3 Chapter Creation Form
- Simple modal with fields for chapter code and description
- Validate chapter code format and uniqueness
- Clear error messages for validation failures
- Submit and cancel buttons

### 2. Subchapter Management

#### 2.1 Subchapter List View
- Display subchapters for a selected chapter
- Show subchapter code and description
- Include alert parameters (landings, days, ETOPS)
- Provide edit and delete actions
- Display fleet-specific configurations

#### 2.2 Subchapter Detail Form
- Fields for subchapter code and description
- Alert configuration fields (landings, days)
- ETOPS dropdown selection
- Fleet association selector
- "Exclude from fleet" option
- Save and cancel buttons

### 3. Fleet-Specific Configuration

#### 3.1 Fleet Selection Interface
- Dropdown for selecting from available fleets
- Filter showing only chapters/subchapters for selected fleet
- Clear indicator of system-wide vs. fleet-specific settings

#### 3.2 Fleet Exclusion Interface
- Checkbox for "Exclude from fleet" option
- Warning when exclusion might affect existing data
- Summary view of all exclusions for a fleet

### 4. Mockups

[Placeholder for wireframes/mockups of key interfaces]

## Non-Functional Requirements

### 1. Performance

#### 1.1 Response Time
- **NFR1.1.1:** Page load time for chapter list shall not exceed 2 seconds
- **NFR1.1.2:** All API endpoints shall respond within 1 second for standard operations
- **NFR1.1.3:** Bulk operations shall complete within 5 seconds or provide progress indication

#### 1.2 Capacity
- **NFR1.2.1:** The system shall support up to 1,000 chapters
- **NFR1.2.2:** The system shall support up to 10,000 subchapters
- **NFR1.2.3:** The system shall handle at least 50 concurrent users

### 2. Security

#### 2.1 Authentication & Authorization
- **NFR2.1.1:** All API endpoints shall require authentication
- **NFR2.1.2:** Chapter creation/modification shall require admin privileges
- **NFR2.1.3:** All actions shall be logged with user information for audit purposes

#### 2.2 Data Protection
- **NFR2.2.1:** All API communications shall use HTTPS
- **NFR2.2.2:** Sensitive configuration data shall be encrypted in the database
- **NFR2.2.3:** Database access shall follow the principle of least privilege

### 3. Reliability & Availability

- **NFR3.1:** The system shall have 99.9% uptime during business hours
- **NFR3.2:** Data changes shall be transactional to prevent partial updates
- **NFR3.3:** The system shall gracefully handle and recover from errors

### 4. Scalability

- **NFR4.1:** The architecture shall support horizontal scaling of API servers
- **NFR4.2:** Database design shall support sharding if needed in the future
- **NFR4.3:** The application shall use lazy loading for large datasets

### 5. Maintainability

- **NFR5.1:** Code shall follow the SOLID principles as outlined
- **NFR5.2:** All components shall have unit test coverage of at least 80%
- **NFR5.3:** Integration tests shall cover all critical paths
- **NFR5.4:** Documentation shall be provided for all public APIs and components

### 6. Accessibility

- **NFR6.1:** The UI shall conform to WCAG 2.1 Level AA standards
- **NFR6.2:** The application shall be usable with keyboard-only navigation
- **NFR6.3:** The application shall work with screen readers

### 7. Compatibility

- **NFR7.1:** The application shall work in the latest versions of Chrome, Firefox, Edge, and Safari
- **NFR7.2:** The application shall be responsive and work on tablet devices
- **NFR7.3:** The API shall be compatible with the Lumina platform standards

## Implementation Plan

### 1. Phase 1: Database Setup and Data Access Layer

#### 1.1 Tasks
- Create database schema for all entities
- Implement Entity Framework Core models
- Develop repository interfaces and implementations
- Configure DbContext and migrations
- Implement data validation logic

#### 1.2 Timeline
- Duration: 2 weeks
- Dependencies: Database server availability

### 2. Phase 2: Business Logic and API Layer

#### 2.1 Tasks
- Implement business service interfaces and implementations
- Develop DTOs and mapping configuration
- Create API controllers for all entities
- Implement authorization policies
- Configure Swagger documentation

#### 2.2 Timeline
- Duration: 3 weeks
- Dependencies: Phase 1 completion

### 3. Phase 3: UI Implementation

#### 3.1 Tasks
- Develop Angular components for all views
- Implement reactive forms and validation
- Create services for API communication
- Implement state management
- Design and implement responsive UI

#### 3.2 Timeline
- Duration: 4 weeks
- Dependencies: Phase 2 completion

### 4. Phase 4: Testing and Integration

#### 4.1 Tasks
- Conduct unit testing for all components
- Perform integration testing between layers
- Execute end-to-end testing of key workflows
- Validate integration with other system modules
- Conduct user acceptance testing

#### 4.2 Timeline
- Duration: 3 weeks
- Dependencies: Phase 3 completion

## Testing Strategy

### 1. Unit Testing

- **Test Framework**: xUnit for .NET, Jasmine for Angular
- **Coverage Requirements**: Minimum 80% code coverage
- **Key Focus Areas**: 
  - Business logic validation
  - Entity mapping
  - API controller actions
  - Angular component methods

### 2. Integration Testing

- **Test Approach**: API endpoint testing with in-memory database
- **Key Scenarios**:
  - Complete CRUD operations for all entities
  - Cross-entity validations
  - Transaction handling
  - Error responses

### 3. UI Testing

- **Test Framework**: Cypress
- **Key Test Cases**:
  - Chapter creation and management workflow
  - Subchapter configuration
  - Fleet exclusion configuration
  - Form validation handling
  - Error message display

### 4. Performance Testing

- **Test Tool**: JMeter
- **Key Metrics**:
  - Response time under various loads
  - Concurrent user handling
  - Database query performance
  - UI rendering time

### 5. User Acceptance Testing

- **Test Approach**: Guided testing with subject matter experts
- **Key Validation Points**:
  - Functional completeness compared to legacy system
  - Workflow efficiency improvements
  - Data integrity across operations
  - Integration with related modules

## Appendix

### A. Glossary

- **ATA**: Air Transport Association
- **ETOPS**: Extended Twin Operations
- **Chapter Code**: Main category in the ATA classification system
- **Subchapter**: Subdivision within an ATA chapter
- **Fleet**: Group of aircraft of the same type

### B. References

- Source Table Analysis: `docs/PRDs/CAMO/LE07/LE07_SourceTables.md`
- Normalized Schema: `docs/PRDs/CAMO/LE07/LE07_normalized_schema.sql`
- Oracle to PostgreSQL Mapping: `docs/database/NormalizationProgress.md`
- Lumina Design System: [Internal Link]
