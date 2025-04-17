# Software Requirements Specification (SRS) – Canti Classics

## Overview
This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Canti Classics website. It outlines the core features, behavior, and constraints of the system, as well as the test cases to verify each requirement.

---

## Software Requirements

This section outlines the functional and non-functional requirements of the system, each tagged with an ID for traceability. Each requirement is linked to corresponding test cases found in the Test Specification section.

### Functional Requirements

#### Website Navigation and Content Display

| ID  | Requirement                                               | Test Cases        |
|-----|-----------------------------------------------------------|-------------------|
| FR1 | Website must provide accessible pages (home, about, etc.) | TC1 – TC6         |
| FR2 | Artists page must load relevant artist content            | TC4               |
| FR3 | Events page should load upcoming event info               | TC2               |
| FR4 | Recordings page must support real-time progress display   | TC3               |
| FR5 | Archives page must provide accessible historical data     | TC5               |

#### User Interaction

| ID  | Requirement                                                  | Test Cases        |
|-----|--------------------------------------------------------------|-------------------|
| FR6 | Users must be able to submit inquiries via form              | TC9 – TC13        |
| FR7 | Email field must validate formatting                         | TC11              |
| FR8 | Users must not be able to submit empty inquiry fields        | TC9               |
| FR9 | Users can unsubscribe from mailing list                      | TC8               |
| FR10| Adding email to the newsletter should redirect after submit  | TC7               |

### Non-Functional Requirements

#### Performance, Usability, Validation, and Security

| ID   | Requirement                                                  | Test Cases           |
|------|--------------------------------------------------------------|----------------------|
| NFR1 | The site must prevent inquiry spam via rate limiting         | TC13                 |
| NFR2 | The newsletter email form should redirect on submit          | TC7                  |
| NFR3 | Input validation should occur on all inquiry fields          | TC9 – TC11           |
| NFR4 | Site should load all pages under 2 seconds (80% of time)     | ST1 (implicit)       |
| NFR5 | JavaScript should restrict input length to 500 characters    | TC10                 |

---

## Test Specification

This section documents the test cases to validate both functional and non-functional requirements.

### Unit Tests

| ID                   | Description                                           | Steps                                      | Input Values                                            | Expected Output                                           | Actual Output | Pass/Fail | Requirement Link   |
|----------------------|-------------------------------------------------------|--------------------------------------------|----------------------------------------------------------|------------------------------------------------------------|----------------|------------|---------------------|
| TC1 - HOME_001       | Home page loads correctly                             | GET /                                       | N/A                                                      | 200 OK + contains 'Home'                                  | Matches        | Pass      | FR1                 |
| TC2 - EVENTS_001     | Events page loads correctly                           | GET /events                                 | N/A                                                      | 200 OK + contains 'Events'                                | Matches        | Pass      | FR3                 |
| TC3 - RECORDINGS_001 | Recordings page loads correctly                       | GET /recordings                             | N/A                                                      | 200 OK + contains 'Recordings'                            | Matches        | Pass      | FR4                 |
| TC4 - ARTISTS_001    | Artists page loads correctly                          | GET /artists                                | N/A                                                      | 200 OK + contains 'Artists'                               | Matches        | Pass      | FR2                 |
| TC5 - ARCHIVES_001   | Archives page loads correctly                         | GET /archives                               | N/A                                                      | 200 OK + contains 'Archives'                              | Matches        | Pass      | FR5                 |
| TC6 - ABOUT_001      | About page loads correctly                            | GET /about                                  | N/A                                                      | 200 OK + contains 'About'                                 | Matches        | Pass      | FR1                 |
| TC7 - ADD_USER_001   | Adding email to newsletter redirects                  | POST /add with email2                       | email2='test@example.com'                                | 302 Redirect                                               | Matches        | Pass      | FR10, NFR2          |
| TC8 - UNSUBSCRIBE_001| Unsubscribe page loads correctly                      | GET /unsubscribe                            | N/A                                                      | 200 OK + contains 'Unsubscribe'                           | Matches        | Pass      | FR9                 |
| TC9 - INQUIRY_MISSING_EMAIL_001 | Inquiry fails without email              | POST /inquiry without email2                | message='test'                                           | 400 or no redirect                                         | Matches        | Pass      | FR6, FR8, NFR3      |
| TC10 - INQUIRY_MAX_LENGTH_001  | Inquiry fails with 500+ char message       | POST /inquiry with 501-char message        | name=bob, email2=valid, message=501-char string          | Error or rejection                                         | Matches        | Pass      | NFR3, NFR5          |
| TC11 - INQURIY_INVALID_EMAIL_001| Reject invalid email                     | POST /inquiry with bad email                | email2="invalid-email"                                   | Error or rejection                                         | Matches        | Pass      | FR7, NFR3           |
| TC12 - INQUIRY_SUCCESS_001     | Valid inquiry submission works              | POST /inquiry with all fields               | name, email2, message                                    | Confirmation or redirect                                  | Matches        | Pass      | FR6, NFR3           |
| TC13 - RATE_LIMIT_001          | Inquiry spam is blocked after repeated posts| POST /inquiry 5x fast                       | email2="test@example.com", message="Spam"                | Block submission                                           | Matches        | Pass      | NFR1                |

### Integration Tests

| ID  | Description                              | Steps                  | Input Values       | Expected Output               | Actual Output | Pass/Fail | Requirement Link |
|-----|------------------------------------------|------------------------|--------------------|-------------------------------|---------------|-----------|------------------|
| IT1 | Newsletter form submit and redirect       | POST /add              | email2=valid       | 302 Redirect                  | Matches       | Pass      | FR10, NFR2       |
| IT2 | Inquiry validation                        | POST /inquiry          | invalid email      | Form not submitted            | Matches       | Pass      | FR6, NFR3        |
| IT3 | Inquiry rate limit block                  | Multiple POST /inquiry | spam               | Request blocked after limit   | Matches       | Pass      | FR6, NFR1        |

### System Tests

| ID  | Description                       | Steps                          | Input Values       | Expected Output                   | Actual Output | Pass/Fail | Requirement Link |
|-----|-----------------------------------|--------------------------------|--------------------|-----------------------------------|---------------|-----------|------------------|
| ST1 | All pages render on deployment    | Run server and visit all URLs  | N/A                | All pages return 200 OK           | Matches       | Pass      | FR1 – FR5         |
| ST2 | Inquiry form success              | POST valid inquiry             | name, email, msg   | Redirect or confirmation message | Matches       | Pass      | FR6               |
| ST3 | Inquiry fails on bad input        | POST with invalid/missing data | missing name/email | Error or rejection                | Matches       | Pass      | NFR3, FR8         |

---

## Software Artifacts

This section links to relevant artifacts such as diagrams, mockups, and documentation.

* [Extended Use Case Descritpion](use_case_diagram/extended_use_case_description.md)
* [UML Diagram](use_case_diagram/UML-Diagram.png)
* [Object Diagram (UML)](object_diagram/object_diagram.pdf)
* [Sequence Diagram](sequence_diagram/sequence_diagram.pdf)
* [Jira Board](https://boostrapers.atlassian.net/jira/software/projects/BT/boards/2)
* [Wireframe (Figma)](https://www.figma.com/design/0Xzhok5Oy4v0Unploml0uV/Laptop-Wireframe?node-id=0-1&p=f&t=iGpN02jtw0xpjcEC-0)
* [Implementation Plan] (implementation_plan/implememntation_plan.md)
* [Functional Specification] (functional_specification/functional_specification.md)
