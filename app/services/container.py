from app.services.movie_service import MovieService
from app.services.review_service import ReviewService

# Single shared instance of MovieService (in-memory storage lives here)
movie_service = MovieService()

# Single shared instance of ReviewService, using the same MovieService
review_service = ReviewService(movie_service)
