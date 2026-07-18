# TODO: Validate
"""Exceptions."""

from __future__ import annotations


class ChirashiError(Exception):
    """Base exception for Chirashi."""


class HTTPError(ChirashiError):
    """Raised when HTTP request fails with unexpected status code."""
