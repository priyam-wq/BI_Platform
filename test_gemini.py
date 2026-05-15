from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(f"Testing with API Key: {api_key[:10]}...")

try:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
    res = llm.invoke("Say hello")
    print("SUCCESS:", res.content)
except Exception as e:
    print("ERROR:", e)
