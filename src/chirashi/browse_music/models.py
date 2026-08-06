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
    type: str
    description: str
    genres: list[Genre]
    publish_date: AwareDatetime = Field(..., alias='publishDate')
    videos: list[str]
    concerts: list[str]
    total_concert_duration_ms: int = Field(..., alias='totalConcertDurationMs')
    created_at: AwareDatetime = Field(..., alias='createdAt')
    is_public: bool = Field(..., alias='isPublic')
    name: str
    total_video_duration_ms: int = Field(..., alias='totalVideoDurationMs')
    id: str
    images: Images
    ready_to_publish: bool = Field(..., alias='readyToPublish')
    updated_at: AwareDatetime = Field(..., alias='updatedAt')
    slug: str

class BrowseMusicModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    total: int
    data: list[Datum]
    meta: dict[str, Any]
