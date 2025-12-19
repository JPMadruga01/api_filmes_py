from datetime import datetime
from typing import List, TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from app.domain.review import Review


class Movie:
    def __init__(
        self,
        title: str,
        description: str,
        director: str,
        release_year: int,
        genre: str,
    ):
        self._id = uuid.uuid4()
        self._title = title
        self._description = description
        self._director = director
        self._release_year = release_year
        self._genre = genre

        # Relationship: one movie can have many reviews
        self._reviews: List["Review"] = []

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        if title is None or str(title).strip() == "":
            raise ValueError("Title must not be empty.")
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description: str):
        if description is None or str(description).strip() == "":
            raise ValueError("Description must not be empty.")
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        self._description = description

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, director: str):
        if director is None or str(director).strip() == "":
            raise ValueError("Director name must not be empty.")
        if not isinstance(director, str):
            raise ValueError("Director must be a string.")
        self._director = director

    @property
    def release_year(self):
        return self._release_year

    @release_year.setter
    def release_year(self, release_year: int):
        if release_year is None:
            raise ValueError("Release year must be provided.")
        if release_year < 1888 or release_year > datetime.now().year:
            raise ValueError("Invalid release year.")
        self._release_year = release_year

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre: str):
        if genre is None or str(genre).strip() == "":
            raise ValueError("Genre must not be empty.")

        allowed_genres = (
            "Action", "Adventure", "Comedy", "Drama", "Horror",
            "Thriller", "Science Fiction", "Fantasy", "Romance",
            "Animation", "Documentary", "Musical", "Western",
            "Crime", "War"
        )

        if genre.title() not in allowed_genres:
            raise ValueError("Invalid genre.")

        self._genre = genre

    @property
    def reviews(self):
        return self._reviews

    def add_review(self, review: "Review"):
        self._reviews.append(review)
