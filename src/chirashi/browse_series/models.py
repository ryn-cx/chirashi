# ruff: noqa: D100, D101
from typing import Any

from good_ass_pydantic_integrator import GAPIBaseModel
from pydantic import AwareDatetime, ConfigDict, Field


class PosterTallItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    width: int
    height: int
    type: str
    source: str


class PosterWideItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    width: int
    height: int
    type: str
    source: str


class PromoImageItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    width: int
    height: int
    type: str
    source: str


class Images(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    poster_tall: list[list[PosterTallItem]]
    poster_wide: list[list[PosterWideItem]]
    promo_image: list[list[PromoImageItem]] | None = None


class ExtendedMaturityRating(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    system: str | None = None
    rating: str | None = None
    level: str | None = None
    advisories: list[None] | None = None


class ContentDescriptorsWithSymbolItem(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str


class LanguagePresentation(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_notation: str
    text_notation: str


class Award(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str
    icon_url: str
    is_current_award: bool
    is_winner: bool


class SeriesMetadata(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    availability_status: str | None = None
    extended_description: str
    episode_count: int
    season_count: int
    extended_maturity_rating: ExtendedMaturityRating
    maturity_ratings: list[str]
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = (
        None
    )
    is_mature: bool
    mature_blocked: bool
    is_subbed: bool
    is_dubbed: bool
    is_simulcast: bool
    linked_guid: str | None = None
    availability_notes: str
    audio_locales: list[str]
    subtitle_locales: list[str]
    series_launch_year: int
    tenant_categories: list[str] | None = None
    language_presentation: LanguagePresentation
    awards: list[Award] | None = None


class Field1s(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    unit: str
    percentage: int


class Field2s(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    unit: str
    percentage: int


class Field3s(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    unit: str
    percentage: int


class Field4s(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    unit: str
    percentage: int


class Field5s(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    displayed: str
    unit: str
    percentage: int


class Rating(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    field_1s: Field1s = Field(..., alias="1s")
    field_2s: Field2s = Field(..., alias="2s")
    field_3s: Field3s = Field(..., alias="3s")
    field_4s: Field4s = Field(..., alias="4s")
    field_5s: Field5s = Field(..., alias="5s")
    average: str
    total: int


class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
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
    last_public: AwareDatetime
    images: Images
    series_metadata: SeriesMetadata
    language_presentation: LanguagePresentation | None = None
    rating: Rating


class Params(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    n: int
    sort_by: str
    ratings: str
    locale: str
    start: int | None = None


class Headers(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    referer: str


class Chirashi(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    params: Params
    headers: Headers
    url: str
    timestamp: AwareDatetime


class BrowseSeries(GAPIBaseModel):
    model_config = ConfigDict(extra="forbid")
    data: list[Datum]
    total: int
    chirashi: Chirashi
    meta: dict[str, Any] | None = None
