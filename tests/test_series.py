# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from chirashi.exceptions import HTTPError
from tests.utils import assert_error, download_and_save, parse_json

if TYPE_CHECKING:
    from chirashi import Chirashi
    from chirashi.series import Series

SERIES_ID = "GG5H5XQX4"
INVALID_SERIES_ID = "GGGGGGGGG"


@pytest.fixture(scope="session")
def endpoint(client: Chirashi) -> Series:
    return client.series


class TestSeries:
    def test_download(self, endpoint: Series) -> None:
        download_and_save(
            endpoint,
            SERIES_ID,
            lambda: endpoint.download(SERIES_ID),
        )

    def test_parse(self, endpoint: Series) -> None:
        # TODO: assert the series id matches SERIES_ID (needs live data)
        data = parse_json(endpoint, SERIES_ID)
        assert data.data is not None

    def test_invalid_download(self, endpoint: Series) -> None:
        assert_error(
            endpoint,
            INVALID_SERIES_ID,
            lambda: endpoint.download(INVALID_SERIES_ID),
            HTTPError,
        )


@pytest.mark.parametrize("locale", [None, "fr-FR"])
def test_log_id(endpoint: Series, locale: str | None) -> None:
    kwargs: dict[str, str] = {} if locale is None else {"locale": locale}
    expected = f"Series series_id={SERIES_ID!r}"
    if locale is not None:
        expected += f" locale={locale!r}"
    assert endpoint.get_log_id(SERIES_ID, **kwargs) == expected
