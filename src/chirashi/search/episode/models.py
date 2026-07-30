from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict
from typing import Any

class ThumbnailItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    width: int
    height: int
    type: str
    source: str

class Images(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    thumbnail: list[list[ThumbnailItem]] | None = None

class AdBreak(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    offset_ms: int

class ExtendedMaturityRating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    system: str
    rating: str
    level: str
    advisories: list[None]

class ContentDescriptorsWithSymbolItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    label: str

class Version(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    audio_locale: str
    guid: str
    original: bool
    variant: str
    season_guid: str
    media_guid: str
    is_premium_only: bool
    roles: list[str]

class LanguagePresentation(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    audio_notation: str
    text_notation: str

class EpisodeMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    series_id: str
    series_title: str
    series_slug_title: str
    season_id: str
    season_title: str
    season_slug_title: str
    season_number: int
    episode_number: int
    episode: str
    sequence_number: int
    season_display_number: str
    season_sequence_number: int
    duration_ms: int
    ad_breaks: list[AdBreak] | None = None
    episode_air_date: AwareDatetime
    upload_date: AwareDatetime
    availability_starts: AwareDatetime
    availability_ends: AwareDatetime
    eligible_region: str
    is_premium_only: bool
    extended_maturity_rating: ExtendedMaturityRating
    maturity_ratings: list[str]
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    is_mature: bool
    mature_blocked: bool
    available_date: None
    free_available_date: AwareDatetime
    premium_date: None
    premium_available_date: AwareDatetime
    is_subbed: bool
    is_dubbed: bool
    is_clip: bool
    available_offline: bool
    linked_guid: str
    tenant_categories: list[str]
    subtitle_locales: list[str]
    availability_notes: str
    audio_locale: str
    versions: list[Version]
    closed_captions_available: bool
    identifier: str
    availability_status: str
    roles: list[str]
    language_presentation: LanguagePresentation

class SearchMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    score: float
    rank: int
    popularity_score: int

class Up(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    displayed: str
    unit: str

class Down(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    displayed: str
    unit: str

class Rating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    up: Up
    down: Down
    total: int

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str
    external_id: str
    channel_id: str
    linked_resource_key: str
    new: bool
    title: str
    description: str
    promo_title: str
    promo_description: str
    type: str
    slug: str
    slug_title: str
    images: Images
    episode_metadata: EpisodeMetadata
    search_metadata: SearchMetadata
    language_presentation: LanguagePresentation
    rating: Rating

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    items: list[Item]
    count: int

class SearchEpisodeModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    data: list[Datum]
    total: int
    meta: dict[str, Any]
