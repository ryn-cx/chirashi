# TODO: Validate
"""Contains BaseEndpoint."""

from __future__ import annotations

from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

from chirashi.constants import FILES_PATH

if TYPE_CHECKING:
    from chirashi import Chirashi


class BaseEndpoint[T: GAPIBaseModel](GAPIClient[T]):
    """Base class for API endpoints."""

    JSON_FILES_ROOT = FILES_PATH

    def __init__(self, client: Chirashi) -> None:
        """Initialize the endpoint."""
        self._client = client

    @staticmethod
    def append_non_default_args(
        log_id: str,
        **args: tuple[object, object],
    ) -> str:
        """Append ``name=value`` for each arg whose value differs from its default."""
        for name, (value, default) in args.items():
            if value != default:
                log_id += f" {name}={value!r}"
        return log_id
