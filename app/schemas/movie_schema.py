from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List

from app.schemas.review_schema import ReviewSchema
from app.domain.movie import Movie


class MovieCreateSchema(BaseModel):
    """
    Input schema used to create a new movie.
    Validates incoming request data.
    """
    title: str
    description: str
    director: str
    release_year: int = Field(..., ge=1888, le=datetime.now().year)
    genre: str


class MovieUpdateSchema(BaseModel):
    """
    Input schema used to partially update a movie (PATCH).
    All fields are optional.
    """
    title: Optional[str] = None
    description: Optional[str] = None
    director: Optional[str] = None
    release_year: Optional[int] = Field(None, ge=1888, le=datetime.now().year)
    genre: Optional[str] = None


class MovieResponseSchema(BaseModel):
    """
    Output schema returned by the API.
    Represents a movie with its related reviews.
    """
    id: str
    title: str
    description: str
    director: str
    release_year: int
    genre: str
    reviews: List[ReviewSchema] = []

    @classmethod
    def from_domain(cls, movie: Movie):
        """
        Converts a domain Movie object into a response schema.
        """
        return cls(
            id=movie.id,
            title=movie.title,
            description=movie.description,
            director=movie.director,
            release_year=movie.release_year,
            genre=movie.genre,
            reviews=movie.reviews,
        )
