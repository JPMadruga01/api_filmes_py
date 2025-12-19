from typing import List
from uuid import UUID

from app.domain.review import Review
from app.schemas.review_schema import ReviewCreateSchema, ReviewUpdateSchema
from app.services.movie_service import MovieService


class ReviewService:
    """
    Service layer responsible for managing reviews.
    Reviews are always associated with a specific movie.
    """

    def __init__(self, movie_service: MovieService):
        # MovieService is injected to access and validate movie existence
        self.movie_service = movie_service

    def create_review(self, movie_id: UUID, review_data: ReviewCreateSchema) -> Review:
        """
        Creates a new review for a given movie.

        :param movie_id: UUID of the movie
        :param review_data: Validated data to create the review
        :return: Created Review object
        """
        movie = self.movie_service.get_by_id(movie_id)

        review = Review(
            movie=movie,
            analysis=review_data.analysis,
            rating=review_data.rating,
        )

        # Add review to the movie aggregate
        movie.reviews.append(review)

        return review

    def list_reviews(self, movie_id: UUID) -> List[Review]:
        """
        Lists all reviews for a given movie.

        :param movie_id: UUID of the movie
        :return: List of Review objects
        """
        movie = self.movie_service.get_by_id(movie_id)
        return movie.reviews

    def get_review_by_id(self, movie_id: UUID, review_id: UUID) -> Review:
        """
        Retrieves a specific review by its ID within a movie.

        :param movie_id: UUID of the movie
        :param review_id: UUID of the review
        :return: Review object if found
        :raises ValueError: If review is not found
        """
        movie = self.movie_service.get_by_id(movie_id)

        for review in movie.reviews:
            if review.id == review_id:
                return review

        raise ValueError("Review not found.")

    def update_review(
        self,
        movie_id: UUID,
        review_id: UUID,
        review_data: ReviewUpdateSchema,
    ) -> Review:
        """
        Updates an existing review.
        Only fields provided in the request are updated.

        :param movie_id: UUID of the movie
        :param review_id: UUID of the review
        :param review_data: Partial data for update
        :return: Updated Review object
        """
        review = self.get_review_by_id(movie_id, review_id)

        update_data = review_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            # Uses domain setters to enforce validation
            setattr(review, field, value)

        return review

    def delete_review(self, movie_id: UUID, review_id: UUID) -> None:
        """
        Deletes a review from a movie.

        :param movie_id: UUID of the movie
        :param review_id: UUID of the review
        :raises ValueError: If review is not found
        """
        movie = self.movie_service.get_by_id(movie_id)
        review = self.get_review_by_id(movie_id, review_id)

        movie.reviews.remove(review)
