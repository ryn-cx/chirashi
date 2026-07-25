"""Contains the SearchSeries class."""

from __future__ import annotations

from chirashi.search.base import BaseSearch
from chirashi.search.series.models import SearchSeriesModel


class SearchSeries(BaseSearch[SearchSeriesModel]):
    """Manage the search series file."""

    search_type = "series"
    _response_model = SearchSeriesModel
