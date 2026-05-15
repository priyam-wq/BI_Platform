import os
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import create_sql_agent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_sql_agent():
    """
    Initializes and returns a LangChain SQL agent connected to MySQL and Gemini.
    """
    # 1. Get database connection string
    db_uri = os.getenv("MYSQL_URL")
    if not db_uri or db_uri.startswith("mysql+pymysql://username:password"):
        raise ValueError("MYSQL_URL environment variable is missing or using the default template. Please configure it in .env")
    
    # 2. Connect to the database using LangChain's SQLDatabase utility
    db = SQLDatabase.from_uri(db_uri)
    
    # 3. Initialize the Gemini LLM
    # We use ChatGoogleGenerativeAI with gemini-1.5-pro for complex reasoning
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or api_key == "your_gemini_api_key":
        raise ValueError("GOOGLE_API_KEY is missing. Please configure it in .env")
        
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0, 
        google_api_key=api_key,
        max_retries=5
    )
    
    # 4. Create the SQL toolkit
    # The toolkit gives the agent tools to inspect tables, query the schema, and run SQL queries
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    
    # 5. Create and return the SQL agent
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        handle_parsing_errors=True
    )
    
    return agent_executor
