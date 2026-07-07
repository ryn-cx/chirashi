# TODO: Validate
"""Search series GAPIClient."""

from __future__ import annotations

from chirashi.search.base import BaseSearchEndpoint
from chirashi.search.series.models import SearchSeries as SearchSeriesModel


class SearchSeries(BaseSearchEndpoint[SearchSeriesModel]):
    """GAPIClient for search series items."""

    _response_model = SearchSeriesModel
