# ruff: noqa: D100, D101
from pydantic import AwareDatetime, BaseModel, ConfigDict


class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_notation: str
    text_notation: str


class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    height: int
    source: str
    type: str
    width: int


class Images(BaseModel):
    model_config = ConfigDict(extra="forbid")
    thumbnail: list[list[ThumbnailItem]]


class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra="forbid")
    level: str
    rating: str
    system: str


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


class AdBreak(BaseModel):
    model_config = ConfigDict(extra="forbid")
    offset_ms: int
    type: str


class Datum(BaseModel):
    model_config = ConfigDict(extra="forbid")
    season_title: str
    is_clip: bool
    availability_notes: str
    closed_captions_available: bool
    language_presentation: LanguagePresentation
    availability_starts: AwareDatetime
    seo_title: str
    is_subbed: bool
    recent_audio_locale: str
    upload_date: AwareDatetime
    slug: str
    description: str
    is_mature: bool
    season_slug_title: str
    images: Images
    production_episode_id: str
    extended_maturity_rating: ExtendedMaturityRating
    channel_id: str
    roles: list[str]
    free_available_date: AwareDatetime
    mature_blocked: bool
    subtitle_locales: list[str]
    title: str
    duration_ms: int
    audio_locale: str
    media_type: str
    season_id: str
    availability_status: str
    identifier: str
    season_sequence_number: int
    premium_date: None
    listing_id: str
    sequence_number: int
    series_id: str
    availability_ends: AwareDatetime
    next_episode_title: str
    eligible_region: str
    available_date: None
    series_slug_title: str
    episode_number: int
    hd_flag: bool
    series_title: str
    content_descriptors: list[str]
    versions: list[Version]
    recent_variant: str
    seo_description: str
    season_display_number: str
    maturity_ratings: list[str]
    season_tags: list[str]
    season_number: int
    is_premium_only: bool
    premium_available_date: AwareDatetime
    is_dubbed: bool
    slug_title: str
    ad_breaks: list[AdBreak]
    episode: str
    id: str
    next_episode_id: str
    episode_air_date: AwareDatetime
    available_offline: bool


class Meta(BaseModel):
    model_config = ConfigDict(extra="forbid")
    versions_considered: bool | None = None


class Params(BaseModel):
    model_config = ConfigDict(extra="forbid")
    locale: str


class Headers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    referer: str


class Chirashi(BaseModel):
    model_config = ConfigDict(extra="forbid")
    params: Params
    headers: Headers
    url: str
    timestamp: AwareDatetime


class Episodes(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: int
    data: list[Datum]
    meta: Meta
    chirashi: Chirashi
