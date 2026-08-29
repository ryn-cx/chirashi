"""Contains the BaseSearch class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING

from pydantic import BaseModel

from chirashi.base_api_endpoint import BaseEndpoint

if TYPE_CHECKING:
    from collections.abc import Callable

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class BaseSearch[T: BaseModel](BaseEndpoint):
    """Base class to manage a search file with a specific type.

    Source: https://www.crunchyroll.com/search?f={type}&q={query}

    Example request:
        - GET /content/v2/discover/search?
            - q={query}&
            - n=100&
            - type={type}&
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
        - Referer: https://www.crunchyroll.com/search?f={type}&q={query}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    MODEL: type[T]
    """The model this search reads its responses with."""

    LOAD: Callable[[str | bytes | object, str], T]
    """The `model_validate_json` its model's module generates."""

    search_type: str
    n: int = 100

    def _download(
        self,
        q: str,
        *,
        n: int | None,
        search_type: str | None,
        ratings: bool,
        locale: str | None,
    ) -> str:
        log_id = self.get_log_id(self.download, locals())
        return self._client.download(
            "content/v2/discover/search",
            params={
                "q": q,
                "n": self.n if n is None else n,
                "type": search_type or self.search_type,
                "ratings": str(ratings).lower(),
                "locale": locale or self._client.locale,
            },
            headers={"referer": "https://www.crunchyroll.com/search"},
            log_id=log_id,
        )

    # TODO: Validate
    def __call__(
        self,
        q: str,
        *,
        n: int | None = None,
        ratings: bool = True,
        locale: str | None = None,
    ) -> T:
        """Run the search and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(q, n=n, ratings=ratings, locale=locale), log_id)

    # TODO: Validate
    def download(
        self,
        q: str,
        *,
        n: int | None = None,
        ratings: bool = True,
        locale: str | None = None,
    ) -> str:
        """Download the search file."""
        return self._download(
            q,
            n=n,
            search_type=None,
            ratings=ratings,
            locale=locale,
        )

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> T:
        """Read a downloaded search file into its model."""
        return type(self).LOAD(data, log_id or self.default_log_id)
