from fastapi import APIRouter, HTTPException, status
from typing import List
from uuid import UUID

from app.schemas.review_schema import (
    ReviewCreateSchema,
    ReviewSchema,
    ReviewUpdateSchema,
)
from app.services.container import review_service


router = APIRouter(
    prefix="/movies/{movie_id}/reviews",
    tags=["reviews"],
)


@router.post(
    "",
    response_model=ReviewSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_review(movie_id: UUID, data: ReviewCreateSchema):
    """
    Creates a new review for a given movie.
    """
    try:
        review = review_service.create_review(movie_id, data)
        return ReviewSchema.from_domain(review)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found.",
        )


@router.get(
    "",
    response_model=List[ReviewSchema],
)
def list_reviews(movie_id: UUID):
    """
    Lists all reviews for a specific movie.
    """
    try:
        reviews = review_service.list_reviews(movie_id)
        return [ReviewSchema.from_domain(review) for review in reviews]
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found.",
        )


@router.get(
    "/{review_id}",
    response_model=ReviewSchema,
)
def get_review(movie_id: UUID, review_id: UUID):
    """
    Retrieves a specific review by movie ID and review ID.
    """
    try:
        review = review_service.get_review_by_id(movie_id, review_id)
        return ReviewSchema.from_domain(review)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found.",
        )


@router.put(
    "/{review_id}",
    response_model=ReviewSchema,
)
def update_review(movie_id: UUID, review_id: UUID, data: ReviewCreateSchema):
    """
    Fully updates a review.
    All fields are expected to be provided.
    """
    try:
        review = review_service.update_review(movie_id, review_id, data)
        return ReviewSchema.from_domain(review)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found.",
        )


@router.patch(
    "/{review_id}",
    response_model=ReviewSchema,
)
def partially_update_review(movie_id: UUID, review_id: UUID, data: ReviewUpdateSchema):
    """
    Partially updates a review.
    Only fields sent in the request are updated.
    """
    try:
        review = review_service.update_review(movie_id, review_id, data)
        return ReviewSchema.from_domain(review)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found.",
        )


@router.delete(
    "/{review_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_review(movie_id: UUID, review_id: UUID):
    """
    Deletes a review by movie ID and review ID.
    """
    try:
        review_service.delete_review(movie_id, review_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found.",
        )
