"""Contains the SearchMusic class."""

from __future__ import annotations

from chirashi.search.base import SearchTypeEndpoint
from chirashi.search.music.models import SearchMusicModel


class SearchMusic(SearchTypeEndpoint[SearchMusicModel]):
    """Manage the search music file."""

    type = "music"
    _response_model = SearchMusicModel
