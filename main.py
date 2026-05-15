from fastapi import FastAPI
from routes.api import router as api_router
from database import engine, Base

# Create database tables if they do not exist
# Note: In a real-world scenario, you might want to use Alembic for database migrations
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI(
    title="AI-Powered BI Platform API",
    description="A backend service connecting natural language queries to MySQL database using LangChain and Gemini API.",
    version="1.0.0"
)

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router
app.include_router(api_router)

# Mount the static directory to serve CSS and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the index.html on the root path
@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

# To run this server locally, use the following command:
# uvicorn main:app --reload

if __name__ == "__main__":
    import uvicorn
    # This allows you to run `python main.py` directly for development
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
