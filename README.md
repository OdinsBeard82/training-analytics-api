# Training Analytics API

A production-ready REST API for logging and retrieving workout sessions, built with Python, FastAPI, SQLAlchemy, and PostgreSQL.

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* psycopg2

## API Endpoints

### Health Check

GET /health
Returns `{"status": "ok"}`

### Create a Workout
POST /workouts
Request body:
```json
{
  "name": "Morning Run",
  "date": "2026-04-28",
  "duration_minutes": 30
}
```
Response:
```json
{
  "id": 1,
  "name": "Morning Run",
  "date": "2026-04-28",
  "duration_minutes": 30
}
```

### Get a Workout by ID
GET /workouts/{id}
Response:
```json
{
  "id": 1,
  "name": "Morning Run",
  "date": "2026-04-28",
  "duration_minutes": 30
}
```

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/OdinsBeard82/training-analytics-api.git
cd training-analytics-api
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file
```env
DATABASE_URL=postgresql://your_username@localhost:5432/training_analytics_dev
```

### 5. Create the database
```bash
createdb training_analytics_dev
```

### 6. Start the server
```bash
uvicorn app.main:app --reload
```

The API will run at `http://localhost:8000`

Interactive docs available at `http://localhost:8000/docs`

## Project Structure

```
app/
├── api/
│   └── routes/
│       └── workouts.py     # Route definitions
├── core/
│   └── config.py           # Environment configuration
├── crud/
│   └── workout.py          # Database operations
├── db/
│   ├── base.py             # SQLAlchemy base
│   ├── init_db.py          # Database initialisation
│   └── session.py          # Session management
├── models/
│   └── workout.py          # SQLAlchemy models
├── schemas/
│   └── workout.py          # Pydantic schemas
└── main.py                 # Application entry point
```

## Validation

* `duration_minutes` must be between 1 and 59
* `date` must be a valid date string (YYYY-MM-DD)
* `name` is required

## Future Improvements

* Add GET /workouts to list all workouts
* Add DELETE and PUT endpoints
* Add user authentication (JWT)
* Add filtering by date range
* Deploy to Render
* Add test coverage with pytest

  ## Live Demo

**Base URL:** https://training-analytics-api.onrender.com

> Note: hosted on Render's free tier — first request may take ~50 seconds to wake up.

Interactive API docs: https://training-analytics-api.onrender.com/docs

