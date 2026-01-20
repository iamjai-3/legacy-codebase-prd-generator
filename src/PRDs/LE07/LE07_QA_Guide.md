# ATA Chapters QA Guide

## Basic Information
- **Feature Code**: LE07
- **JIRA Ticket**: https://aphinity.atlassian.net/browse/CON-1453
- **Developers**: Andy Weatherall
- **QA Contact**: [TO_BE_FILLED]
- **Last Updated**: 2025-07-08

## Navigation
- **Entry Point URL**: `/maintenance-reference/ata-chapters`
- **Parent Section**: Maintenance Reference (`/maintenance-reference`)

## Key Elements
| Element | QA-ID | Description | Type | Required | Validation Rules |
|---------|-------|-------------|-------|-----------|------------------|
| Page Header | `ata-chapters-header` | Main header with title and create button | div | Yes | Contains title and create button |
| Page Title | `ata-chapters-title` | Main page title | h1 | Yes | "ATA Chapters" |
| Create Button | `ata-chapters-create-button` | Button to create new chapter | button | Yes | Opens create dialog |
| Filter Section | `ata-chapters-filters` | Filter controls container | div | Yes | Contains search and filter inputs |
| Search Input | `ata-chapters-filters-search-input` | Search by description | input | No | Max 100 chars |
| Chapter Code Input | `ata-chapters-filters-chapter-id-input` | Filter by chapter code | input | No | Numeric, 2 digits |
| Clear Filters | `ata-chapters-filters-clear-all-button` | Clear all filters | button | No | Visible when filters active |
| Chapter List | `ata-chapters-list` | Main data table | table | Yes | Displays chapters with pagination |
| Table Header | `ata-chapters-list-header-row` | Table column headers | tr | Yes | Sortable columns |
| Sort Code | `ata-chapters-list-sort-code` | Sort by chapter code | button | Yes | Toggles asc/desc |
| Sort Description | `ata-chapters-list-sort-description` | Sort by description | button | Yes | Toggles asc/desc |
| Chapter Row | `ata-chapters-list-row-{id}` | Individual chapter row | tr | Yes | Clickable, opens edit dialog |
| Edit Action | `ata-chapters-list-edit-{id}` | Edit chapter action | button | Yes | Opens edit dialog |
| Pagination | `ata-chapters-list-pagination` | Pagination controls | div | No | Shows when >1 page |
| **Create Dialog** | `create-ata-chapter-dialog` | Create new chapter dialog | dialog | Yes | Modal form |
| Create Dialog Content | `create-ata-chapter-dialog-content` | Dialog content container | div | Yes | Contains form |
| Create Dialog Header | `create-ata-chapter-dialog-header` | Dialog header section | div | Yes | Contains title and description |
| Create Dialog Title | `create-ata-chapter-dialog-title` | Dialog title text | h2 | Yes | "Create ATA Chapter" |
| Create Dialog Description | `create-ata-chapter-dialog-description` | Dialog description text | p | Yes | Instruction text |
| Create Dialog Form | `create-ata-chapter-dialog-form` | Form within create dialog | form | Yes | Contains form fields |
| **Edit Dialog** | `edit-ata-chapter-dialog` | Edit existing chapter dialog | dialog | Yes | Modal form |
| Edit Dialog Content | `edit-ata-chapter-dialog-content` | Dialog content container | div | Yes | Contains form |
| Edit Dialog Header | `edit-ata-chapter-dialog-header` | Dialog header section | div | Yes | Contains title and description |
| Edit Dialog Title | `edit-ata-chapter-dialog-title` | Dialog title text | h2 | Yes | "Edit ATA Chapter" |
| Edit Dialog Description | `edit-ata-chapter-dialog-description` | Dialog description text | p | Yes | Instruction text |
| Edit Dialog Form | `edit-ata-chapter-dialog-form` | Form within edit dialog | form | Yes | Contains form fields |
| **Form Fields** | | | | | |
| Form Error Alert | `ata-chapter-form-error-alert` | Form validation error alert | div | No | Shows on validation errors |
| Chapter Code Label | `ata-chapter-form-chapter-code-label` | Chapter code field label | label | Yes | "Chapter Code *" |
| Chapter Code Input | `ata-chapter-form-chapter-code-input` | Chapter code input field | input | Yes | 2-digit number, disabled when editing |
| Chapter Code Description | `ata-chapter-form-chapter-code-description` | Chapter code help text | p | Yes | Field instruction text |
| Chapter Code Error | `ata-chapter-form-chapter-code-error` | Chapter code validation error | span | No | Shows validation messages |
| Description Label | `ata-chapter-form-description-label` | Description field label | label | Yes | "Description *" |
| Description Input | `ata-chapter-form-description-input` | Description textarea field | textarea | Yes | Max 25 chars |
| Description Description | `ata-chapter-form-description-description` | Description help text | p | Yes | Field instruction text |
| Description Error | `ata-chapter-form-description-error` | Description validation error | span | No | Shows validation messages |
| Form Actions | `ata-chapter-form-actions` | Form button container | div | Yes | Contains cancel and submit buttons |
| Cancel Button | `ata-chapter-form-cancel-button` | Cancel form action | button | Yes | Closes dialog without saving |
| Submit Button | `ata-chapter-form-submit-button` | Submit form action | button | Yes | Creates or updates chapter |

## Test Data

### Test Scenarios
```yaml
valid_chapter_creation:
  description: "Create new ATA chapter with valid data"
  input:
    chapterId: "32"
    chapterDescription: "Landing Gear"
  expected_results:
    success: true
    created_chapter:
      chapterId: 32
      chapterDescription: "Landing Gear"

invalid_chapter_code:
  description: "Create chapter with invalid code"
  input:
    chapterId: "ABC"
    chapterDescription: "Test Chapter"
  expected_results:
    error: "Chapter code must be a 2-digit number (00-99)"

duplicate_chapter:
  description: "Create chapter with existing code"
  input:
    chapterId: "32"
    chapterDescription: "Duplicate Chapter"
  expected_results:
    error: "Chapter with this code already exists"

search_chapters:
  description: "Search chapters by description"
  input:
    search: "landing"
  expected_results:
    filtered_results: true
    contains: "Landing Gear"

pagination_test:
  description: "Test pagination with 20+ chapters"
  input:
    pageSize: 20
    pageNumber: 2
  expected_results:
    page_size: 20
    current_page: 2
    navigation_enabled: true
```

## Common Flows

### 1. View ATA Chapters List
1. Navigate to `/maintenance-reference/ata-chapters`
2. Verify page loads with `ata-chapters-title` displaying "ATA Chapters"
3. Verify `ata-chapters-list` displays chapters in table format
4. Verify columns: Chapter Code, Description, Subchapters, Actions
5. Verify pagination controls appear if more than 20 chapters

### 2. Create New ATA Chapter
1. Navigate to `/maintenance-reference/ata-chapters`
2. Click `ata-chapters-create-button`
3. Verify `create-ata-chapter-dialog` opens
4. Fill `ata-chapter-form-chapter-code-input` with "32"
5. Fill `ata-chapter-form-description-input` with "Landing Gear"
6. Click `ata-chapter-form-submit-button`
7. Verify success toast appears
8. Verify new chapter appears in list
9. Verify edit dialog opens for newly created chapter

### 3. Edit Existing ATA Chapter
1. Navigate to `/maintenance-reference/ata-chapters`
2. Click on any chapter row OR click actions menu > Edit
3. Verify `edit-ata-chapter-dialog` opens
4. Verify chapter code field is disabled
5. Modify `ata-chapter-form-description-input`
6. Click `ata-chapter-form-submit-button`
7. Verify success toast appears
8. Verify updated description appears in list

### 4. Search and Filter Chapters
1. Navigate to `/maintenance-reference/ata-chapters`
2. Enter text in `ata-chapters-filters-search-input`
3. Verify list filters to show matching descriptions
4. Enter number in `ata-chapters-filters-chapter-id-input`
5. Verify list filters to show matching chapter codes
6. Click `ata-chapters-filters-clear-all-button`
7. Verify all filters are cleared and full list is displayed

### 5. Sort Chapters
1. Navigate to `/maintenance-reference/ata-chapters`
2. Click `ata-chapters-list-sort-code`
3. Verify chapters are sorted by code (ascending)
4. Click `ata-chapters-list-sort-code` again
5. Verify chapters are sorted by code (descending)
6. Click `ata-chapters-list-sort-description`
7. Verify chapters are sorted by description (ascending)

### 6. Pagination Navigation
1. Navigate to `/maintenance-reference/ata-chapters` (ensure 20+ chapters exist)
2. Verify pagination controls are visible
3. Click `ata-chapters-list-pagination-next`
4. Verify page number changes and new results load
5. Click `ata-chapters-list-pagination-previous`
6. Verify page number changes and previous results load
7. Click specific page number
8. Verify navigation to that page

### 7. Navigation Context
1. Navigate to `/maintenance-reference`
2. Verify "Maintenance Reference" section is displayed
3. Verify "ATA Chapters" appears in navigation menu
4. Click on "ATA Chapters" navigation item
5. Verify navigation to `/maintenance-reference/ata-chapters`
6. Verify breadcrumb shows current location in hierarchy

## API Endpoints

### Get All Chapters
- **Endpoint**: `GET /api/maintenance-reference/Chapter`
- **Parameters**:
  - `pageNumber`: Page number (number, default: 1)
  - `pageSize`: Results per page (number, default: 20)
  - `search`: Search term (string, optional)
  - `chapterId`: Chapter ID filter (number, optional)
  - `sortBy`: Sort field (string, default: "ChapterId")
  - `sortDirection`: Sort direction (string, default: "asc")
- **Response**:
  ```json
  {
    "items": [
      {
        "chapterId": 32,
        "chapterDescription": "Landing Gear",
        "subchapterCount": 5,
        "alertRateCount": 2
      }
    ],
    "totalCount": 50,
    "pageNumber": 1,
    "pageSize": 20,
    "totalPages": 3,
    "hasPreviousPage": false,
    "hasNextPage": true
  }
  ```

### Get Chapter by ID
- **Endpoint**: `GET /api/maintenance-reference/Chapter/{id}`
- **Parameters**:
  - `id`: Chapter ID (number, required)
- **Response**:
  ```json
  {
    "chapterId": 32,
    "chapterDescription": "Landing Gear",
    "subchapterCount": 5,
    "alertRateCount": 2
  }
  ```

### Create Chapter
- **Endpoint**: `POST /api/maintenance-reference/Chapter`
- **Request Body**:
  ```json
  {
    "chapterId": 32,
    "chapterDescription": "Landing Gear"
  }
  ```
- **Response**: Created chapter object (201 Created)

### Update Chapter
- **Endpoint**: `PUT /api/maintenance-reference/Chapter/{id}`
- **Request Body**:
  ```json
  {
    "chapterId": 32,
    "chapterDescription": "Updated Landing Gear"
  }
  ```
- **Response**: Updated chapter object (200 OK)

### Delete Chapter
- **Endpoint**: `DELETE /api/maintenance-reference/Chapter/{id}`
- **Response**: 204 No Content

## Security Notes
- Authentication via Keycloak using OpenID Connect (OIDC)
- Input validation using Zod schema validation
- Role-based access control (implementation details TBD)
- XSS prevention through React's built-in sanitization
- SQL injection prevention via Entity Framework parameterized queries

## Performance Considerations
- Search input debounced with 500ms delay
- Default page size: 20 items
- Pagination supports efficient data loading
- React Query caching for API responses

## Browser Compatibility
- Modern browsers supporting ES6+ features
- Tested with latest Chrome, Firefox, Safari, Edge

## Related Documentation
- https://aphinity.atlassian.net/wiki/spaces/LM/pages/2067922949/Migrate+LE07+ATA+Chapter+Codes+Management+to+Lumina

## Changelog
| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 08/07/2025 | 1.0.0 | Initial ATA Chapters implementation | Andy Weatherall |