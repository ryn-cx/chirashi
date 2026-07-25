"""Utils."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Literal, overload

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path
    from typing import Any

    from good_ass_pydantic_integrator import GAPIClient
    from pydantic import BaseModel

    from chirashi.base_api_endpoint import BaseEndpoint
    from chirashi.exceptions import ChirashiError


def json_path(
    gapi_client: GAPIClient[Any],
    name: str | int,
    category: Literal["Multipage", "Error"] | None = None,
) -> Path:
    if category:
        return (
            gapi_client.json_files_folder().parent
            / (category + "s")
            / gapi_client.json_files_folder().stem
            / f"{name}.json"
        )

    return gapi_client.json_files_folder() / f"{name}.json"


def json_content[T: BaseModel](
    gapi_client: BaseEndpoint[T, ...],
    name: str | int,
    category: Literal["Multipage", "Error"] | None = None,
) -> str:
    return json_path(gapi_client, name, category=category).read_text()


def loaded_json(
    gapi_client: BaseEndpoint[Any, ...],
    name: str | int,
    category: Literal["Multipage"] | None = None,
) -> dict[str, Any]:
    return json.loads(json_content(gapi_client, name, category=category))


@overload
def parsed_json[T: BaseModel](
    gapi_client: BaseEndpoint[T, ...],
    name: str | int,
    category: Literal["Multipage"],
) -> list[T]: ...
@overload
def parsed_json[T: BaseModel](
    gapi_client: BaseEndpoint[T, ...],
    name: str | int,
    category: None = None,
) -> T: ...
def parsed_json[T: BaseModel](
    gapi_client: BaseEndpoint[T, ...],
    name: str | int,
    category: Literal["Multipage"] | None = None,
) -> T | list[T]:
    data = json.loads(json_content(gapi_client, name, category=category))
    if category == "Multipage":
        return [gapi_client.parse(page) for page in data]
    return gapi_client.parse(data)


def download_and_save(
    gapi_client: GAPIClient[Any],
    name: str | int,
    get: Callable[[], dict[str, Any] | list[dict[str, Any]]],
    category: Literal["Multipage"] | None = None,
) -> Path:
    file = json_path(gapi_client, name, category)
    if file.exists():
        msg = f"File already recorded for {type(gapi_client).__name__}/{name}"
        pytest.skip(msg)  # ty: ignore[too-many-positional-arguments]
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(json.dumps(get(), indent=2))
    return file


def assert_error(
    gapi_client: GAPIClient[Any],
    name: str | int,
    download: Callable[[], object],
    error: type[ChirashiError],
) -> None:
    if json_path(gapi_client, name, "Error").exists():
        msg = f"File already recorded for {type(gapi_client).__name__}/{name}"
        pytest.skip(msg)  # ty: ignore[too-many-positional-arguments]
    with pytest.raises(error) as excinfo:
        download()
    record_error(gapi_client, name, excinfo.value.response)


def get_error_path(gapi_client: GAPIClient[Any], name: str | int) -> Path:
    return json_path(gapi_client, name, category="Error")


def record_error(
    gapi_client: GAPIClient[Any],
    name: str | int,
    response: str | dict[str, Any] | None = None,
) -> None:
    json_path = get_error_path(gapi_client, name)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    if response is None:
        content = ""
    elif isinstance(response, str):
        content = response
    else:
        content = json.dumps(response, indent=2)
    json_path.write_text(content)
