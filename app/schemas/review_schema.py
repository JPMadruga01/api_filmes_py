from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class ReviewCreateSchema(BaseModel):
    """
    Input schema used to create a new review.
    Validates request payload.
    """
    analysis: str = Field(
        ...,
        min_length=1,
        description="Textual analysis of the movie"
    )
    rating: int = Field(
        ...,
        ge=0,
        le=10,
        description="Rating score between 0 and 10"
    )


class ReviewUpdateSchema(BaseModel):
    """
    Input schema used to partially update a review (PATCH).
    All fields are optional.
    """
    analysis: Optional[str] = Field(None, min_length=1)
    rating: Optional[int] = Field(None, ge=0, le=10)


class ReviewSchema(BaseModel):
    """
    Output schema returned by the API.
    Represents a review linked to a movie.
    """
    id: UUID
    movie_id: UUID
    analysis: str
    rating: int

    @classmethod
    def from_domain(cls, review):
        """
        Converts a domain Review object into a response schema.
        Domain type is not imported to avoid circular dependencies.
        """
        return cls(
            id=review.id,
            movie_id=review.movie_id,
            analysis=review.analysis,
            rating=review.rating,
        )
