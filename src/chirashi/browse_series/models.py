# ruff: noqa: D100, D101
from typing import Any

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra="forbid")
    level: str | None = None
    rating: str | None = None
    system: str | None = None
    advisories: list[None] | None = None


class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_notation: str
    text_notation: str


class Award(BaseModel):
    model_config = ConfigDict(extra="forbid")
    icon_url: str
    is_current_award: bool
    is_winner: bool
    text: str


class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str


class SeriesMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_locales: list[str]
    availability_notes: str
    content_descriptors: list[str] | None = None
    episode_count: int
    extended_description: str
    extended_maturity_rating: ExtendedMaturityRating
    is_dubbed: bool
    is_mature: bool
    is_simulcast: bool
    is_subbed: bool
    language_presentation: LanguagePresentation
    mature_blocked: bool
    maturity_ratings: list[str]
    season_count: int
    series_launch_year: int
    subtitle_locales: list[str]
    tenant_categories: list[str] | None = None
    awards: list[Award] | None = None
    availability_status: str | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = (
        None
    )
    linked_guid: str | None = None


class Field3s(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    percentage: int
    unit: str


class Field4s(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    percentage: int
    unit: str


class Field5s(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    percentage: int
    unit: str


class Field1s(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    percentage: int
    unit: str


class Field2s(BaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    percentage: int
    unit: str


class Rating(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field_3s: Field3s = Field(..., alias="3s")
    field_4s: Field4s = Field(..., alias="4s")
    field_5s: Field5s = Field(..., alias="5s")
    average: str
    total: int
    field_1s: Field1s = Field(..., alias="1s")
    field_2s: Field2s = Field(..., alias="2s")


class PosterTallItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    height: int
    source: str
    type: str
    width: int


class PosterWideItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    height: int
    source: str
    type: str
    width: int


class PromoImageItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    width: int
    height: int
    type: str
    source: str


class Images(BaseModel):
    model_config = ConfigDict(extra="forbid")
    poster_tall: list[list[PosterTallItem]]
    poster_wide: list[list[PosterWideItem]]
    promo_image: list[list[PromoImageItem]] | None = None


class Datum(BaseModel):
    model_config = ConfigDict(extra="forbid")
    channel_id: str
    title: str
    series_metadata: SeriesMetadata
    new: bool
    description: str
    external_id: str
    promo_description: str
    type: str
    slug: str
    rating: Rating
    slug_title: str
    images: Images
    promo_title: str
    id: str
    last_public: str
    linked_resource_key: str
    language_presentation: LanguagePresentation | None = None


class Params(BaseModel):
    model_config = ConfigDict(extra="forbid")
    n: int
    sort_by: str
    ratings: str
    locale: str
    start: int | None = None


class Headers(BaseModel):
    model_config = ConfigDict(extra="forbid")
    referer: str


class Chirashi(BaseModel):
    model_config = ConfigDict(extra="forbid")
    params: Params
    headers: Headers
    url: str
    timestamp: AwareDatetime


class BrowseSeries(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: int
    data: list[Datum]
    meta: dict[str, Any] | None = None
    chirashi: Chirashi
