"""Browse series API endpoint."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.browse_series.models import BrowseSeries as BrowseSeriesModel
from chirashi.browse_series.models import Datum


class BrowseSeries(BaseEndpoint[BrowseSeriesModel]):
    """Provides methods to download, parse, and retrieve browse series data."""

    _response_model = BrowseSeriesModel

    def download(
        self,
        *,
        start: int | None = None,
        n: int = 36,
        sort_by: str = "newly_added",
        ratings: str = "true",
        locale: str = "en-US",
    ) -> dict[str, Any]:
        """Downloads browse series data.

        Args:
            start: The starting index for pagination.
            n: The number of results per page.
            sort_by: The sort order.
            ratings: Whether to include ratings.
            locale: The locale for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        params: dict[str, str | int] = {
            "n": n,
            "sort_by": sort_by,
            "ratings": ratings,
            "locale": locale,
        }

        if start is not None:
            params["start"] = start

        headers = {"referer": "https://www.crunchyroll.com/videos/new"}

        return self._client.download(
            "content/v2/discover/browse",
            params,
            headers,
        )

    def get(
        self,
        *,
        start: int | None = None,
        n: int = 36,
        sort_by: str = "newly_added",
        ratings: str = "true",
        locale: str = "en-US",
    ) -> BrowseSeriesModel:
        """Downloads and parses browse series data.

        Convenience method that calls ``download()`` then ``parse()``.

        Args:
            start: The starting index for pagination.
            n: The number of results per page.
            sort_by: The sort order.
            ratings: Whether to include ratings.
            locale: The locale for the request.

        Returns:
            A BrowseSeries model containing the parsed data.
        """
        data = self.download(
            n=n,
            sort_by=sort_by,
            locale=locale,
            start=start,
            ratings=ratings,
        )
        return self.parse(data)

    def get_since_datetime(
        self,
        *,
        n: int = 36,
        locale: str = "en-US",
        sort_by: str = "newly_added",
        ratings: str = "true",
        end_datetime: datetime | None = None,
    ) -> list[BrowseSeriesModel]:
        """Gets all browse pages until end_date is reached (inclusive).

        Args:
            n: The number of results per page.
            locale: The locale for the request.
            sort_by: The sort order.
            ratings: Whether to include ratings.
            end_datetime: Stop when reaching this datetime.

        Returns:
            List of BrowseSeries pages.
        """
        start = 0
        all_data: list[BrowseSeriesModel] = []
        end_datetime = end_datetime or datetime.now().astimezone()

        while True:
            result = self.get(
                n=n,
                locale=locale,
                start=start,
                sort_by=sort_by,
                ratings=ratings,
            )

            all_data.append(result)

            if result.data[-1].last_public < end_datetime or len(result.data) < n:
                return all_data

            start += n

    def extract_entries(
        self,
        input_data: BrowseSeriesModel | list[BrowseSeriesModel],
    ) -> list[Datum]:
        """Returns all of the episodes from one or more BrowseSeries entries."""
        if isinstance(input_data, list):
            result: list[Datum] = []
            for response in input_data:
                result.extend(self.extract_entries(response))
            return result

        return input_data.data
