from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class Field1s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    percentage: int | None = None
    unit: str | None = None

class Field2s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    percentage: int | None = None
    unit: str | None = None

class Field3s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    percentage: int | None = None
    unit: str | None = None

class Field4s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    percentage: int | None = None
    unit: str | None = None

class Field5s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    percentage: int | None = None
    unit: str | None = None

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_1s: Field1s | None = Field(None, alias='1s')
    field_2s: Field2s | None = Field(None, alias='2s')
    field_3s: Field3s | None = Field(None, alias='3s')
    field_4s: Field4s | None = Field(None, alias='4s')
    field_5s: Field5s | None = Field(None, alias='5s')
    average: str | None = None
    total: int | None = None

class SearchMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    popularity_score: int | float | None = None
    rank: int | None = None
    score: float | None = None

class PosterTallItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | None = None
    source: str | None = None
    type: str | None = None
    width: int | None = None

class PosterWideItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | None = None
    source: str | None = None
    type: str | None = None
    width: int | None = None

class PromoImageItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    height: int | None = None
    source: str | None = None
    type: str | None = None
    width: int | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_tall: list[list[PosterTallItem]] | None = None
    poster_wide: list[list[PosterWideItem]] | None = None
    promo_image: list[list[PromoImageItem]] | None = None

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    level: str | None = None
    rating: str | None = None
    system: str | None = None

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_notation: str | None = None
    text_notation: str | None = None

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class Award(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    icon_url: str | None = None
    is_current_award: bool | None = None
    is_winner: bool | None = None
    text: str | None = None

class Images1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_tall: list[list[PosterTallItem]] | None = None
    poster_wide: list[list[PosterWideItem]] | None = None

class Livestream(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    countdown_visibility: int | None = None
    end_date: AwareDatetime | None = None
    episode_end_date: AwareDatetime | None = None
    episode_id: str | None = None
    episode_start_date: AwareDatetime | None = None
    images: Images1 | None = None
    start_date: AwareDatetime | None = None

class SeriesMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_locales: list[str] | None = None
    availability_notes: str | None = None
    episode_count: int | None = None
    extended_description: str | None = None
    extended_maturity_rating: ExtendedMaturityRating | None = None
    is_dubbed: bool | None = None
    is_mature: bool | None = None
    is_simulcast: bool | None = None
    is_subbed: bool | None = None
    language_presentation: LanguagePresentation | None = None
    mature_blocked: bool | None = None
    maturity_ratings: list[str] | None = None
    season_count: int | None = None
    series_launch_year: int | None = None
    subtitle_locales: list[str] | None = None
    tenant_categories: list[str] | None = None
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    awards: list[Award] | None = None
    livestream: Livestream | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    new: bool | None = None
    slug: str | None = None
    rating: Rating | None = None
    search_metadata: SearchMetadata | None = None
    slug_title: str | None = None
    channel_id: str | None = None
    images: Images | None = None
    series_metadata: SeriesMetadata | None = None
    title: str | None = None
    promo_title: str | None = None
    description: str | None = None
    linked_resource_key: str | None = None
    id: str | None = None
    promo_description: str | None = None
    external_id: str | None = None

class SimilarToModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    total: int | None = None
    data: list[Datum] | None = None
    meta: dict[str, Any] | None = None
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
