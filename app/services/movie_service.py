from typing import List
from uuid import UUID

from app.domain.movie import Movie
from app.schemas.movie_schema import MovieCreateSchema, MovieUpdateSchema


class MovieService:
    """
    Service layer responsible for managing Movie entities.
    Contains application/business logic and in-memory storage.
    """

    def __init__(self):
        # In-memory storage for movies
        self._movies: List[Movie] = []

    def create_movie(self, movie_data: MovieCreateSchema) -> Movie:
        """
        Creates a new Movie domain object from a MovieCreateSchema
        and stores it in memory.

        :param movie_data: Validated input data for creating a movie
        :return: Created Movie object
        """
        data = movie_data.model_dump()
        movie = Movie(**data)
        self._movies.append(movie)
        return movie

    def list_movies(self) -> List[Movie]:
        """
        Returns all registered movies.

        :return: List of Movie objects
        """
        return self._movies

    def get_by_id(self, movie_id: UUID) -> Movie:
        """
        Retrieves a movie by its ID.

        :param movie_id: UUID of the movie
        :return: Movie object if found
        :raises ValueError: If movie is not found
        """
        for movie in self._movies:
            if movie_id == movie.id:
                return movie

        raise ValueError("Movie not found.")

    def update_movie(self, movie_id: UUID, movie_data: MovieUpdateSchema) -> Movie:
        """
        Updates an existing movie using a MovieUpdateSchema.
        Only fields provided by the user are updated.

        :param movie_id: UUID of the movie to update
        :param movie_data: Partial data for update
        :return: Updated Movie object
        """
        movie = self.get_by_id(movie_id)

        # Only update fields that were explicitly sent
        update_data = movie_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            # Uses domain setters, enforcing validation rules
            setattr(movie, field, value)

        return movie

    def delete_movie(self, movie_id: UUID) -> None:
        """
        Deletes a movie from memory by its ID.

        :param movie_id: UUID of the movie to delete
        :raises ValueError: If movie is not found
        """
        movie = self.get_by_id(movie_id)
        self._movies.remove(movie)
