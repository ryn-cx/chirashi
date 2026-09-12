# TODO: Validate
from __future__ import annotations

import pytest
from get_around import build_client_automatically

from chirashi import Chirashi


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> Chirashi:
    # Every test downloads, so a run without a way out skips rather than fails.
    try:
        get_around_client = build_client_automatically()
    except RuntimeError as error:
        pytest.skip(f"No credentials to download with: {error}")
    return Chirashi(get_around_client)
