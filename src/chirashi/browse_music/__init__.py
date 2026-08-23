# TODO: Validate
"""Contains the BrowseMusic class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.browse_music.models import BrowseMusicModel, model_validate_json
from chirashi.exceptions import StartOutOfRangeError

if TYPE_CHECKING:
    from collections.abc import Sequence

    from chirashi.browse_music.models import Datum

logger = getLogger(__name__)
logger.addHandler(NullHandler())

N = 36


class BrowseMusic(BaseEndpoint):
    """Endpoint contraining information about the entire music catalogue.

    Warning: This endpoint does not appear to actually used on the Crunchyroll website.
    """

    # TODO: Validate
    def __call__(
        self,
        *,
        start: int = 0,
        n: int = N,
        locale: str | None = None,
    ) -> BrowseMusicModel:
        """Look the browse music up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(start=start, n=n, locale=locale), log_id)

    # TODO: Validate
    def download(
        self,
        *,
        start: int = 0,
        n: int = N,
        locale: str | None = None,
    ) -> str:
        """Download the music catalogue file."""
        log_id = self.get_log_id(self.download, locals())
        params: dict[str, str | int] = {
            "n": n,
            "locale": locale or self._client.locale,
        }

        if start:
            params["start"] = start

        response = self._client.download(
            "content/v2/music/browse",
            params=params,
            headers={"referer": "https://www.crunchyroll.com/music"},
            log_id=log_id,
        )
        return self._validate_download(response, start)

    # TODO: Validate
    def _validate_download(self, response: str, start: int) -> str:
        # A start past the end of the catalogue is answered with an empty page
        # and a total of 0 rather than an error, so it has to be caught here.
        total = json.loads(response)["total"]
        if start and start > total:
            raise StartOutOfRangeError(start, total, response)
        return response

    def download_all(
        self,
        *,
        n: int = N,
        locale: str | None = None,
    ) -> list[str]:
        """Downloads every page of the music catalogue."""
        results: list[str] = []
        start = 0

        while True:
            page = self.download(start=start, n=n, locale=locale)
            results.append(page)
            start += n
            if start >= json.loads(page)["total"]:
                return results

    # TODO: Validate
    def download_merged(
        self,
        *,
        n: int = N,
        locale: str | None = None,
    ) -> str:
        """Download the whole music catalogue as a single file.

        The pages are put together into one file holding every artist, which is
        the whole catalogue written the way one page of it is, rather than the
        pages themselves.
        """
        return self.merge_pages(self.download_all(n=n, locale=locale))

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> BrowseMusicModel:
        """Read a downloaded music catalogue file into its model."""
        return model_validate_json(data, log_id or type(self).__name__)

    # TODO: Validate
    def load_pages(self, datas: list[str]) -> list[BrowseMusicModel]:
        """Read the pages `download_all` returns into their models."""
        return [self.load(data) for data in datas]

    def extract_data(
        self,
        input_data: BrowseMusicModel | str | Sequence[BrowseMusicModel | str],
    ) -> list[Datum]:
        """Extracts data entries from one or more files."""
        # A single file is text, which is itself a Sequence, so it is held apart
        # from a sequence of files.
        responses = (
            [input_data]
            if isinstance(input_data, (BrowseMusicModel, str))
            else input_data
        )

        result: list[Datum] = []
        for response in responses:
            parsed = (
                response
                if isinstance(response, BrowseMusicModel)
                else self.load(response)
            )
            result.extend(parsed.data)
        return result
