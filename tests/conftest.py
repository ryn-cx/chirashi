# TODO: Validate
import pytest
from get_around import build_client_automatically

from chirashi import Chirashi


@pytest.fixture(scope="session")
def client() -> Chirashi:
    return Chirashi(build_client_automatically())
