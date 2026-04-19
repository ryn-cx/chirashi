# ruff: noqa: D100, D101
from pydantic import BaseModel, ConfigDict, Field, RootModel


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


class Images(BaseModel):
    model_config = ConfigDict(extra="forbid")
    poster_tall: list[list[PosterTallItem]]
    poster_wide: list[list[PosterWideItem]]


class Award(BaseModel):
    model_config = ConfigDict(extra="forbid")
    icon_url: str
    is_current_award: bool
    is_winner: bool
    text: str


class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra="forbid")
    level: str
    rating: str
    system: str


class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_notation: str
    text_notation: str


class SeriesMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    audio_locales: list[str]
    availability_notes: str
    awards: list[Award] | None = None
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
    tenant_categories: list[str]


class SearchMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    score: float


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


class Rating(BaseModel):
    model_config = ConfigDict(extra="forbid")
    total: int
    field_1s: Field1s = Field(..., alias="1s")
    field_2s: Field2s = Field(..., alias="2s")
    field_3s: Field3s = Field(..., alias="3s")
    field_4s: Field4s = Field(..., alias="4s")
    field_5s: Field5s = Field(..., alias="5s")
    average: str


class SearchSery(BaseModel):
    model_config = ConfigDict(extra="forbid")
    images: Images
    promo_title: str
    new: bool
    id: str
    title: str
    series_metadata: SeriesMetadata
    promo_description: str
    external_id: str
    linked_resource_key: str
    channel_id: str
    description: str
    search_metadata: SearchMetadata
    rating: Rating
    slug: str
    type: str
    slug_title: str


class SearchSeries(RootModel[list[SearchSery]]):
    root: list[SearchSery]
