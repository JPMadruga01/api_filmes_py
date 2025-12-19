from fastapi import FastAPI

from app.api.movie_router import router as movie_router
from app.api.review_router import router as review_router


app = FastAPI(
    title="Movies API",
    version="1.0.0",
)


# Register application routers
app.include_router(movie_router)
app.include_router(review_router)


@app.get("/")
def healthcheck():
    """
    Simple health check endpoint.
    """
    return {"status": "ok"}
