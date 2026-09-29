from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class PosterTallItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')

class PosterWideItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')

class PromoImageItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_tall: list[list[PosterTallItem]] | Any = Field(default=None, union_mode='left_to_right')
    poster_wide: list[list[PosterWideItem]] | Any = Field(default=None, union_mode='left_to_right')
    promo_image: list[list[PromoImageItem]] | Any = Field(default=None, union_mode='left_to_right')

class LocalizedImages(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_tall: str | Any = Field(default=None, union_mode='left_to_right')
    poster_wide: str | Any = Field(default=None, union_mode='left_to_right')

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    system: str | Any = Field(default=None, union_mode='left_to_right')
    rating: str | Any = Field(default=None, union_mode='left_to_right')
    level: str | Any = Field(default=None, union_mode='left_to_right')
    advisories: list[Any] | Any = Field(default=None, union_mode='left_to_right')

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | Any = Field(default=None, union_mode='left_to_right')

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_notation: str | Any = Field(default=None, union_mode='left_to_right')
    text_notation: str | Any = Field(default=None, union_mode='left_to_right')
    is_original_audio: bool | Any = Field(default=None, union_mode='left_to_right')
    audio_locale: str | Any = Field(default=None, union_mode='left_to_right')
    text_locale: str | Any = Field(default=None, union_mode='left_to_right')
    audio_notation_reason: str | Any = Field(default=None, union_mode='left_to_right')
    text_notation_reason: str | Any = Field(default=None, union_mode='left_to_right')

class Award(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | Any = Field(default=None, union_mode='left_to_right')
    icon_url: str | Any = Field(default=None, union_mode='left_to_right')
    is_current_award: bool | Any = Field(default=None, union_mode='left_to_right')
    is_winner: bool | Any = Field(default=None, union_mode='left_to_right')

class SeriesMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_status: str | Any = Field(default=None, union_mode='left_to_right')
    extended_description: str | Any = Field(default=None, union_mode='left_to_right')
    episode_count: int | Any = Field(default=None, union_mode='left_to_right')
    season_count: int | Any = Field(default=None, union_mode='left_to_right')
    extended_maturity_rating: ExtendedMaturityRating | Any = Field(default=None, union_mode='left_to_right')
    maturity_ratings: list[str] | Any = Field(default=None, union_mode='left_to_right')
    content_descriptors: list[str] | Any = Field(default=None, union_mode='left_to_right')
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | Any = Field(default=None, union_mode='left_to_right')
    is_mature: bool | Any = Field(default=None, union_mode='left_to_right')
    mature_blocked: bool | Any = Field(default=None, union_mode='left_to_right')
    is_subbed: bool | Any = Field(default=None, union_mode='left_to_right')
    is_dubbed: bool | Any = Field(default=None, union_mode='left_to_right')
    is_simulcast: bool | Any = Field(default=None, union_mode='left_to_right')
    linked_guid: str | Any = Field(default=None, union_mode='left_to_right')
    availability_notes: str | Any = Field(default=None, union_mode='left_to_right')
    audio_locales: list[str] | Any = Field(default=None, union_mode='left_to_right')
    subtitle_locales: list[str] | Any = Field(default=None, union_mode='left_to_right')
    series_launch_year: int | Any = Field(default=None, union_mode='left_to_right')
    tenant_categories: list[str] | Any = Field(default=None, union_mode='left_to_right')
    language_presentation: LanguagePresentation | Any = Field(default=None, union_mode='left_to_right')
    awards: list[Award] | Any = Field(default=None, union_mode='left_to_right')

class SearchMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    score: float | Any = Field(default=None, union_mode='left_to_right')
    rank: int | Any = Field(default=None, union_mode='left_to_right')
    popularity_score: int | float | Any = Field(default=None, union_mode='left_to_right')

class Field1s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')
    percentage: int | Any = Field(default=None, union_mode='left_to_right')

class Field2s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')
    percentage: int | Any = Field(default=None, union_mode='left_to_right')

class Field3s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')
    percentage: int | Any = Field(default=None, union_mode='left_to_right')

class Field4s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')
    percentage: int | Any = Field(default=None, union_mode='left_to_right')

class Field5s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')
    percentage: int | Any = Field(default=None, union_mode='left_to_right')

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_1s: Field1s | Any = Field(None, alias='1s', union_mode='left_to_right')
    field_2s: Field2s | Any = Field(None, alias='2s', union_mode='left_to_right')
    field_3s: Field3s | Any = Field(None, alias='3s', union_mode='left_to_right')
    field_4s: Field4s | Any = Field(None, alias='4s', union_mode='left_to_right')
    field_5s: Field5s | Any = Field(None, alias='5s', union_mode='left_to_right')
    average: str | Any = Field(default=None, union_mode='left_to_right')
    total: int | Any = Field(default=None, union_mode='left_to_right')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    external_id: str | Any = Field(default=None, union_mode='left_to_right')
    channel_id: str | Any = Field(default=None, union_mode='left_to_right')
    linked_resource_key: str | Any = Field(default=None, union_mode='left_to_right')
    new: bool | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    description: str | Any = Field(default=None, union_mode='left_to_right')
    promo_title: str | Any = Field(default=None, union_mode='left_to_right')
    promo_description: str | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')
    slug_title: str | Any = Field(default=None, union_mode='left_to_right')
    last_public: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    images: Images | Any = Field(default=None, union_mode='left_to_right')
    localized_images: LocalizedImages | Any = Field(default=None, union_mode='left_to_right')
    series_metadata: SeriesMetadata | Any = Field(default=None, union_mode='left_to_right')
    search_metadata: SearchMetadata | Any = Field(default=None, union_mode='left_to_right')
    language_presentation: LanguagePresentation | Any = Field(default=None, union_mode='left_to_right')
    rating: Rating | Any = Field(default=None, union_mode='left_to_right')

class SearchMovieListingModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')
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
