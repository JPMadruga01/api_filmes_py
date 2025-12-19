from typing import TYPE_CHECKING
import uuid

# Used only for type hints to avoid circular imports at runtime
if TYPE_CHECKING:
    from app.domain.movie import Movie


class Review:
    """
    Domain entity that represents a review for a movie.
    Encapsulates validation and business rules related to reviews.
    """

    def __init__(self, movie: "Movie", analysis: str, rating: int):
        self._id = uuid.uuid4()
        self._movie = movie

        # Use setters to enforce validation rules
        self.analysis = analysis
        self.rating = rating

    @property
    def id(self):
        """Unique identifier for the review."""
        return self._id

    @property
    def movie(self) -> "Movie":
        """Returns the movie associated with this review."""
        return self._movie

    @property
    def movie_id(self):
        """Convenience property to access the movie ID."""
        return self._movie.id

    @property
    def analysis(self):
        """Textual analysis of the movie."""
        return self._analysis

    @analysis.setter
    def analysis(self, analysis: str):
        if analysis is None or str(analysis).strip() == "":
            raise ValueError("Analysis must not be empty.")
        if not isinstance(analysis, str):
            raise ValueError("Analysis must be a string.")
        self._analysis = analysis

    @property
    def rating(self):
        """Numeric rating given to the movie."""
        return self._rating

    @rating.setter
    def rating(self, rating: int):
        if rating is None:
            raise ValueError("Rating must be provided.")
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer.")
        if rating < 0 or rating > 10:
            raise ValueError("Rating must be between 0 and 10.")
        self._rating = rating
