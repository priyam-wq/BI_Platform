# AI-Powered Business Intelligence Platform

An intelligent Business Intelligence backend and frontend that allows you to query your SQL databases using plain, natural language. Built with **FastAPI**, **LangChain**, and **Google Gemini**, this platform acts as an AI data assistant that instantly translates human questions into complex SQL queries, executes them against your database, and returns clear, actionable business insights.

## Features
- 🧠 **Natural Language to SQL:** Uses LangChain's SQL Agent to automatically explore your database schema and write accurate queries.
- ⚡ **Lightning Fast Backend:** Built on FastAPI for high performance and automatic interactive API documentation (Swagger UI).
- 🎨 **Premium UI:** Includes a custom-built, animated "glassmorphism" dashboard to chat with your data directly from the browser.
- 📊 **Real-time Token Tracking:** Calculates exactly how much processing power (LLM tokens) the AI is using for every query.
- 🔄 **Resilient:** Built-in auto-retry mechanisms to handle API rate limits and traffic spikes smoothly.

## Tech Stack
- **Backend:** FastAPI, Python, Uvicorn
- **AI / LLM:** Google Gemini API (`gemini-flash-latest`), LangChain
- **Database Connectivity:** SQLAlchemy, PyMySQL
- **Frontend:** Vanilla HTML, CSS (Glassmorphism), Vanilla JavaScript
