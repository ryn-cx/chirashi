from typing import Any, Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel

class PosterTallItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class PosterWideItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    poster_tall: list[list[PosterTallItem]]
    poster_wide: list[list[PosterWideItem]]

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    system: str | None = None
    rating: str | None = None
    level: str | None = None

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_notation: str
    text_notation: str
    text_locale: str | None = None
    text_notation_reason: str | None = None
    is_original_audio: bool | None = None
    audio_locale: str | None = None
    audio_notation_reason: str | None = None

class LocalizedImages(BaseModel):
    model_config = ConfigDict(defer_build=True)
    poster_wide: str
    poster_tall: str

class Award(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    icon_url: str
    is_current_award: bool
    is_winner: bool

class SeriesModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    channel_id: str
    title: str
    slug: str
    slug_title: str
    description: str
    extended_description: str
    keywords: list[str]
    season_tags: list[str]
    images: Images
    episode_count: int
    season_count: int
    media_count: int
    content_provider: str
    maturity_ratings: list[str]
    extended_maturity_rating: ExtendedMaturityRating
    is_mature: bool
    mature_blocked: bool
    is_subbed: bool
    is_dubbed: bool
    is_simulcast: bool
    seo_title: str
    seo_description: str
    subtitle_locales: list[str]
    audio_locales: list[str]
    availability_status: str
    availability_notes: str
    series_launch_year: int | None = None
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    language_presentation: LanguagePresentation
    localized_images: LocalizedImages | None = None
    awards: list[Award] | None = None
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
