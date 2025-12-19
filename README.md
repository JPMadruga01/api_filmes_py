# 🎬 Movies API — FastAPI

A RESTful API for managing movies and their reviews, built with **Python and FastAPI**.  
This project demonstrates backend fundamentals, clean architecture principles, and REST best practices.

Designed as a **portfolio project** to showcase backend development skills using modern Python tooling.

---

## 🚀 Tech Stack

- **Python 3.11+**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- In-memory data storage (for simplicity and learning purposes)

---

## ✨ Features

### Movies
- Create, read, update, and delete movies
- Input validation and domain-level constraints
- Unique movie identification using UUID

### Reviews
- Create and manage reviews associated with a movie
- Nested RESTful routes (`/movies/{movie_id}/reviews`)
- Full and partial updates (PUT / PATCH)

---

## 🧠 Architecture & Design

The project follows a **layered architecture**, promoting separation of concerns and maintainability.

app/
api/ # HTTP layer (FastAPI routers)
domain/ # Business entities and rules
schemas/ # Pydantic models (API contracts)
services/ # Application logic (use cases)
main.py # Application entry point
### Key Design Decisions

- **Router Layer**  
  Responsible only for HTTP concerns (request/response, status codes, validation).

- **Service Layer**  
  Encapsulates business logic and use cases, independent of FastAPI.

- **Domain Layer**  
  Contains core entities (`Movie`, `Review`) with encapsulated behavior and validation.

- **Schemas (Pydantic)**  
  Define clear API contracts for input and output, decoupled from domain models.

- **Dependency Container**  
  Shared service instances to maintain consistent in-memory state across routers.

---

## 📌 API Endpoints

### Movies
- `POST /movies`
- `GET /movies`
- `GET /movies/{movie_id}`
- `PUT /movies/{movie_id}`
- `PATCH /movies/{movie_id}`
- `DELETE /movies/{movie_id}`

### Reviews
- `POST /movies/{movie_id}/reviews`
- `GET /movies/{movie_id}/reviews`
- `GET /movies/{movie_id}/reviews/{review_id}`
- `PUT /movies/{movie_id}/reviews/{review_id}`
- `PATCH /movies/{movie_id}/reviews/{review_id}`
- `DELETE /movies/{movie_id}/reviews/{review_id}`

---

## ⚙️ How to Run

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn

# Run the application
uvicorn app.main:app --reload
