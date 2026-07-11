# TODO: Validate
"""Episodes API endpoint."""

from __future__ import annotations

from typing import Any, override

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.episodes.models import Episodes as EpisodesModel


class Episodes(BaseEndpoint[EpisodesModel]):
    """Provides methods to download, parse, and retrieve episodes data."""

    _response_model = EpisodesModel

    def download(
        self,
        series_id: str,
        *,
        locale: str = "en-US",
    ) -> dict[str, Any]:
        """Downloads the episodes data for a given season ID.

        Args:
            series_id: The season ID to get episodes for.
            locale: The locale for the request.

        Returns:
            The raw JSON response as a dict, suitable for passing to ``parse()``.
        """
        # This referer is valid, but it's not the ideal one because the real one would
        # include the series slug at the end as well.
        headers = {"referer": f"https://www.crunchyroll.com/series/{series_id}"}
        endpoint = f"content/v2/cms/seasons/{series_id}/episodes"
        params = {"locale": locale}
        return self._client.download(
            endpoint=endpoint,
            params=params,
            headers=headers,
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        return bool(response["data"])

    def get(self, series_id: str, *, locale: str = "en-US") -> EpisodesModel:
        """Downloads and parses the episodes data for a given season ID.

        Args:
            series_id: The season ID to get episodes for.
            locale: The locale for the request.

        Returns:
            An Episodes model containing the parsed data.

        Raises:
            NoContentError: If the response has no meaningful content. The raw
                response is available on the exception's `response` attribute.
        """
        data = self.download(series_id, locale=locale)
        return self._parse_or_raise(data, has_content=self.has_content(data))
