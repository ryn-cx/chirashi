"""Contains the Objects class."""

from __future__ import annotations

from typing import Any

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.objects.models import ObjectsModel


class Objects(BaseEndpoint[ObjectsModel]):
    """Manage the objects file."""

    _response_model = ObjectsModel

    def download(
        self,
        object_ids: list[str],
        *,
        locale: str | None = None,
    ) -> dict[str, Any]:
        """Downloads the objects file.

        Multiple object ids are fetched in a single request by joining them with
        commas (e.g. ``/objects/GE00258180JAJP,GEXH3W29Z``).

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
        joined_ids = ",".join(object_ids)
        return self._client.download(
            endpoint="content/v2/cms/objects/" + joined_ids,
            params={
                "ratings": True,
                "locale": locale or self._client.locale,
            },
            headers={"referer": f"https://www.crunchyroll.com/watch/{object_ids[0]}"},
            log_id=f"{self.__class__.__name__} {joined_ids}",
        )

    def get(self, object_ids: list[str], *, locale: str | None = None) -> ObjectsModel:
        """Downloads and parses the objects file."""
        data = self.download(object_ids, locale=locale)
        joined_ids = ",".join(object_ids)
        return self._parse_or_raise(data, f"{self.__class__.__name__} {joined_ids}")
