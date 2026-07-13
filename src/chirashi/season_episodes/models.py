# ruff: noqa: D100, D101, D102, TC001, TC002, TC003
from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict


class ExtendedMaturityRating(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    system: str
    rating: str
    level: str


class Version(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_locale: str
    guid: str
    original: bool
    variant: str
    season_guid: str
    media_guid: str
    is_premium_only: bool
    roles: list[str]


class ContentDescriptorsWithSymbolItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str


class ThumbnailItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    width: int
    height: int
    type: str
    source: str


class Images(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    thumbnail: list[list[ThumbnailItem]]


class AdBreak(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    offset_ms: int


class LanguagePresentation(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_notation: str
    text_notation: str


class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    channel_id: str
    series_id: str
    series_title: str
    series_slug_title: str
    season_id: str
    season_title: str
    season_slug_title: str
    season_number: int
    episode: str
    episode_number: int
    sequence_number: int
    season_display_number: str
    season_sequence_number: int
    production_episode_id: str
    title: str
    slug_title: str
    description: str
    next_episode_id: str
    next_episode_title: str | None = None
    hd_flag: bool
    maturity_ratings: list[str]
    extended_maturity_rating: ExtendedMaturityRating
    is_mature: bool
    mature_blocked: bool
    episode_air_date: AwareDatetime
    upload_date: AwareDatetime
    availability_starts: AwareDatetime
    availability_ends: AwareDatetime
    eligible_region: str
    available_date: None
    free_available_date: AwareDatetime
    premium_date: None
    premium_available_date: AwareDatetime
    is_subbed: bool
    is_dubbed: bool
    is_clip: bool
    seo_title: str
    seo_description: str
    season_tags: list[None]
    available_offline: bool
    subtitle_locales: list[str]
    availability_notes: str
    audio_locale: str
    versions: list[Version]
    closed_captions_available: bool
    identifier: str
    content_descriptors: list[str]
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem]
    media_type: str
    slug: str
    images: Images
    duration_ms: int
    ad_breaks: list[AdBreak]
    is_premium_only: bool
    listing_id: str
    recent_audio_locale: str
    recent_variant: str
    availability_status: str
    language_presentation: LanguagePresentation
    roles: list[str]


class Meta(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    versions_considered: bool


class SeasonEpisodesModel(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    data: list[Datum]
    total: int
    meta: Meta
