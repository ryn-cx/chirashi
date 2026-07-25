"""Contains the SearchEpisode class."""

from __future__ import annotations

from chirashi.search.base import BaseSearch
from chirashi.search.episode.models import SearchEpisodeModel


class SearchEpisode(BaseSearch[SearchEpisodeModel]):
    """Manage the search episode file."""

    search_type = "episode"
    _response_model = SearchEpisodeModel
