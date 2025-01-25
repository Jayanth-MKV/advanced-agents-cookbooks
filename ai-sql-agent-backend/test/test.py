from sqlalchemy import create_engine
from config.settings import settings
from agent.agent import SQLAgent
from dotenv import load_dotenv
load_dotenv()
# Create a SQLDatabase instance
engine = create_engine(settings.DATABASE_URL)
agent = SQLAgent()

# Test the agent with a sample query
async def test_query():
    async for step, message in agent.process_query("Find me events that companies in Pharmaceuticals sector are attending"):
        print(step, message)

    final_answer = await agent.get_final_answer()
    print(final_answer)

import asyncio
asyncio.run(test_query())








# import requests
# import json

# url = "http://localhost:8000/query"
# data = {
#         "question": "Find me events that companies in Pharmaceuticals sector are attending"
# }
# # with requests.post(url,json=data, stream=True) as r:
# #     for chunk in r.iter_content(1024):  # or, for line in r.iter_lines():
# #         print(chunk)

# with requests.post(url, json=data, stream=True) as r:
#     # Check if the request was successful
#     r.raise_for_status()
    
#     # Process each line of the streaming response
#     for line in r.iter_lines():
#         if line:
#             # Decode the line from bytes to string
#             decoded_line = line.decode('utf-8')
#             # Print or process the JSON data
#             try:
#                 json_data = json.loads(decoded_line)
#                 print(json.dumps(json_data, indent=2))  # Pretty-print the JSON data
#             except json.JSONDecodeError:
#                 print(f"Failed to decode JSON: {decoded_line}")