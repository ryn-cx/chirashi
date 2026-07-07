# TODO: Validate
"""Base class for the per-category search item GAPIClients."""

from __future__ import annotations

from typing import TYPE_CHECKING, override

from good_ass_pydantic_integrator import GAPIClient
from pydantic import RootModel

from chirashi.constants import FILES_PATH

if TYPE_CHECKING:
    from pathlib import Path


class BaseSearchEndpoint[T: RootModel](GAPIClient[T]):
    """Base class for search item GAPIClients.

    Each concrete subclass parses one category's list of items extracted from a
    search response. Unlike ``BaseEndpoint`` these clients are used via
    classmethods only and are never instantiated with a Chirashi client, so they
    take no ``__init__``.
    """

    @override
    @classmethod
    def json_files_folder(cls) -> Path:
        folder_name = cls._folder_name(cls._model_name())
        return FILES_PATH / folder_name
