# TODO: Validate
from __future__ import annotations

from datetime import datetime, timedelta
from typing import TYPE_CHECKING

from chirashi.browse_series import N
from chirashi.browse_series.models import BrowseSeriesModel
from chirashi.exceptions import StartOutOfRangeError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from chirashi import Chirashi


# TODO: Validate
class BrowseSeriesTest(RecordedEndpoint):
    MODEL = BrowseSeriesModel


# TODO: Validate
def test_download(client: Chirashi) -> None:
    BrowseSeriesTest.download_test(0, lambda: client.browse_series.download(start=0))


# TODO: Validate
def test_download_until_datetime(client: Chirashi) -> None:
    end_datetime = datetime.now().astimezone() - timedelta(days=7)
    BrowseSeriesTest.download_test(
        "until_datetime",
        lambda: client.browse_series.download_until_datetime(end_datetime),
        "Multipage",
    )


# TODO: Validate
def test_download_invalid(client: Chirashi) -> None:
    BrowseSeriesTest.error_test(
        9999,
        lambda: client.browse_series.download(start=9999),
        StartOutOfRangeError,
    )


# TODO: Validate
def test_parse() -> None:
    BrowseSeriesTest.parse_test(0)


# TODO: Validate
def test_parse_until_datetime() -> None:
    BrowseSeriesTest.parse_test("until_datetime", "Multipage")


# TODO: Validate
def test_extract_data(client: Chirashi) -> None:
    loaded = BrowseSeriesTest.recorded_documents(0)
    extracted_loaded = client.browse_series.extract_data(loaded)

    data = client.browse_series.load(BrowseSeriesTest.recorded_content(0))
    extracted_data = client.browse_series.extract_data(data)
    assert extracted_data == extracted_loaded
    assert len(extracted_data) == N


# TODO: Validate
def test_extract_data_until_datetime(client: Chirashi) -> None:
    loaded = BrowseSeriesTest.recorded_documents("until_datetime", category="Multipage")
    extracted_loaded = client.browse_series.extract_data(loaded)

    data = [
        client.browse_series.load(page)
        for page in BrowseSeriesTest.recorded_documents("until_datetime", "Multipage")
    ]
    extracted_data = client.browse_series.extract_data(data)
    assert extracted_data == extracted_loaded
    assert len(extracted_data) == len(loaded) * N
