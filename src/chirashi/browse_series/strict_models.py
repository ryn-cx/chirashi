from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any

class PosterTallItem(BaseModel):
    width: int
    height: int
    type: str
    source: str

class PosterWideItem(BaseModel):
    width: int
    height: int
    type: str
    source: str

class PromoImageItem(BaseModel):
    width: int
    height: int
    type: str
    source: str

class Images(BaseModel):
    poster_tall: list[list[PosterTallItem]]
    poster_wide: list[list[PosterWideItem]]
    promo_image: list[list[PromoImageItem]]

class LocalizedImages(BaseModel):
    poster_tall: str
    poster_wide: str

class ExtendedMaturityRating(BaseModel):
    system: str | None = None
    rating: str | None = None
    level: str | None = None
    advisories: list[None] | None = None

class ContentDescriptorsWithSymbolItem(BaseModel):
    label: str

class LanguagePresentation(BaseModel):
    audio_notation: str
    text_notation: str
    is_original_audio: bool | None = None
    text_locale: str | None = None
    text_notation_reason: str | None = None
    audio_locale: str | None = None
    audio_notation_reason: str | None = None

class Award(BaseModel):
    text: str
    icon_url: str
    is_current_award: bool
    is_winner: bool

class SeriesMetadata(BaseModel):
    availability_status: str
    extended_description: str
    episode_count: int
    season_count: int
    extended_maturity_rating: ExtendedMaturityRating
    maturity_ratings: list[str]
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    is_mature: bool
    mature_blocked: bool
    is_subbed: bool
    is_dubbed: bool
    is_simulcast: bool
    linked_guid: str
    availability_notes: str
    audio_locales: list[str]
    subtitle_locales: list[str]
    series_launch_year: int
    tenant_categories: list[str]
    language_presentation: LanguagePresentation
    awards: list[Award] | None = None

class Field1s(BaseModel):
    displayed: str
    unit: str
    percentage: int

class Field2s(BaseModel):
    displayed: str
    unit: str
    percentage: int

class Field3s(BaseModel):
    displayed: str
    unit: str
    percentage: int

class Field4s(BaseModel):
    displayed: str
    unit: str
    percentage: int

class Field5s(BaseModel):
    displayed: str
    unit: str
    percentage: int

class Rating(BaseModel):
    field_1s: Field1s = Field(..., alias='1s')
    field_2s: Field2s = Field(..., alias='2s')
    field_3s: Field3s = Field(..., alias='3s')
    field_4s: Field4s = Field(..., alias='4s')
    field_5s: Field5s = Field(..., alias='5s')
    average: str
    total: int

class Datum(BaseModel):
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
    localized_images: LocalizedImages
    series_metadata: SeriesMetadata
    language_presentation: LanguagePresentation
    rating: Rating

class BrowseSeriesModel(BaseModel):
    data: list[Datum]
    total: int
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
