# TODO: Validate
"""Contains the SearchMovieListing class."""

from __future__ import annotations

from chirashi.search.base import SearchTypeEndpoint
from chirashi.search.movie_listing.models import SearchMovieListingModel


class SearchMovieListing(SearchTypeEndpoint[SearchMovieListingModel]):
    """Manage the search movie listing file."""

    type = "movie_listing"
    _response_model = SearchMovieListingModel
