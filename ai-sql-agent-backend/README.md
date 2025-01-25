<a href="https://ai-sql-agent.vercel.app/">
  <video alt="sql-agent-chatbot" src="https://ai-sql-agent.vercel.app/sql-agent.mp4">
</a>
<h1 align="center">FastAPI For SQL Agent</h1>

### AI-powered application that allows users to interact with csv/excel/database

`Check the UI app :` [`APP`](https://github.com/Jayanth-MKV/ai-sql-agent)

`Check the Deployed app :` [`FASTAPI`](https://db-chatapp.onrender.com/docs)

`Check the Demo Video Here :` [`Video`](https://ai-sql-agent.vercel.app/sql-agent.mp4)

## Setup

Clone the repo  
```
git clone <url>
```
Create a .env file in the root directory with the following content:
```
GROQ_API_KEY="..."
```
```
poetry install
```
```
poetry run python main.py
```

The app will start at
```
localhost:8000
```

### Docker Configuration

Follow the `README.Docker.md`



![ss6](https://ai-sql-agent.vercel.app/ss6.png)

## Motivation for Data Engineering/Processing

1. **Data Completeness**: Handle missing or incomplete data to prevent errors in downstream processes. This includes filling in missing values or using intelligent methods to infer missing information.
2. **Data Enrichment**: Enhance the data by adding additional attributes or categories, such as industry tags or location information, using LLMs (Large Language Models) to make the data more useful for specific applications.

## Data Preprocessing - Main Steps:


| **Category**           | **Key Steps**                                                     | **Purpose**                                                      |
|------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| **Event Data Processing**  | **1. Missing Values**                                             | Fill gaps in `event_logo_url`, `event_venue`, and `event_country`. |
|                        | **2. Date Handling**                                             | Standardize dates and calculate event duration.                   |
|                        | **3. Country Standardization**                                    | Ensure uniformity in country names.                               |
|                        | **4. Industry Tagging**                                          | Use LLMs to categorize events into specific industries.           |
|                        | **5. Venue Validation**                                          | Validate and standardize venue information using LLMs.            |
|                        | **6. Domain Extraction**                                         | Simplify URLs by extracting domains.                              |
|                        | **7. Virtual Event Flagging**                                    | Identify and flag virtual events.                                 |
| **People Data Processing** | **1. Missing Values**                                             | Fill gaps in `middle_name`, `person_city`, and `person_country`.   |
|                        | **2. Name Standardization**                                      | Format names uniformly and create a `full_name` field.            |
|                        | **3. Email Generation**                                          | Generate valid emails using predefined patterns with LLMs.        |
|                        | **4. Job Level Categorization**                                  | Classify job titles into levels for better segmentation.          |
|                        | **5. Location Standardization**                                  | Ensure consistent formatting of city, state, and country names.   |
| **Company Data Processing** | **1. Missing Values**                                             | Fill gaps in `company_revenue`, `n_employees`, and `company_industry`. |
|                        | **2. Standardization**                                           | Normalize revenue, employee counts, and industry names.           |
|                        | **3. Year Validation**                                           | Validate and correct the founding year.                           |
|                        | **4. Domain Extraction**                                         | Extract domains from URLs for easier access.                      |
|                        | **5. LinkedIn Presence**                                         | Flag companies with LinkedIn profiles for networking.             |

---

## Main Functionalities of API

- User query analysis
- SQL Query generation
- Query Rechecking
- Execution of the query
- Result Formatting

All combined to form a SQL Agent

## Key Challenges 
- Data consistency issues. Like countries like usa can be united states/us also . This is solved by standardizing all the country names using the LLM in the database.
- Large Datasets querying can lead to context length exceeding. Thus i put a limit of 10 rows for now. Perhaps the separation of querying result from agentic input helps a lot.
- Correcting system prompt for the agent is an insanely frustating task. This prompt required multiple tries to make it work good using the data provided.
- streaming out response for each step of the agent seemed to be unusual at start.
- Sometimes the agent hallucinates and couldn't find the tools correctly. This is corrected by changing the system prompt a bit.
- query rechecking is more frequently done with wrong query initially. this is solved by adjusting the prompt.
- The sqlite database used is prone to memory errors. so make sure the server is not interrupted while running the query.
- The abstractness of langchain agentic classes are very convinient for more complex modifications.
- Some user queries that are not present in the database like event_industry does not contain "Oil & Gas", hence it must be searched over other columns like event_description etc.
- The conditions in the query seems to use = more than LIKE.

## Future Improvements

- Caching responses and queries can be implemented
- The system prompt can be optimized
- Better error handling can be implemented with robust API
- Question suggestions can be implemented
- Custom Data uploads/Custom knowledge base can be implemented
- Multiple conversations can be implemented
- Rate-limit and Authentication
- Feedback mechanism from the user can be implemented

## API

```curl
curl -X 'POST' \
  'https://db-chatapp.onrender.com/query' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question": "Find me events that companies in Pharmaceutical sector are attending"
}'
```

> Response body
```bash
{"step": "Analyzing the problem", "message": "Starting to process your query"}
{"step": "Gathering relevant information", "message": "Action Tool Input : {'query': \"SELECT e.* FROM events e JOIN companies c ON e.event_url = c.event_url WHERE c.company_industry LIKE '%Pharmaceutical%' LIMIT 10\"}"}
{"step": "Executing actions", "message": "Running action: sql_db_query"}
{"step": "Evaluating the query", "message": "sql_db_query"}
{"step": "Final Answer", "message": "## Event Results\n\n| Event Name | Event Start Date | Event Venue | Event Country | Company Name | Company Industry |\n|------------|------------------|-------------|--------------|-------------|-----------------|\n| 2nd Edition of Global Conference on Gynecology & Women's Health | 2024-10-17 | Best Western Plus Hotel & Conference Center | United States | Pfizer | pharmaceutical manufacturing |\n| 2nd Edition of Global Conference on Gynecology & Women's Health | 2024-10-17 | Best Western Plus Hotel & Conference Center | United States | R & S Northeast | pharmaceutical manufacturing |\n| Cyber Security World Asia | 2024-10-09 | Marina Bay Sands | Singapore | Magpharm Laboratoires | pharmaceutical manufacturing |\n| Cloud Expo Asia Singapore 2024 | 2024-10-09 | Marina Bay Sands | Singapore | Magpharm Laboratoires | pharmaceutical manufacturing |\n\n## Key Findings:\n\n* There are 4 events that companies in the Pharmaceutical sector are attending.\n* Pfizer and R & S Northeast are attending the 2nd Edition of Global Conference on Gynecology & Women's Health in the United States.\n* Magpharm Laboratoires is attending Cyber Security World Asia and Cloud Expo Asia Singapore 2024 in Singapore."}
```
