from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any

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

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_tall: list[PosterTallItem] | None = None
    poster_wide: list[PosterWideItem] | None = None

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_value: str | None = Field(None, alias='displayValue')
    id: str | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    images: Images | None = None
    is_public: bool | None = Field(None, alias='isPublic')
    ready_to_publish: bool | None = Field(None, alias='readyToPublish')
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    description: str | None = None
    concerts: list[str] | None = None
    total_video_duration_ms: int | None = Field(None, alias='totalVideoDurationMs')
    type: str | None = None
    genres: list[Genre] | None = None
    id: str | None = None
    created_at: AwareDatetime | None = Field(None, alias='createdAt')
    publish_date: AwareDatetime | None = Field(None, alias='publishDate')
    slug: str | None = None
    total_concert_duration_ms: int | None = Field(None, alias='totalConcertDurationMs')
    videos: list[str] | None = None
    name: str | None = None

class BrowseMusicModel(BaseModel):
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
