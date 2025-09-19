# Sprint 0: Simple Microservices Repository

## 🎯 Goal
Create a FastAPI application with Person and Address resources implementing full CRUD operations.

## 🚀 Running
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py

API Documentation: http://0.0.0.0:8000/docs
📝 API Endpoints
Person Resource

GET /persons - List all
POST /persons - Create
GET /persons/{id} - Get one
PUT /persons/{id} - Update
DELETE /persons/{id} - Delete

Address Resource

GET /addresses - List all
POST /addresses - Create
GET /addresses/{id} - Get one
PUT /addresses/{id} - Update
DELETE /addresses/{id} - Delete