"""Contains the SearchMovieListing class."""

from __future__ import annotations

from chirashi.search.base import BaseSearch
from chirashi.search.movie_listing.models import SearchMovieListingModel


class SearchMovieListing(BaseSearch[SearchMovieListingModel]):
    """Manage the search movie listing file."""

    search_type = "movie_listing"
    _response_model = SearchMovieListingModel
