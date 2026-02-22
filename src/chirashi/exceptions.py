"""Exception classes for chirashi."""


class ChirashiError(Exception):
    """Base exception for chirashi library."""


class HTTPError(ChirashiError):
    """Raised when HTTP request fails with unexpected status code."""
