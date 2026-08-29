# TODO: Validate
"""Constants."""

from pathlib import Path

FILES_PATH = Path(__file__).parent / "_files"
"""Where the recorded responses live."""

IDS_PATH = Path(__file__).parent / "ids"
"""Where the ids each model's responses are recorded for live."""

CHIRASHI_PATH = Path(__file__).parent.parent / "src" / "chirashi"
"""The package the models are written into."""
