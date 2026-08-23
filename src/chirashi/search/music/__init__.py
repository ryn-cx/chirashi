"""Contains the SearchMusic class."""

from __future__ import annotations

from chirashi.search.base import BaseSearch
from chirashi.search.music.models import SearchMusicModel, model_validate_json


class SearchMusic(BaseSearch[SearchMusicModel]):
    """Manage the search music file."""

    search_type = "music"
    MODEL = SearchMusicModel
    LOAD = staticmethod(model_validate_json)
