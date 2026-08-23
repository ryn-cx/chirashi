"""Contains the SearchEpisode class."""

from __future__ import annotations

from chirashi.search.base import BaseSearch
from chirashi.search.episode.models import SearchEpisodeModel, model_validate_json


class SearchEpisode(BaseSearch[SearchEpisodeModel]):
    """Manage the search episode file."""

    search_type = "episode"
    MODEL = SearchEpisodeModel
    LOAD = staticmethod(model_validate_json)
