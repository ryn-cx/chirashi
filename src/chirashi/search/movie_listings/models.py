# ruff: noqa: D100, D101
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, RootModel


class SearchMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    score: float


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


class AdBreak(BaseModel):
    model_config = ConfigDict(extra="forbid")
    offset_ms: int
    type: str


class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra="forbid")
    level: str
    rating: str
    system: str


class MovieListingMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ad_breaks: list[AdBreak]
    availability_notes: str
    availability_status: str
    available_date: None
    available_offline: bool
    content_descriptors: list[str]
    duration_ms: int
    extended_description: str
    extended_maturity_rating: ExtendedMaturityRating
    first_movie_id: str
    free_available_date: AwareDatetime
    is_dubbed: bool
    is_mature: bool
    is_premium_only: bool
    is_subbed: bool
    mature_blocked: bool
    maturity_ratings: list[str]
    movie_release_year: int
    premium_available_date: AwareDatetime
    premium_date: None
    subtitle_locales: list[None]
    tenant_categories: list[str]


class SearchMovieListingItem(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    slug: str
    new: bool
    id: str
    type: str
    search_metadata: SearchMetadata
    description: str
    images: Images
    promo_title: str
    promo_description: str
    external_id: str
    linked_resource_key: str
    channel_id: str
    rating: Rating
    slug_title: str
    movie_listing_metadata: MovieListingMetadata


class SearchMovieListing(RootModel[list[SearchMovieListingItem]]):
    root: list[SearchMovieListingItem]
