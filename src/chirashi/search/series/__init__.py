"""Contains the SearchSeries class."""

from __future__ import annotations

from chirashi.search.base import BaseSearch
from chirashi.search.series.models import SearchSeriesModel, model_validate_json


class SearchSeries(BaseSearch[SearchSeriesModel]):
    """Manage the search series file."""

    search_type = "series"
    MODEL = SearchSeriesModel
    LOAD = staticmethod(model_validate_json)
