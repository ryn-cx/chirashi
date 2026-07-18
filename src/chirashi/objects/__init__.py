"""Contains the Objects class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.objects.models import ObjectsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Objects(BaseEndpoint[ObjectsModel]):
    """Manage the objects file."""

    _response_model = ObjectsModel

    def get_log_id(self, object_id: str, *, locale: str | None = None) -> str:
        """Build the log id for a download."""
        return self.append_non_default_args(
            f"{self.__class__.__name__} {object_id=}",
            locale=(locale, None),
        )

    def download(
        self,
        object_id: str,
        *,
        locale: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the objects file.

        Example request: https://www.crunchyroll.com/watch/GE00258180JAJP/the-magic-that-started-everything
            GET /content/v2/cms/objects/GE00258180JAJP?ratings=true&locale=en-US HTTP/2
            Host: www.crunchyroll.com
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0
            Accept: application/json, text/plain, */*
            Accept-Language: en-US,en;q=0.9
            Accept-Encoding: gzip, deflate, br, zstd
            Authorization: Bearer __REDACTED__
            Connection: keep-alive
            Referer: https://www.crunchyroll.com/watch/GE00258180JAJP/the-magic-that-started-everything
            Cookie: __REDACTED__
            Sec-Fetch-Dest: empty
            Sec-Fetch-Mode: cors
            Sec-Fetch-Site: same-origin
            TE: trailers
        """
        return self._client.download(
            endpoint="content/v2/cms/objects/" + object_id,
            params={
                "ratings": True,
                "locale": locale or self._client.locale,
            },
            headers={"referer": f"https://www.crunchyroll.com/watch/{object_id}"},
            log_id=self.get_log_id(object_id, locale=locale),
        )

    def download_and_parse(
        self,
        object_id: str,
        *,
        locale: str | None = None,
    ) -> ObjectsModel:
        """Downloads and parses the objects file."""
        return self.parse(self.download(object_id, locale=locale))
