# TODO: Validate
"""Search episodes GAPIClient."""

from __future__ import annotations

from chirashi.search.base import BaseSearchEndpoint
from chirashi.search.episodes.models import SearchEpisode as SearchEpisodeModel


class SearchEpisode(BaseSearchEndpoint[SearchEpisodeModel]):
    """GAPIClient for search episode items."""

    _response_model = SearchEpisodeModel

