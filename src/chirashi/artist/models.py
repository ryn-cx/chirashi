from pydantic import AwareDatetime, ConfigDict, Field
from good_ass_pydantic_integrator import GAPIBaseModel
from typing import Any

class Genre(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_value: str = Field(..., alias='displayValue')
    id: str

class PosterTallItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    height: int
    source: str
    type: str
    width: int

class PosterWideItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    height: int
    source: str
    type: str
    width: int

class Images(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    poster_tall: list[PosterTallItem]
    poster_wide: list[PosterWideItem]

class Datum(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    slug: str
    total_video_duration_ms: int = Field(..., alias='totalVideoDurationMs')
    description: str
    type: str
    genres: list[Genre]
    images: Images
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    concerts: list[None]
    created_at: AwareDatetime = Field(..., alias='createdAt')
    id: str
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    total_concert_duration_ms: int = Field(..., alias='totalConcertDurationMs')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    videos: list[str]
    is_public: bool = Field(..., alias='isPublic')
    name: str

class ArtistModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    total: int
    data: list[Datum]
    meta: dict[str, Any]
