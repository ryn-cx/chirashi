"""Contains the Browse class."""

from __future__ import annotations

import json
from datetime import datetime
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.browse_series.models import BrowseSeriesModel, model_validate_json
from chirashi.exceptions import StartOutOfRangeError

if TYPE_CHECKING:
    from collections.abc import Sequence

    from chirashi.browse_series.models import Datum

logger = getLogger(__name__)
logger.addHandler(NullHandler())

N = 36


class Browse(BaseEndpoint):
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

    # TODO: Validate
    def __call__(
        self,
        *,
        start: int = 0,
        n: int = N,
        sort_by: str = "newly_added",
        ratings: str = "true",
        locale: str | None = None,
    ) -> BrowseSeriesModel:
        """Look the browse series up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(
            self.download(
                start=start,
                n=n,
                sort_by=sort_by,
                ratings=ratings,
                locale=locale,
            ),
            log_id,
        )

    # TODO: Validate
    def download(
        self,
        *,
        start: int = 0,
        n: int = N,
        sort_by: str = "newly_added",
        ratings: str = "true",
        locale: str | None = None,
    ) -> str:
        """Download the browse file."""
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

    # TODO: Validate
    def _validate_download(self, response: str, start: int) -> str:
        total = json.loads(response)["total"]
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
    ) -> list[str]:
        """Downloads all files until end_datetime is reached."""
        results: list[str] = []
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

            parsed = json.loads(page)
            last_public = datetime.fromisoformat(parsed["data"][-1]["last_public"])
            if last_public < end_datetime or start >= parsed["total"]:
                return results

    # TODO: Validate
    def download_merged_until_datetime(  # noqa: PLR0913 - Required to match API.
        self,
        end_datetime: datetime | None = None,
        *,
        start: int = 0,
        n: int = N,
        locale: str | None = None,
        sort_by: str = "newly_added",
        ratings: str = "true",
    ) -> str:
        """Download every page down to `end_datetime` as a single file.

        The pages are put together into one file holding every series the walk
        reached, which is that stretch of the catalogue written the way one page
        of it is, rather than the pages themselves.
        """
        return self.merge_pages(
            self.download_until_datetime(
                end_datetime,
                start=start,
                n=n,
                locale=locale,
                sort_by=sort_by,
                ratings=ratings,
            ),
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> BrowseSeriesModel:
        """Read a downloaded browse file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)

    # TODO: Validate
    def load_pages(self, datas: list[str]) -> list[BrowseSeriesModel]:
        """Read the pages `download_until_datetime` returns into their models."""
        return [self.load(data) for data in datas]

    def extract_data(
        self,
        input_data: BrowseSeriesModel | str | Sequence[BrowseSeriesModel | str],
    ) -> list[Datum]:
        """Extracts data entries from one or more files."""
        # A single file is text, which is itself a Sequence, so it is held apart
        # from a sequence of files.
        responses = (
            [input_data]
            if isinstance(input_data, (BrowseSeriesModel, str))
            else input_data
        )

        result: list[Datum] = []
        for response in responses:
            parsed = (
                response
                if isinstance(response, BrowseSeriesModel)
                else self.load(response)
            )
            result.extend(parsed.data)
        return result
