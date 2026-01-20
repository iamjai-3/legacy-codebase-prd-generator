# ATA Chapter Codes (LE07) - Rework Plan

## Overview

This document outlines a detailed plan for reworking the existing LE07 ATA Chapter Codes feature implementation to align with the updated normalized PostgreSQL database schema. The plan covers changes required at each application layer, from entity models to the user interface. The plan prioritizes reusing and updating existing classes rather than creating new ones in different locations.

## 1. Data Access Layer Changes

### 1.1 Entity Class Updates

#### 1.1.1 ChapterEntity (Lumina.Data.CAMO.MaintenanceReference.Entities)
- **Type Changes:**
  - Change `ChapterId` from `string` to `int` with auto-increment
  - Rename `Description` to `ChapterDescription` with CHARACTER(25) type
  - Change `NextChapter` to `NextChapterId` as INTEGER with self-reference
- **Remove Fields:**
  - Remove `ChapterCode` property (derived/not mapped)
  - Remove `SystemCategory` property (not in new schema)
- **Add/Update Fields:**
  - Update `DbtUpdatedAt` and `DbtInvocationId` to be properly mapped to database columns
- **Navigation Properties:**
  - Update `Subchapters` collection with proper cascade options
  - Update `AlertRates` collection with proper cascade options
- **Mapping Configuration:**
  - Update `ChapterEntityTypeConfiguration` with correct column types and constraints

#### 1.1.2 SubchapterEntity (Lumina.Data.CAMO.MaintenanceReference.Entities)
- **Type Changes:**
  - Change `SubchapterId` from `string` to `int` with auto-increment
  - Change `ChapterId` from `string` to `int?` (nullable)
  - Rename `SubchapterCode` to `Subchapter` 
  - Change `Fleet` to `FleetCode` with proper foreign key reference
- **Remove Fields:**
  - Remove `InclusionStatus` and `EtopsStatus` (not in new schema)
- **Column Names:**
  - Ensure all column names match the actual schema
  - Fix mapping for `AlertLimitLandings` and `AlertLimitDays`
- **Navigation Properties:**
  - Update `Chapter` relationship with INTEGER key relationship
  - Add navigation property to `Fleet`

#### 1.1.3 ChapterAlertRateEntity (Lumina.Data.CAMO.MaintenanceReference.Entities)
- **Type Changes:**
  - Change `AlertRateId` from `string` to `int` with auto-increment
  - Change `ChapterId` from `string` to `int?` (nullable)
- **Remove Fields:**
  - Remove `TechLogType`, `AlertStatus`, and `AlertSeverity` (not in new schema)
- **Navigation Properties:**
  - Update `Chapter` relationship with INTEGER key relationship

#### 1.1.4 FleetChapterEntity (Lumina.Data.CAMO.FleetManagement.Entities)
- **Type Changes:**
  - Add explicit `FleetChaptersId` as INTEGER primary key
  - Change `ChapterCode` to `ChapterId` as INTEGER
- **Column Names:**
  - Update column mappings to match schema:
    - Rename `chapter_code` to `chapter_id` with INTEGER type
- **Navigation Properties:**
  - Update `Chapter` foreign key relationship to use INTEGER keys

#### 1.1.5 FleetEntity (Lumina.Data.CAMO.FleetManagement.Entities)
- No major structural changes needed, schema appears to match
- Ensure DBT tracking fields are properly mapped

### 1.2 Repository Implementations

#### 1.2.1 ChapterRepository ✅
- ✅ Updated method signatures to use `int` for chapter IDs
- ✅ Added dynamic column mapping for resilience
- ✅ Updated queries to handle INTEGER IDs
- ✅ Implemented explicit null handling for all operations
- ✅ Implemented fallback mechanisms for schema variations within the existing class structure

#### 1.2.2 SubchapterRepository
- Update method signatures to use `int` for subchapter and chapter IDs
- Implement resilient queries with dynamic table/column detection
- Fix filtering and sorting methods to handle new column names/types
- Add proper null checks for all nullable fields
- Update any SQL queries to reflect new schema

#### 1.2.3 ChapterAlertRateRepository
- Update method signatures to use `int` for alert rate and chapter IDs
- Fix related entity fetching to handle INTEGER relationships
- Update any SQL queries to reflect new schema

#### 1.2.4 FleetChapterRepository ✅
- ✅ Updated method signatures to use proper ID types
- ✅ Fixed composite key handling for new schema
- ✅ Added dynamic table name detection
- ✅ Handled new primary key configuration
- ✅ Added methods for filtering by modification date
- ✅ Added methods for PIREP rate limits and NextChapterId filtering

#### 1.2.5 DbContext Configuration
- Update OnModelCreating to properly configure all entities
- Ensure schema name is consistently "lumina"
- Fix relationship configurations to use correct key types
- Add configurations for DBT tracking fields
- Update existing entity type configurations rather than creating new ones

## 2. Data Transfer Objects and Extension Methods

### 2.1 Update Existing DTOs
- Modify existing DTOs in their current locations:
  - Update property types (string IDs to int)
  - Update property names to match normalized schema
  - Add missing properties for DBT tracking
  - Add proper nullability annotations

### 2.2 Update Extension Methods
- Update existing extension methods in current locations
- Ensure proper null handling in all conversions
- Add validation during conversions
- Fix mapping code to handle type changes

## 3. Business Logic Layer Changes

### 3.1 DTOs

#### 3.1.1 ChapterDto
- Change `ChapterId` from `string` to `int`
- Rename `Description` to `ChapterDescription`
- Change `NextChapter` to `NextChapterId` as `int?`
- Remove properties not in schema
- Add DBT tracking properties

#### 3.1.2 SubchapterDto
- Change `SubchapterId` from `string` to `int` 
- Change `ChapterId` from `string` to `int?`
- Update property names to match entity
- Remove properties not in schema
- Add explicit nullability annotations
- Add DBT tracking properties

#### 3.1.3 ChapterAlertRateDto
- Change `AlertRateId` from `string` to `int`
- Change `ChapterId` from `string` to `int?`
- Remove properties not in schema
- Add DBT tracking properties

#### 3.1.4 FleetChapterDto ✅
- ✅ Added `FleetChapterId` property
- ✅ Changed `ChapterId` from `string` to `int?`
- ✅ Updated property names to match entity
- ✅ Added DBT tracking fields not in schema
- Add explicit nullability annotations
- Add DBT tracking properties

#### 3.1.3 ChapterAlertRateDto
- Change `AlertRateId` from `string` to `int`

### 3.2 Service Implementations

#### 3.2.1 ChapterService ✅
- ✅ Updated implementation to use `int` for chapter IDs
- ✅ Implemented new methods for fleet code filtering
- ✅ Implemented new methods for modified date filtering
- ✅ Updated entity mapping to handle new property types
- ✅ Added structured logging and error handling
- ✅ Added DBT tracking field handling

#### 3.2.2 ISubchapterService and SubchapterService
- Update method signatures to use `int` for IDs
- Fix validation and business rules for modified schema
- Implement proper user identity integration
- Add explicit null parameter handling
- Add performance metrics and structured logging

#### 3.2.3 IChapterAlertRateService and ChapterAlertRateService
- Update method signatures to use `int` for IDs
- Fix alert rate calculation logic to match new schema
- Add performance metrics and structured logging

#### 3.2.4 FleetChapterService ✅
- ✅ Updated implementation to use proper ID types
- ✅ Implemented new methods for fleet and chapter ID filtering
- ✅ Implemented new methods for PIREP rate limits and modified date filtering
- ✅ Added structured logging and error handling
- ✅ Updated entity mapping to handle new property types
- ✅ Added implementation for NextChapterId filtering
- ✅ Added DBT tracking field handling

## 4. API Layer Changes

### 4.1 Controllers

#### 4.1.1 ChapterController

#### 4.1.2 SubchapterController
- Update method signatures to use `int` for IDs
- Fix route templates and parameter binding
- Add validation middleware integration
- Add performance metrics

#### 4.1.3 ChapterAlertRateController
- Update method signatures to use `int` for IDs
- Fix route templates and parameter binding
- Add validation middleware integration
- Add performance metrics

#### 4.1.4 FleetChapterController ✅
- ✅ Updated method signatures to use `int` for fleet chapter IDs
- ✅ Replaced composite key routes with single ID routes
- ✅ Added validation for integer ID parameters
- ✅ Added new endpoints for modified-since, PIREP rate limits, and next chapter ID filtering
- ✅ Updated logging and error handling with structured logging

### 4.2 Middleware ✅
- ✅ Created SchemaValidationMiddleware for validating request bodies against schema compliance requirements
- ✅ Added FleetChapterDto and ChapterDto validation logic
- ✅ Implemented ApplicationBuilderExtensions to register middleware
- ✅ Added HttpContextAccessor registration for middleware support

## 5. UI Layer Changes

### 5.1 Angular Models
- Update TypeScript interfaces to match new DTO structures
- Update ID types from string to number
- Fix property names to match updated DTOs

### 5.2 Angular Services
- Update method signatures to use correct ID types
- Fix API endpoint URLs to match new controller routes
- Add error handling for schema-related issues
- Update any client-side filtering/sorting to handle new property names

### 5.3 Angular Components
- Update forms to handle new property names and types
- Fix binding expressions in templates
- Update validation rules in reactive forms
- Add proper error handling and user feedback for schema-related issues

## 6. Testing Changes

### 6.1 Unit Tests
- Update all test fixtures to use new ID types
- Add tests for schema variation handling
- Add tests for explicit null handling
- Add edge case tests for all services

### 6.2 Integration Tests
- Update test fixtures to match new schema
- Add tests for dynamic table/column detection
- Add tests with schema variations to verify resilience
- Test error handling for schema mismatches

### 6.3 E2E Tests
- Update UI test assertions for new property names/types
- Test full workflows with new schema
- Verify error handling and user feedback

## 7. Project Reference Updates

- Update all project references from 'Oases.*' to 'Lumina.*'
- Fix import statements in source files
- Update dependency injection registrations with existing class names
- Fix namespace references across the solution while maintaining the current project structure

## 8. Implementation Sequence

1. ✅ Update existing Entity models with proper attribute mappings
2. ✅ Update DbContext configuration
3. ✅ Update Repository implementations with dynamic schema handling
   - ✅ Implemented dynamic schema detection in FleetRepository
   - ✅ Added DBT tracking field handling for auditing
   - ✅ Updated method signatures to use int IDs
   - ✅ Added new filtering methods for modified date, aircraft type, and engine type
4. ✅ Update existing DTOs with new type signatures
5. ✅ Update Services to handle the modified entities and DTOs
   - ✅ Updated IChapterService interface to use int IDs
   - ✅ Updated ChapterService implementation to handle int IDs and new filtering methods
   - ✅ Updated IFleetChapterService to use int IDs and add new capabilities
   - ✅ Updated FleetChapterService to implement all interface changes
   - ✅ Added proper error handling and logging throughout service layer
   - ✅ Added DBT tracking field handling for auditing
6. ✅ Add validation middleware and update Controllers (completed)
7. 🔄 Update Angular models and services (in progress)
8. 📝 Update Angular components and templates (not started)
9. 📝 Update all tests (not started)
10. 📝 Final integration testing (not started)

## 9. Rollout Strategy

1. Implement changes in a feature branch
2. Run automated test suite continuously during implementation
3. Perform code reviews for each major component
4. Deploy to development environment for testing
5. Fix issues discovered in testing
6. Deploy to staging environment
7. Conduct user acceptance testing
8. Deploy to production with monitoring

## 10. Fallback Plan

1. Implement feature toggles to control schema version handling
2. Create version-specific repositories that can be toggled
3. Maintain compatibility classes for backward compatibility
4. Have rollback scripts ready for database changes

---

This plan covers the comprehensive changes needed to align the existing implementation with the updated normalized PostgreSQL schema, while ensuring resilience against schema variations and integrating best practices from the LE03 feature.
