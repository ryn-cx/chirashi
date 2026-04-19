# ruff: noqa: D100, D101
from pydantic import AwareDatetime, BaseModel, ConfigDict, RootModel


class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    height: int
    source: str
    type: str
    width: int


class Images(BaseModel):
    model_config = ConfigDict(extra="forbid")
    thumbnail: list[list[ThumbnailItem]]


class Up(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    unit: str


class Down(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    unit: str


class Rating(BaseModel):
    model_config = ConfigDict(extra="forbid")
    up: Up
    down: Down
    total: int


class AdBreak(BaseModel):
    model_config = ConfigDict(extra="forbid")
    offset_ms: int
    type: str


class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra="forbid")
    level: str
    rating: str
    system: str


class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_notation: str
    text_notation: str


class Version(BaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_locale: str
    guid: str
    is_premium_only: bool
    media_guid: str
    original: bool
    roles: list[str]
    season_guid: str
    variant: str


class EpisodeMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ad_breaks: list[AdBreak]
    audio_locale: str
    availability_ends: AwareDatetime
    availability_notes: str
    availability_starts: AwareDatetime
    availability_status: str
    available_date: None
    available_offline: bool
    closed_captions_available: bool
    content_descriptors: list[str]
    duration_ms: int
    eligible_region: str
    episode: str
    episode_air_date: AwareDatetime
    episode_number: int
    extended_maturity_rating: ExtendedMaturityRating
    free_available_date: AwareDatetime
    identifier: str
    is_clip: bool
    is_dubbed: bool
    is_mature: bool
    is_premium_only: bool
    is_subbed: bool
    language_presentation: LanguagePresentation
    mature_blocked: bool
    maturity_ratings: list[str]
    premium_available_date: AwareDatetime
    premium_date: None
    roles: list[str]
    season_display_number: str
    season_id: str
    season_number: int
    season_sequence_number: int
    season_slug_title: str
    season_title: str
    sequence_number: int
    series_id: str
    series_slug_title: str
    series_title: str
    subtitle_locales: list[str]
    tenant_categories: list[str]
    upload_date: AwareDatetime
    versions: list[Version]


class SearchMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    score: float


class SearchEpisodeItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    linked_resource_key: str
    slug_title: str
    channel_id: str
    images: Images
    id: str
    promo_description: str
    rating: Rating
    external_id: str
    title: str
    description: str
    slug: str
    episode_metadata: EpisodeMetadata
    new: bool
    promo_title: str
    type: str
    search_metadata: SearchMetadata


class SearchEpisode(RootModel[list[SearchEpisodeItem]]):
    root: list[SearchEpisodeItem]
