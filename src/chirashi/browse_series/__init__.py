"""Contains the Browse class."""

from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, override

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.browse_series.models import BrowseSeriesModel
from chirashi.exceptions import StartOutOfRangeError

if TYPE_CHECKING:
    from chirashi.browse_series.models import Datum

logger = getLogger(__name__)
logger.addHandler(NullHandler())

N = 36


class Browse(BaseEndpoint[BrowseSeriesModel]):
    """Manage the browse file.

    Source: https://www.crunchyroll.com/videos/new

    Example request:
        - GET /content/v2/discover/browse?
            - n=36&
            - sort_by=newly_added&
            - ratings=true&
            - locale=en-US
            - HTTP/2
        - Host: www.crunchyroll.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/plain, */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Authorization: Bearer __REDACTED__
        - Sec-GPC: 1
        - Connection: keep-alive
        - Referer: https://www.crunchyroll.com/videos/new
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    _response_model = BrowseSeriesModel

    @override
    def download(
        self,
        *,
        start: int = 0,
        n: int = N,
        sort_by: str = "newly_added",
        ratings: str = "true",
        locale: str | None = None,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        params: dict[str, str | int] = {
            "n": n,
            "sort_by": sort_by,
            "ratings": ratings,
            "locale": locale or self._client.locale,
        }

        if start:
            params["start"] = start

        response = self._client.download(
            "content/v2/discover/browse",
            params=params,
            headers={"referer": "https://www.crunchyroll.com/videos/new"},
            log_id=log_id,
        )
        return self._validate_download(response, start)

    def _validate_download(
        self,
        response: dict[str, Any],
        start: int,
    ) -> dict[str, Any]:
        total = response["total"]
        if start and start > total:
            raise StartOutOfRangeError(start, total, response)
        return response

    def download_until_datetime(  # noqa: PLR0913 - Required to match API.
        self,
        end_datetime: datetime | None = None,
        *,
        start: int = 0,
        n: int = N,
        locale: str | None = None,
        sort_by: str = "newly_added",
        ratings: str = "true",
    ) -> list[dict[str, Any]]:
        """Downloads all files until end_datetime is reached."""
        results: list[dict[str, Any]] = []
        end_datetime = end_datetime or datetime.now().astimezone()

        while True:
            page = self.download(
                n=n,
                locale=locale,
                start=start,
                sort_by=sort_by,
                ratings=ratings,
            )
            results.append(page)
            start += n

            last_public = datetime.fromisoformat(page["data"][-1]["last_public"])
            if last_public < end_datetime or start >= page["total"]:
                return results

    def parse_until_datetime(
        self,
        datas: list[dict[str, Any]],
    ) -> list[BrowseSeriesModel]:
        """Parses the output of download_until_datetime."""
        return [self.parse(data) for data in datas]

    @override
    def download_and_parse(
        self,
        *,
        start: int = 0,
        n: int = N,
        sort_by: str = "newly_added",
        ratings: str = "true",
        locale: str | None = None,
    ) -> BrowseSeriesModel:
        response = self.download(
            start=start,
            n=n,
            sort_by=sort_by,
            ratings=ratings,
            locale=locale,
        )
        return self.parse(response)

    def download_and_parse_until_datetime(
        self,
        end_datetime: datetime | None = None,
        *,
        n: int = N,
        locale: str | None = None,
        sort_by: str = "newly_added",
        ratings: str = "true",
    ) -> list[BrowseSeriesModel]:
        """Downloads and parses all files until end_datetime is reached."""
        responses = self.download_until_datetime(
            end_datetime,
            n=n,
            locale=locale,
            sort_by=sort_by,
            ratings=ratings,
        )
        return self.parse_until_datetime(responses)

    def extract_data(
        self,
        input_data: BrowseSeriesModel
        | dict[str, Any]
        | Sequence[BrowseSeriesModel | dict[str, Any]],
    ) -> list[Datum]:
        """Extracts data entries from one or more files."""
        responses = input_data if isinstance(input_data, Sequence) else [input_data]

        result: list[Datum] = []
        for response in responses:
            parsed = (
                response
                if isinstance(response, BrowseSeriesModel)
                else self.parse(response)
            )
            result.extend(parsed.data)
        return result
