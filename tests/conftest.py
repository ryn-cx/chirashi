# TODO: Validate
from __future__ import annotations

import pytest
from get_around import build_client_automatically

from chirashi import Chirashi

pytest.register_assert_rewrite("tests.utils")


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> Chirashi:
    # Recording needs a way out; a run that only reads what is already recorded
    # needs none, so a missing one skips rather than fails.
    try:
        get_around_client = build_client_automatically()
    except RuntimeError as error:
        pytest.skip(f"No credentials to download with: {error}")
    return Chirashi(get_around_client)
