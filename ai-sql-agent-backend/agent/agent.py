import json
from typing import Optional, Dict, List, Tuple, AsyncGenerator, Any
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config.settings import settings
from utils.DBconnect import connectToDB 
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

class SQLAgent:
    def __init__(self) -> None:
        self.db,self.context = connectToDB(settings.DATABASE_URL)

        self.llm = ChatGroq(model=settings.LLM_MODEL)
        # toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)
        # self.tools = toolkit.get_tools()


        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", settings.SYSTEM_PROMPT),
                ("human", "{input}"),
                MessagesPlaceholder("agent_scratchpad"),
            ]
        )
        self.agent = create_sql_agent(
            llm=self.llm,
            db=self.db,
            prompt=self.prompt,
            agent_type="tool-calling",
            verbose=True,
            # extra_tools=self.tools
        )

        self.final_answer: Optional[str] = None

    async def process_query(
        self, question: str
    ) -> AsyncGenerator[Tuple[str, str], None]:
        yield "Analyzing the problem", "Starting to process your query"

        try:
            database_schema = "\n".join(self.db.get_usable_table_names())

            async for chunk in self.agent.astream({"input": question, "schema": database_schema, "table_info": self.context}):
                # print(chunk)
                if "actions" in chunk:
                    for action in chunk["actions"]:
                        if action.tool == "sql_db_query":
                            yield "Gathering relevant information", f"Action Tool Input : {action.tool_input}"
                        yield "Executing actions", f"Running action: {action.tool}"
                elif "steps" in chunk:
                    for step in chunk["steps"]:
                        yield "Evaluating the query", step.action.tool
                elif "output" in chunk:
                    self.final_answer = str(chunk["output"])
                    yield "Evaluating the results", "Processing the results"

        except Exception as e:
            print(f"Debug: Error in process_query: {str(e)}")
            yield "Error", f"An error occurred: {str(e)}"

   
    async def get_final_answer(self) -> str:
        if self.final_answer is None:
            return "No query has been processed yet."
        if isinstance(self.final_answer, list):
            return self.final_answer[0]["text"] if self.final_answer else "No result"
        return str(self.final_answer)