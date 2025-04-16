# FastAPI Project

This is a FastAPI project template.

## Setup

1. Install uv if you haven't already:
```bash
pip install uv
```

2. Create a virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
uv pip install -r requirements.txt
```

## Running the Application

To run the application, use:
```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000
API documentation will be available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 