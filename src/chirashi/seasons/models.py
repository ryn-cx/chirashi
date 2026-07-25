from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import ConfigDict
from typing import Any

class ExtendedMaturityRating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    system: str
    rating: str
    level: str

class ContentDescriptorsWithSymbolItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    label: str

class Version(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    audio_locale: str
    guid: str
    original: bool
    variant: str

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    channel_id: str
    title: str
    slug_title: str
    series_id: str
    season_display_number: str
    season_sequence_number: int
    season_number: int
    is_complete: bool
    description: str
    keywords: list[str]
    season_tags: list[str]
    images: dict[str, Any]
    extended_maturity_rating: ExtendedMaturityRating
    maturity_ratings: list[str]
    content_descriptors: list[str]
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    is_mature: bool
    mature_blocked: bool
    is_subbed: bool
    is_dubbed: bool
    is_simulcast: bool
    seo_title: str
    seo_description: str
    availability_notes: str
    audio_locales: list[str]
    subtitle_locales: list[str]
    audio_locale: str
    versions: list[Version]
    identifier: str
    number_of_episodes: int

class Meta(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    versions_considered: bool

class SeasonsModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum]
    meta: Meta
    total: int
