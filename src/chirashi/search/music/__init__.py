# TODO: Validate
"""Search music GAPIClient."""

from __future__ import annotations

from chirashi.search.base import BaseSearchEndpoint
from chirashi.search.music.models import SearchMusic as SearchMusicModel


class SearchMusic(BaseSearchEndpoint[SearchMusicModel]):
    """GAPIClient for search music items."""

    _response_model = SearchMusicModel
