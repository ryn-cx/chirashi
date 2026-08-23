from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

class PosterTallItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    height: int | None = None
    source: str | None = None
    type: str | None = None
    width: int | None = None

class PosterWideItem(BaseModel):
    model_config = ConfigDict(extra='ignore')
    height: int | None = None
    source: str | None = None
    type: str | None = None
    width: int | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore')
    poster_tall: list[PosterTallItem] | None = None
    poster_wide: list[PosterWideItem] | None = None

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore')
    display_value: str | None = Field(None, alias='displayValue')
    id: str | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore')
    images: Images | None = None
    publish_date: AwareDatetime | None = Field(None, alias='publishDate')
    ready_to_publish: bool | None = Field(None, alias='readyToPublish')
    total_video_duration_ms: int | None = Field(None, alias='totalVideoDurationMs')
    type: str | None = None
    genres: list[Genre] | None = None
    slug: str | None = None
    is_public: bool | None = Field(None, alias='isPublic')
    name: str | None = None
    total_concert_duration_ms: int | None = Field(None, alias='totalConcertDurationMs')
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    videos: list[str] | None = None
    concerts: list[Any] | None = None
    created_at: AwareDatetime | None = Field(None, alias='createdAt')
    description: str | None = None
    id: str | None = None

class ArtistModel(BaseModel):
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
