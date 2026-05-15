from fastapi import APIRouter
from pydantic import BaseModel
from services.bi_service import process_business_query

# Create an API Router instance
router = APIRouter()

# Define the request body schema for the /ask endpoint
class AskRequest(BaseModel):
    query: str

@router.get("/health")
def health_check():
    """
    Health check endpoint to ensure the API is running correctly.
    Returns a simple JSON response.
    """
    return {"status": "ok", "message": "BI Platform API is up and running!"}

@router.post("/ask")
def ask_question(request: AskRequest):
    """
    Endpoint to process natural language questions.
    It passes the query to the BI service, which converts it to SQL, 
    queries the database, and returns the insights in JSON format.
    """
    # Call the service layer to process the query
    result = process_business_query(request.query)
    
    return result
