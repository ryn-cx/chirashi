# TODO: Validate
"""Contains the SearchEpisode class."""

from __future__ import annotations

from chirashi.search.base import SearchTypeEndpoint
from chirashi.search.episode.models import SearchEpisodeModel


class SearchEpisode(SearchTypeEndpoint[SearchEpisodeModel]):
    """Manage the search episode file."""

    type = "episode"
    _response_model = SearchEpisodeModel
