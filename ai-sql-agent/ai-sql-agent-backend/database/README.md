# Database Schema & Processing Data (Events,Company,people)

`Check the UI app :` [`APP`](https://github.com/Jayanth-MKV/ai-sql-agent)

`Check the Deployed app :` [`FASTAPI`](https://db-chatapp.onrender.com/docs)


This repository contains the database schema for managing information on companies, events, and people. Below is an overview of each table in the database:

## Schema

### 1. **Companies Table**
| **Column Name**                  | **Data Type** | **Description**                                                                 |
|----------------------------------|---------------|---------------------------------------------------------------------------------|
| `company_logo_url`               | TEXT          | URL of the company’s logo.                                                      |
| `company_logo_text`              | TEXT          | Text description of the company’s logo.                                         |
| `company_name`                   | TEXT          | Name of the company.                                                            |
| `relation_to_event`              | TEXT          | Company’s relation to the event (e.g., sponsor, partner).                       |
| `event_url`                      | TEXT          | URL of the event associated with the company.                                   |
| `company_revenue`                | TEXT          | Company’s revenue.                                                              |
| `n_employees`                    | TEXT          | Number of employees in the company.                                             |
| `company_phone`                  | TEXT          | Contact phone number of the company.                                            |
| `company_founding_year`          | REAL          | Year the company was founded.                                                   |
| `company_address`                | TEXT          | Physical address of the company.                                                |
| `company_industry`               | TEXT          | Industry sector the company operates in.                                        |
| `company_overview`               | TEXT          | A brief overview of the company.                                                |
| `homepage_url`                   | TEXT          | URL of the company’s homepage.                                                  |
| `linkedin_company_url`           | TEXT          | LinkedIn profile URL of the company.                                            |
| `homepage_base_url`              | TEXT          | Base URL of the company’s homepage.                                             |
| `company_logo_url_on_event_page` | TEXT          | URL of the company’s logo as displayed on the event page.                       |
| `company_logo_match_flag`        | TEXT          | Flag indicating if the company logo matches across sources.                     |
| `company_revenue_standardized`   | TEXT          | Standardized company revenue.                                                   |
| `n_employees_standardized`       | REAL          | Standardized number of employees.                                               |
| `company_phone_cleaned`          | REAL          | Cleaned version of the company’s phone number.                                  |
| `has_logo`                       | INTEGER       | Flag indicating if the company has a logo.                                      |
| `domain`                         | TEXT          | Domain extracted from the company’s URL.                                        |
| `has_linkedin`                   | INTEGER       | Flag indicating if the company has a LinkedIn profile.                          |
| `valid_homepage_base_url`        | INTEGER       | Flag indicating if the homepage base URL is valid.                              |

### 2. **Events Table**
| **Column Name**             | **Data Type** | **Description**                                                                 |
|-----------------------------|---------------|---------------------------------------------------------------------------------|
| `event_logo_url`            | TEXT          | URL of the event’s logo.                                                        |
| `event_name`                | TEXT          | Name of the event.                                                              |
| `event_start_date`          | TEXT          | Start date of the event.                                                        |
| `event_end_date`            | TEXT          | End date of the event.                                                          |
| `event_venue`               | TEXT          | Venue where the event is held.                                                  |
| `event_country`             | TEXT          | Country where the event is held.                                                |
| `event_description`         | TEXT          | Brief description of the event.                                                 |
| `event_url`                 | TEXT          | URL of the event.                                                               |
| `event_duration`            | REAL          | Duration of the event in hours.                                                 |
| `has_logo`                  | INTEGER       | Flag indicating if the event has a logo.                                        |
| `event_year`                | INTEGER       | Year the event is held.                                                         |
| `event_month`               | INTEGER       | Month the event is held.                                                        |
| `event_id`                  | INTEGER       | Unique identifier for the event.                                                |
| `event_industry`            | TEXT          | Industry sector the event belongs to.                                           |
| `event_domain`              | TEXT          | Domain extracted from the event’s URL.                                          |
| `is_virtual`                | INTEGER       | Flag indicating if the event is virtual.                                        |
| `event_duration_in_days`    | REAL          | Duration of the event in days.                                                  |

### 3. **People Table**
| **Column Name**                     | **Data Type** | **Description**                                                                 |
|-------------------------------------|---------------|---------------------------------------------------------------------------------|
| `first_name`                        | TEXT          | First name of the person.                                                       |
| `middle_name`                       | TEXT          | Middle name of the person.                                                      |
| `last_name`                         | TEXT          | Last name of the person.                                                        |
| `job_title`                         | TEXT          | Job title of the person.                                                        |
| `person_city`                       | TEXT          | City where the person is located.                                               |
| `person_state`                      | TEXT          | State where the person is located.                                              |
| `person_country`                    | TEXT          | Country where the person is located.                                            |
| `email_pattern`                     | TEXT          | Pattern used for generating the person’s email.                                 |
| `homepage_base_url`                 | TEXT          | Base URL of the person’s associated company homepage.                           |
| `duration_in_current_job`           | TEXT          | Duration the person has been in their current job.                              |
| `duration_in_current_company`       | TEXT          | Duration the person has been in their current company.                          |
| `full_name`                         | TEXT          | Full name of the person.                                                        |
| `generated_email`                   | TEXT          | Generated email for the person.                                                 |
| `duration_in_current_job_months`    | REAL          | Duration in the current job in months.                                          |
| `duration_in_current_company_months`| REAL          | Duration in the current company in months.                                      |
| `person_id`                         | INTEGER       | Unique identifier for the person.                                               |
| `company_domain`                    | TEXT          | Domain of the person’s associated company.                                      |
| `job_level`                         | TEXT          | Job level of the person (e.g., Individual Contributor, Middle Management).      |

## Challenges Faced

1. **Data Inconsistencies**: When I dug into the data, I encountered some major hurdles. First, there were inconsistencies , such as varying formats for dates, addresses, and names, was a significant challenge. Ensuring that the data is standardized across all entries required meticulous cleaning processes.
   
2. **Missing Data**: Another issue was the sheer amount of missing data, particularly in fields like company phone numbers, addresses, and revenue information. Filling in these gaps intelligently while maintaining data integrity was difficult.

3. **Normalization Issues**: Also struggled with normalization. Standardizing revenue, employee counts, and industry names across different datasets involved complex normalization processes to ensure consistency and comparability.

4. **Validation Complexities**: Had to make sure that things like company founding years, phone numbers, and URLs were accurate, but the data came from all sorts of sources and formats, making it tough to keep everything straight.

## Potential Improvements


1. **Enhanced Normalization**: Further normalization of the data could be implemented to reduce redundancy and improve the efficiency of data storage. For example, separating out industry sectors into a related table would allow for more flexible querying.

2. **Advanced Validation Mechanisms**: Implementing more sophisticated validation mechanisms using machine learning models could improve the accuracy of fields like revenue and employee counts, and better identify anomalies in the data.

3. **Improved Schema Design**: The schema could be optimized by creating more relationships between tables, such as linking people to companies through a many-to-many relationship table, to better capture the complexity of real-world relationships.

4. **Comprehensive Error Logging**: Incorporating a comprehensive error logging system would help track and resolve data issues more efficiently, providing more insights into where and why data cleaning might fail.
