import asyncio
from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import AsyncGenerator
from agent.agent import SQLAgent
import json
from dotenv import load_dotenv


app = FastAPI()
load_dotenv()
origins = [
    "http://localhost:3000",
      "https://ai-sql-agent.vercel.app" ,
      "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = SQLAgent()


# Define a mock async generator
async def mock_streaming_response() -> AsyncGenerator[bytes, None]:
    data_chunks = [
        b'{"step": "Analyzing the problem", "message": "Starting to process your query"}\n',
        b'{"step": "Gathering relevant information", "message": "Action Tool Input : {\'query\': \\"SELECT c.company_name, e.event_name, e.event_start_date, e.event_end_date FROM companies c JOIN events e ON c.event_url = e.event_url WHERE e.event_country = \'Singapore\' AND e.event_start_date BETWEEN NOW() AND DATE_ADD(NOW(), INTERVAL 9 MONTH) LIMIT 10\\"}"}\n',
        b'{"step": "Executing actions", "message": "Running action: sql_db_query"}\n',
        b'{"step": "Evaluating the solutions", "message": "sql_db_query"}\n',
        b'{"step": "Gathering relevant information", "message": "Action Tool Input : {\'query\': \\"SELECT c.company_name, e.event_name, e.event_start_date, e.event_end_date FROM companies c JOIN events e ON c.event_url = e.event_url WHERE e.event_country = \'Singapore\' AND e.event_start_date BETWEEN NOW() AND DATE_ADD(NOW(), INTERVAL 9 MONTH) LIMIT 10\\"}"}\n',
        b'{"step": "Executing actions", "message": "Running action: sql_db_query"}\n',
        b'{"step": "Evaluating the solutions", "message": "sql_db_query"}\n',
        b'{"step": "Gathering relevant information", "message": "Action Tool Input : {\'query\': \\"SELECT c.company_name, e.event_name, e.event_start_date, e.event_end_date FROM companies c JOIN events e ON c.event_url = e.event_url WHERE e.event_country = \'Singapore\' AND e.event_start_date BETWEEN DATE(\'now\') AND DATE(\'now\', \'+9 months\') LIMIT 10\\"}"}\n',
        b'{"step": "Executing actions", "message": "Running action: sql_db_query"}\n',
        b'{"step": "Evaluating the solutions", "message": "sql_db_query"}\n',
        b'{"step": "Evaluating the results", "message":"processing result"}', 
        b'{"step": "Final Answer", "message": "<div class=\\"overflow-x-auto bg-gradient-to-br from-blue-900 to-teal-800 rounded-lg shadow-xl p-4\\">\\n  <table class=\\"w-full border-collapse\\">\\n    <thead>\\n      <tr class=\\"bg-gradient-to-r from-blue-700 to-teal-600 text-white\\">\\n        <th class=\\"px-4 py-3 text-left text-xs font-semibold uppercase tracking-wider border-b border-blue-500\\">Company Name</th>\\n        <th class=\\"px-4 py-3 text-left text-xs font-semibold uppercase tracking-wider border-b border-blue-500\\">Event Name</th>\\n        <th class=\\"px-4 py-3 text-left text-xs font-semibold uppercase tracking-wider border-b border-blue-500\\">Event Start Date</th>\\n        <th class=\\"px-4 py-3 text-left text-xs font-semibold uppercase tracking-wider border-b border-blue-500\\">Event End Date</th>\\n      </tr>\\n    </thead>\\n    <tbody class=\\"divide-y divide-blue-500\\">\\n      <tr class=\\"bg-gradient-to-r from-blue-800 to-teal-700 hover:from-blue-700 hover:to-teal-600 transition-all duration-200\\">\\n        <td class=\\"px-4 py-3 text-sm text-white\\">Accor</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">AHICE South East Asia</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-25</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-26</td>\\n      </tr>\\n      <tr class=\\"bg-gradient-to-r from-blue-800 to-teal-700 hover:from-blue-700 hover:to-teal-600 transition-all duration-200\\">\\n        <td class=\\"px-4 py-3 text-sm text-white\\">Accor Plus</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">AHICE South East Asia</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-25</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-26</td>\\n      </tr>\\n      <tr class=\\"bg-gradient-to-r from-blue-800 to-teal-700 hover:from-blue-700 hover:to-teal-600 transition-all duration-200\\">\\n        <td class=\\"px-4 py-3 text-sm text-white\\">Bandcamp</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">AHICE South East Asia</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-25</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-26</td>\\n      </tr>\\n      <tr class=\\"bg-gradient-to-r from-blue-800 to-teal-700 hover:from-blue-700 hover:to-teal-600 transition-all duration-200\\">\\n        <td class=\\"px-4 py-3 text-sm text-white\\">BowerBird</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">AHICE South East Asia</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-25</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-26</td>\\n      </tr>\\n      <tr class=\\"bg-gradient-to-r from-blue-800 to-teal-700 hover:from-blue-700 hover:to-teal-600 transition-all duration-200\\">\\n        <td class=\\"px-4 py-3 text-sm text-white\\">Bowerbird Energy</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">AHICE South East Asia</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-25</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-26</td>\\n      </tr>\\n      <tr class=\\"bg-gradient-to-r from-blue-800 to-teal-700 hover:from-blue-700 hover:to-teal-600 transition-all duration-200\\">\\n        <td class=\\"px-4 py-3 text-sm text-white\\">CBRE</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">AHICE South East Asia</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-25</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-26</td>\\n      </tr>\\n      <tr class=\\"bg-gradient-to-r from-blue-800 to-teal-700 hover:from-blue-700 hover:to-teal-600 transition-all duration-200\\">\\n        <td class=\\"px-4 py-3 text-sm text-white\\">CNBC</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">AHICE South East Asia</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-25</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-26</td>\\n      </tr>\\n      <tr class=\\"bg-gradient-to-r from-blue-800 to-teal-700 hover:from-blue-700 hover:to-teal-600 transition-all duration-200\\">\\n        <td class=\\"px-4 py-3 text-sm text-white\\">CNN</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">AHICE South East Asia</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-25</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-26</td>\\n      </tr>\\n      <tr class=\\"bg-gradient-to-r from-blue-800 to-teal-700 hover:from-blue-700 hover:to-teal-600 transition-all duration-200\\">\\n        <td class=\\"px-4 py-3 text-sm text-white\\">The Straits Times</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">AHICE South East Asia</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-25</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-26</td>\\n      </tr>\\n      <tr class=\\"bg-gradient-to-r from-blue-800 to-teal-700 hover:from-blue-700 hover:to-teal-600 transition-all duration-200\\">\\n        <td class=\\"px-4 py-3 text-sm text-white\\">The Business Times</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">AHICE South East Asia</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-25</td>\\n        <td class=\\"px-4 py-3 text-sm text-white\\">2025-02-26</td>\\n      </tr>\\n    </tbody>\\n  </table>\\n</div>"}\n',
    ]
    for chunk in data_chunks:
        yield chunk
        await asyncio.sleep(2)  # Simulate delay between chunks


class Query(BaseModel):
    question: str

# Define a mock endpoint
@app.post("/mockquery")
async def mock_query_endpoint(query: Query):
    return StreamingResponse(
        mock_streaming_response(),
        media_type="text/event-stream",
    )




async def process_query_with_updates(
    question: str, agent: SQLAgent
) -> AsyncGenerator[str, None]:
    async for step, message in agent.process_query(question):
        yield json.dumps({"step": step, "message": message}) + "\n"
        
    final_answer = await agent.get_final_answer()
    yield json.dumps({"step": "Final Answer", "message": final_answer}) + "\n"


@app.post("/query")
async def query_endpoint(query: Query):
    return StreamingResponse(
        process_query_with_updates(query.question, agent),
        media_type="text/event-stream",
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)