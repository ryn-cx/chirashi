from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any

class PosterTallItem(BaseModel):
    height: int
    source: str
    type: str
    width: int

class PosterWideItem(BaseModel):
    height: int
    source: str
    type: str
    width: int

class Images(BaseModel):
    poster_tall: list[PosterTallItem]
    poster_wide: list[PosterWideItem]

class Genre(BaseModel):
    display_value: str = Field(..., alias='displayValue')
    id: str

class Datum(BaseModel):
    images: Images
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    total_video_duration_ms: int = Field(..., alias='totalVideoDurationMs')
    type: str
    genres: list[Genre]
    slug: str
    is_public: bool = Field(..., alias='isPublic')
    name: str
    total_concert_duration_ms: int = Field(..., alias='totalConcertDurationMs')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    videos: list[str]
    concerts: list[None]
    created_at: AwareDatetime = Field(..., alias='createdAt')
    description: str
    id: str

class ArtistModel(BaseModel):
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
