# TODO: Validate
"""Contains BaseEndpoint."""

from __future__ import annotations

import json
from inspect import Parameter, signature
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

    from chirashi import Chirashi


# TODO: Validate
class BaseEndpoint:
    """Base class for API endpoints."""

    WEBSITE = "Crunchyroll"

    # TODO: Validate
    @property
    def default_log_id(self) -> str:
        """Get the log id of the endpoint itself, without any arguments."""
        return f"{self.WEBSITE} - {self.__class__.__name__}"

    def __init__(self, client: Chirashi) -> None:
        """Initialize the endpoint with the Chirashi client."""
        self._client = client

    # TODO: Validate
    @staticmethod
    def merge_pages(pages: list[str]) -> str:
        """Return the pages of one listing written out as a single file.

        The first page is what the merged file is built on, since its total is
        the size of the whole listing, and its data is replaced by the data of
        every page in the order they were served.

        Raises:
            ValueError: If there are no pages, since there is nothing to say the
                listing was answered with.
        """
        if not pages:
            msg = "Expected at least one page, got none."
            raise ValueError(msg)

        documents: list[dict[str, Any]] = [json.loads(page) for page in pages]
        merged = dict(documents[0])
        merged["data"] = [
            item for document in documents for item in document.get("data", ())
        ]
        return json.dumps(merged)

    @staticmethod
    def non_default_args(
        func: Callable[..., Any],
        values: dict[str, Any],
    ) -> dict[str, Any]:
        """Return the args that are changed from their default values."""
        return {
            name: values[name]
            for name, param in signature(func).parameters.items()
            if param.default is not Parameter.empty
            and name in values
            and values[name] != param.default
        }

    # TODO: Validate
    def get_log_id(self, func: Callable[..., Any], values: dict[str, Any]) -> str:
        """Get the log id.

        Example: Crunchyroll - ClassName (arg1='value1' arg2='value2')
        """
        required = {
            name: values[name]
            for name, param in signature(func).parameters.items()
            if param.default is Parameter.empty and name in values
        }
        set_args = {**required, **self.non_default_args(func, values)}
        parts = [
            *(f"{name}={value!r}" for name, value in set_args.items()),
        ]
        if not parts:
            return self.default_log_id
        return f"{self.default_log_id} ({' '.join(parts)})"
