"""Search movie listings GAPIClient."""

from __future__ import annotations

from typing import TYPE_CHECKING, override

from good_ass_pydantic_integrator import GAPIClient

from chirashi.constants import FILES_PATH
from chirashi.search.movie_listings.models import (
    SearchMovieListing as SearchMovieListingModel,
)

if TYPE_CHECKING:
    from pathlib import Path


class SearchMovieListing(GAPIClient[SearchMovieListingModel]):
    """GAPIClient for search movie listing items."""

    _response_model = SearchMovieListingModel

    @override
    @classmethod
    def json_files_folder(cls) -> Path:
        folder_name = cls._to_folder_name(cls._get_model_name())
        return FILES_PATH / folder_name
