# TODO: Validate
"""Search top results GAPIClient."""

from __future__ import annotations

from chirashi.search.base import BaseSearchEndpoint
from chirashi.search.top_results.models import (
    SearchTopResults as SearchTopResultsModel,
)


class SearchTopResults(BaseSearchEndpoint[SearchTopResultsModel]):
    """GAPIClient for search top results items."""

    _response_model = SearchTopResultsModel
