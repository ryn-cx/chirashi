# TODO: Validate
from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, override

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from chirashi.constants import FILES_PATH
from chirashi.exceptions import NoContentError

if TYPE_CHECKING:
    from pathlib import Path

    from chirashi import Chirashi


class BaseEndpoint[T: GAPIBaseModel](GAPIClient[T]):
    """Base class for API endpoints."""

    def __init__(self, client: Chirashi) -> None:
        """Initialize the endpoint with the Chirashi client."""
        self._client = client

    @staticmethod
    @abstractmethod
    def has_content(*args: Any, **kwargs: Any) -> bool:  # noqa: ANN401
        """Return whether the response has meaningful content."""

    def _parse_or_raise(self, response: dict[str, Any], *, has_content: bool) -> T:
        """Parse `response`, or raise `NoContentError` when it is empty.

        This is the single place `get` decides "nothing here". The raised
        `NoContentError` carries `response`, so callers can still recover the
        downloaded payload from the exception.

        Args:
            response: The raw JSON response to parse.
            has_content: The endpoint's `has_content` verdict for `response`.

        Returns:
            The parsed model.

        Raises:
            NoContentError: If `has_content` is false.
        """
        if not has_content:
            raise NoContentError(response, endpoint=type(self).__name__)
        return self.parse(response)
