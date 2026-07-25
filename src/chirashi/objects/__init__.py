"""Contains the Objects class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import Any, override

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.exceptions import EpisodeNotFoundError, ResourceNotFoundError
from chirashi.objects.models import ObjectsModel

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Objects(BaseEndpoint[ObjectsModel]):
    """Manage the objects file.

    Source: https://www.crunchyroll.com/watch/{object_id}/{slug}

    Example request: https://www.crunchyroll.com/watch/{object_id}/{slug}
        - GET /content/v2/cms/objects/{object_id}?
            - ratings=true&
            - locale=en-US
            - HTTP/2
        - Host: www.crunchyroll.com
        - User-Agent: __REDACTED__
        - Accept: application/json, text/plain, */*
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Authorization: Bearer __REDACTED__
        - Connection: keep-alive
        - Referer: https://www.crunchyroll.com/watch/{object_id}/{slug}
        - Cookie: __REDACTED__
        - Sec-Fetch-Dest: empty
        - Sec-Fetch-Mode: cors
        - Sec-Fetch-Site: same-origin
        - TE: trailers
    """

    _response_model = ObjectsModel

    @override
    def download(
        self,
        object_id: str,
        *,
        locale: str | None = None,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        try:
            return self._client.download(
                endpoint="content/v2/cms/objects/" + object_id,
                params={
                    "ratings": True,
                    "locale": locale or self._client.locale,
                },
                headers={"referer": f"https://www.crunchyroll.com/watch/{object_id}"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise EpisodeNotFoundError(
                object_id,
                err.status_code,
                err.response,
            ) from err

    @override
    def download_and_parse(
        self,
        object_id: str,
        *,
        locale: str | None = None,
    ) -> ObjectsModel:
        return self.parse(self.download(object_id, locale=locale))
