from fastapi import APIRouter, HTTPException, status
from typing import List
from uuid import UUID

from app.schemas.movie_schema import (
    MovieCreateSchema,
    MovieUpdateSchema,
    MovieResponseSchema,
)
from app.services.container import movie_service


router = APIRouter(
    prefix="/movies",
    tags=["movies"],
)


@router.post(
    "",
    response_model=MovieResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(data: MovieCreateSchema):
    """
    Creates a new movie.
    - Receives validated data via MovieCreateSchema
    - Calls the MovieService
    - Returns a MovieResponseSchema
    """
    movie = movie_service.create_movie(data)
    return MovieResponseSchema.from_domain(movie)


@router.get(
    "",
    response_model=List[MovieResponseSchema],
)
def list_movies():
    """
    Lists all registered movies.
    """
    movies = movie_service.list_movies()
    return [MovieResponseSchema.from_domain(movie) for movie in movies]


@router.get(
    "/{movie_id}",
    response_model=MovieResponseSchema,
)
def get_movie(movie_id: UUID):
    """
    Retrieves a movie by its ID.
    """
    try:
        movie = movie_service.get_by_id(movie_id)
        return MovieResponseSchema.from_domain(movie)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found.",
        )


@router.put(
    "/{movie_id}",
    response_model=MovieResponseSchema,
)
def update_movie(movie_id: UUID, data: MovieUpdateSchema):
    """
    Fully updates a movie by its ID.
    All fields are expected to be provided.
    """
    try:
        movie = movie_service.update_movie(movie_id, data)
        return MovieResponseSchema.from_domain(movie)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found.",
        )


@router.patch(
    "/{movie_id}",
    response_model=MovieResponseSchema,
)
def partially_update_movie(movie_id: UUID, data: MovieUpdateSchema):
    """
    Partially updates a movie by its ID.
    Only fields sent in the request are updated.
    """
    try:
        movie = movie_service.update_movie(movie_id, data)
        return MovieResponseSchema.from_domain(movie)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found.",
        )


@router.delete(
    "/{movie_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(movie_id: UUID):
    """
    Deletes a movie by its ID.
    """
    try:
        movie_service.delete_movie(movie_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found.",
        )
