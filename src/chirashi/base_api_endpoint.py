# TODO: Validate
"""Contains BaseEndpoint."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from chirashi.constants import FILES_PATH
from chirashi.exceptions import NoContentError

if TYPE_CHECKING:
    from chirashi import Chirashi


class BaseEndpoint[T: GAPIBaseModel](GAPIClient[T]):
    """Base class for API endpoints."""

    JSON_FILES_ROOT = FILES_PATH

    def __init__(self, client: Chirashi) -> None:
        """Initialize the endpoint."""
        self._client = client

    @staticmethod
    @abstractmethod
    def has_content(*args: Any, **kwargs: Any) -> bool:  # noqa: ANN401
        """Return whether the response has meaningful content."""

    def _parse_or_raise(self, response: dict[str, Any], log_id: str) -> T:
        """Parse `response`, or raise `NoContentError` if it is empty.

        Raises:
            NoContentError: If `has_content` is false.
        """
        if not self.has_content(response):
            raise NoContentError(response, log_id)
        return self.parse(response)
