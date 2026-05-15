from agent import get_sql_agent
from langchain_core.callbacks import BaseCallbackHandler

class TokenTrackerCallback(BaseCallbackHandler):
    def __init__(self):
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.total_tokens = 0

    def on_llm_end(self, response, **kwargs):
        for gen_list in response.generations:
            for gen in gen_list:
                if hasattr(gen, 'message') and hasattr(gen.message, 'usage_metadata') and gen.message.usage_metadata:
                    metadata = gen.message.usage_metadata
                    self.prompt_tokens += metadata.get("input_tokens", 0)
                    self.completion_tokens += metadata.get("output_tokens", 0)
                    self.total_tokens += metadata.get("total_tokens", 0)

# We initialize the agent lazily or handle errors if env vars are missing
def process_business_query(query: str) -> dict:
    """
    Takes a natural language query, runs it through the SQL agent,
    and returns a JSON-friendly response.
    """
    try:
        # Initialize the agent
        agent = get_sql_agent()
    except Exception as e:
         return {
             "status": "error", 
             "message": f"Agent initialization failed. Ensure .env is correctly configured. Error: {str(e)}"
         }
         
    try:
        # Prompt instructing the agent to return clear business insights
        # The agent takes this prompt, figures out the necessary tables, writes the SQL query, 
        # executes it, and analyzes the results to answer the query.
        full_prompt = f"""
        You are a highly skilled business intelligence assistant. 
        Given the following user query, explore the database, run the correct SQL query, 
        and provide a clear, concise business insight based on the data.
        
        User Query: {query}
        """
        
        # Run the agent with token tracking
        cb = TokenTrackerCallback()
        result = agent.invoke({"input": full_prompt}, {"callbacks": [cb]})
        
        # The agent's output is typically a string in result["output"]
        output_text = result.get("output", "No output generated.")
        
        return {
            "status": "success",
            "query": query,
            "insight": output_text,
            "tokens": {
                "input": cb.prompt_tokens,
                "output": cb.completion_tokens,
                "total": cb.total_tokens
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
