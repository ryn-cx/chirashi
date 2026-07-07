# TODO: Validate
"""Base API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING, override

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from chirashi.constants import FILES_PATH

if TYPE_CHECKING:
    from pathlib import Path

    from chirashi import Chirashi


class BaseEndpoint[T: GAPIBaseModel](GAPIClient[T]):
    """Base class for API endpoints."""

    def __init__(self, client: Chirashi) -> None:
        """Initialize the endpoint with the Chirashi client."""
        self._client = client
