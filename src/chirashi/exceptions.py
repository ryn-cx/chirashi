# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


class ChirashiError(Exception):
    """Base exception for Chirashi."""


class HTTPError(ChirashiError):
    """Raised when HTTP request fails with unexpected status code."""


class NoContentError(ChirashiError):
    """Raised when a response has no meaningful content."""

    def __init__(
        self,
        response: dict[str, Any],
        log_id: str,
    ) -> None:
        """Store the downloaded response so it can be recovered by the caller."""
        self.response = response
        super().__init__(f"Response has no content for {log_id}.")
