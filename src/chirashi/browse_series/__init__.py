# TODO: Validate
"""Contains the Browse class."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, override

from good_ass_pydantic_integrator import CustomSerializer, ReplacementType

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.browse_series.models import (
    BrowseSeries as BrowseModel,
)

if TYPE_CHECKING:
    from chirashi.browse_series.models import Datum


class Browse(BaseEndpoint[BrowseModel]):
    """Manage the browse file."""

    _response_model = BrowseModel

    def download(
        self,
        *,
        start: int | None = None,
        n: int = 36,
        sort_by: str = "newly_added",
        ratings: str = "true",
        locale: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the browse file.

        Example request:
            GET /content/v2/discover/browse?n=36&sort_by=newly_added&ratings=true&locale=en-US HTTP/2
            Host: www.crunchyroll.com
            User-Agent: __REDACTED__
            Accept: application/json, text/plain, */*
            Accept-Language: en-US,en;q=0.9
            Accept-Encoding: gzip, deflate, br, zstd
            Authorization: Bearer __REDACTED__
            Sec-GPC: 1
            Connection: keep-alive
            Referer: https://www.crunchyroll.com/videos/new
            Cookie: __REDACTED__
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            TE: trailers
        """
        params: dict[str, str | int] = {
            "n": n,
            "sort_by": sort_by,
            "ratings": ratings,
            "locale": locale or self._client.locale,
        }

        if start:
            params["start"] = start

        headers = {"referer": "https://www.crunchyroll.com/videos/new"}

        return self._client.download(
            "content/v2/discover/browse",
            params=params,
            headers=headers,
            log_id=f"{self.__class__.__name__} {start}",
        )

    @staticmethod
    @override
    def has_content(response: dict[str, Any]) -> bool:
        return bool(response["data"])

    def get(
        self,
        *,
        start: int | None = None,
        n: int = 36,
        sort_by: str = "newly_added",
        ratings: str = "true",
        locale: str | None = None,
    ) -> BrowseModel:
        """Downloads and parses the browse file."""
        data = self.download(
            n=n,
            sort_by=sort_by,
            locale=locale,
            start=start,
            ratings=ratings,
        )
        return self._parse_or_raise(data, f"{self.__class__.__name__} {start}")

    def get_since_datetime(
        self,
        end_datetime: datetime | None = None,
        *,
        n: int = 36,
        locale: str | None = None,
        sort_by: str = "newly_added",
        ratings: str = "true",
    ) -> list[BrowseModel]:
        """Downloads all browse pages until end_datetime is reached (inclusive)."""
        start = 0
        all_data: list[BrowseModel] = []
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
            start += n

            if result.data[-1].last_public < end_datetime or start >= result.total:
                return all_data

    def compile_entries(
        self,
        input_data: BrowseModel | list[BrowseModel],
    ) -> list[Datum]:
        """Compile all of the Browse entries into a single list of Datums."""
        if isinstance(input_data, list):
            result: list[Datum] = []
            for response in input_data:
                result.extend(self.compile_entries(response))
            return result

        return input_data.data
