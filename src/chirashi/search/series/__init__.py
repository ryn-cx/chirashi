# TODO: Validate
"""Contains the SearchSeries class."""

from __future__ import annotations

from chirashi.search.base import SearchTypeEndpoint
from chirashi.search.series.models import SearchSeriesModel


class SearchSeries(SearchTypeEndpoint[SearchSeriesModel]):
    """Manage the search series file."""

    type = "series"
    _response_model = SearchSeriesModel
