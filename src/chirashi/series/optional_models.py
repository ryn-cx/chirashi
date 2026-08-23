from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict
from typing import Any

class PosterWideItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class PosterTallItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore')
    poster_wide: list[list[PosterWideItem]] | None = None
    poster_tall: list[list[PosterTallItem]] | None = None

class LocalizedImages(BaseModel):
    model_config = ConfigDict(extra='ignore')
    poster_wide: str | None = None
    poster_tall: str | None = None

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore')
    system: str | None = None
    rating: str | None = None
    level: str | None = None

class Award(BaseModel):
    model_config = ConfigDict(extra='ignore')
    text: str | None = None
    icon_url: str | None = None
    is_current_award: bool | None = None
    is_winner: bool | None = None

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    label: str | None = None

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra='ignore')
    audio_notation: str | None = None
    text_notation: str | None = None
    is_original_audio: bool | None = None
    audio_locale: str | None = None
    text_locale: str | None = None
    audio_notation_reason: str | None = None
    text_notation_reason: str | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore')
    id: str | None = None
    channel_id: str | None = None
    title: str | None = None
    slug: str | None = None
    slug_title: str | None = None
    description: str | None = None
    extended_description: str | None = None
    keywords: list[str] | None = None
    season_tags: list[str] | None = None
    images: Images | None = None
    localized_images: LocalizedImages | None = None
    episode_count: int | None = None
    season_count: int | None = None
    media_count: int | None = None
    content_provider: str | None = None
    maturity_ratings: list[str] | None = None
    extended_maturity_rating: ExtendedMaturityRating | None = None
    is_mature: bool | None = None
    mature_blocked: bool | None = None
    is_subbed: bool | None = None
    is_dubbed: bool | None = None
    is_simulcast: bool | None = None
    seo_title: str | None = None
    seo_description: str | None = None
    subtitle_locales: list[str] | None = None
    audio_locales: list[str] | None = None
    availability_status: str | None = None
    availability_notes: str | None = None
    series_launch_year: int | None = None
    awards: list[Award] | None = None
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    language_presentation: LanguagePresentation | None = None

class SeriesModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
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
