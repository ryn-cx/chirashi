from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel
from typing import Any

class PosterWideItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class PosterTallItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    poster_wide: list[list[PosterWideItem]]
    poster_tall: list[list[PosterTallItem]]

class LocalizedImages(BaseModel):
    model_config = ConfigDict(defer_build=True)
    poster_wide: str
    poster_tall: str

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    system: str
    rating: str
    level: str

class Award(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    icon_url: str
    is_current_award: bool
    is_winner: bool

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    audio_notation: str
    text_notation: str
    is_original_audio: bool
    audio_locale: str
    text_locale: str
    audio_notation_reason: str
    text_notation_reason: str

class Datum(BaseModel):
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
    localized_images: LocalizedImages
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
    series_launch_year: int
    awards: list[Award] | None = None
    content_descriptors: list[str]
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem]
    language_presentation: LanguagePresentation

class SeriesModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    total: int
    data: list[Datum]
    meta: dict[str, Any]
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
