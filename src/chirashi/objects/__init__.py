"""Contains the Objects class."""

from __future__ import annotations

import json
from logging import NullHandler, getLogger
from typing import Any

from chirashi.base_api_endpoint import BaseEndpoint
from chirashi.exceptions import (
    ChirashiError,
    EpisodeNotFoundError,
    ResourceNotFoundError,
)
from chirashi.objects.models import ObjectsModel, model_validate_json

logger = getLogger(__name__)
logger.addHandler(NullHandler())


# TODO: Validate
def extract_object(response: str) -> dict[str, Any]:
    """Extract the object from the Objects response."""
    if data := json.loads(response)["data"]:
        return data[0]

    msg = "The response has no object in it"
    raise ChirashiError(msg)


class Objects(BaseEndpoint):
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

    # TODO: Validate
    def __call__(
        self,
        object_id: str,
        *,
        locale: str | None = None,
    ) -> ObjectsModel:
        """Download and parse the objects file."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(object_id, locale=locale), log_id)

    # TODO: Validate
    def download(
        self,
        object_id: str,
        *,
        locale: str | None = None,
    ) -> str:
        """Download the objects file."""
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

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> ObjectsModel:
        """Load a objects file into its model."""
        return model_validate_json(
            extract_object(data),
            log_id or self.default_log_id,
        )
