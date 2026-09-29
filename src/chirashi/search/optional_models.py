from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID

class PosterWideItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')

class PosterTallItem(BaseModel):
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

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')

class Thumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | Any = Field(default=None, union_mode='left_to_right')
    height: int | Any = Field(default=None, union_mode='left_to_right')
    type: str | Any = Field(default=None, union_mode='left_to_right')
    source: str | Any = Field(default=None, union_mode='left_to_right')

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_wide: list[list[PosterWideItem]] | Any = Field(default=None, union_mode='left_to_right')
    poster_tall: list[list[PosterTallItem]] | Any = Field(default=None, union_mode='left_to_right')
    promo_image: list[list[PromoImageItem]] | Any = Field(default=None, union_mode='left_to_right')
    thumbnail: list[list[ThumbnailItem] | Thumbnail] | Any = Field(default=None, union_mode='left_to_right')

class LocalizedImages(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_wide: str | Any = Field(default=None, union_mode='left_to_right')
    poster_tall: str | Any = Field(default=None, union_mode='left_to_right')
    thumbnail: str | Any = Field(default=None, union_mode='left_to_right')

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

class Up(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')

class Down(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | Any = Field(default=None, union_mode='left_to_right')
    unit: str | Any = Field(default=None, union_mode='left_to_right')

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_1s: Field1s | Any = Field(None, alias='1s', union_mode='left_to_right')
    field_2s: Field2s | Any = Field(None, alias='2s', union_mode='left_to_right')
    field_3s: Field3s | Any = Field(None, alias='3s', union_mode='left_to_right')
    field_4s: Field4s | Any = Field(None, alias='4s', union_mode='left_to_right')
    field_5s: Field5s | Any = Field(None, alias='5s', union_mode='left_to_right')
    average: str | Any = Field(default=None, union_mode='left_to_right')
    total: int | Any = Field(default=None, union_mode='left_to_right')
    up: Up | Any = Field(default=None, union_mode='left_to_right')
    down: Down | Any = Field(default=None, union_mode='left_to_right')

class AdBreak(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    offset_ms: int | Any = Field(default=None, union_mode='left_to_right')

class Version(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_locale: str | Any = Field(default=None, union_mode='left_to_right')
    guid: str | Any = Field(default=None, union_mode='left_to_right')
    original: bool | Any = Field(default=None, union_mode='left_to_right')
    variant: str | Any = Field(default=None, union_mode='left_to_right')
    season_guid: str | Any = Field(default=None, union_mode='left_to_right')
    media_guid: str | Any = Field(default=None, union_mode='left_to_right')
    is_premium_only: bool | Any = Field(default=None, union_mode='left_to_right')
    roles: list[str] | Any = Field(default=None, union_mode='left_to_right')

class LanguagePresentation2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_notation: str | Any = Field(default=None, union_mode='left_to_right')
    text_notation: str | Any = Field(default=None, union_mode='left_to_right')
    is_original_audio: bool | Any = Field(default=None, union_mode='left_to_right')
    text_locale: str | Any = Field(default=None, union_mode='left_to_right')
    text_notation_reason: str | Any = Field(default=None, union_mode='left_to_right')
    audio_locale: str | Any = Field(default=None, union_mode='left_to_right')
    audio_notation_reason: str | Any = Field(default=None, union_mode='left_to_right')

class EpisodeMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    series_id: str | Any = Field(default=None, union_mode='left_to_right')
    series_title: str | Any = Field(default=None, union_mode='left_to_right')
    series_slug_title: str | Any = Field(default=None, union_mode='left_to_right')
    season_id: str | Any = Field(default=None, union_mode='left_to_right')
    season_title: str | Any = Field(default=None, union_mode='left_to_right')
    season_slug_title: str | Any = Field(default=None, union_mode='left_to_right')
    season_number: int | Any = Field(default=None, union_mode='left_to_right')
    episode_number: int | Any = Field(default=None, union_mode='left_to_right')
    episode: str | Any = Field(default=None, union_mode='left_to_right')
    sequence_number: int | Any = Field(default=None, union_mode='left_to_right')
    season_display_number: str | Any = Field(default=None, union_mode='left_to_right')
    season_sequence_number: int | Any = Field(default=None, union_mode='left_to_right')
    duration_ms: int | Any = Field(default=None, union_mode='left_to_right')
    ad_breaks: list[AdBreak] | Any = Field(default=None, union_mode='left_to_right')
    episode_air_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    upload_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    availability_starts: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    availability_ends: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    eligible_region: str | Any = Field(default=None, union_mode='left_to_right')
    is_premium_only: bool | Any = Field(default=None, union_mode='left_to_right')
    extended_maturity_rating: ExtendedMaturityRating | Any = Field(default=None, union_mode='left_to_right')
    maturity_ratings: list[str] | Any = Field(default=None, union_mode='left_to_right')
    content_descriptors: list[str] | Any = Field(default=None, union_mode='left_to_right')
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | Any = Field(default=None, union_mode='left_to_right')
    is_mature: bool | Any = Field(default=None, union_mode='left_to_right')
    mature_blocked: bool | Any = Field(default=None, union_mode='left_to_right')
    available_date: Any | None = None
    free_available_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    premium_date: Any | None = None
    premium_available_date: AwareDatetime | Any = Field(default=None, union_mode='left_to_right')
    is_subbed: bool | Any = Field(default=None, union_mode='left_to_right')
    is_dubbed: bool | Any = Field(default=None, union_mode='left_to_right')
    is_clip: bool | Any = Field(default=None, union_mode='left_to_right')
    available_offline: bool | Any = Field(default=None, union_mode='left_to_right')
    linked_guid: str | Any = Field(default=None, union_mode='left_to_right')
    tenant_categories: list[str] | Any = Field(default=None, union_mode='left_to_right')
    subtitle_locales: list[str] | Any = Field(default=None, union_mode='left_to_right')
    availability_notes: str | Any = Field(default=None, union_mode='left_to_right')
    audio_locale: str | Any = Field(default=None, union_mode='left_to_right')
    versions: list[Version] | Any = Field(default=None, union_mode='left_to_right')
    closed_captions_available: bool | Any = Field(default=None, union_mode='left_to_right')
    identifier: str | Any = Field(default=None, union_mode='left_to_right')
    availability_status: str | Any = Field(default=None, union_mode='left_to_right')
    roles: list[str] | Any = Field(default=None, union_mode='left_to_right')
    language_presentation: LanguagePresentation2 | Any = Field(default=None, union_mode='left_to_right')

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    end_date: AwareDatetime | Any = Field(None, alias='endDate', union_mode='left_to_right')
    start_date: AwareDatetime | Any = Field(None, alias='startDate', union_mode='left_to_right')

class Artist(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_value: str | Any = Field(None, alias='displayValue', union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')

class MainArtistItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    connector: str | Any = Field(default=None, union_mode='left_to_right')
    id: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    roles: list[str] | Any = Field(default=None, union_mode='left_to_right')
    sequence_number: int | Any = Field(None, alias='sequenceNumber', union_mode='left_to_right')
    slug: str | Any = Field(default=None, union_mode='left_to_right')

class Artists(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    main_artist: list[MainArtistItem] | Any = Field(None, alias='MainArtist', union_mode='left_to_right')

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
    episode_metadata: EpisodeMetadata | Any = Field(default=None, union_mode='left_to_right')
    streams_link: str | Any = Field(default=None, union_mode='left_to_right')
    availability: Availability | Any = Field(default=None, union_mode='left_to_right')
    copyright: str | Any = Field(default=None, union_mode='left_to_right')
    maturity_ratings: dict[str, Any] | Any = Field(None, alias='maturityRatings', union_mode='left_to_right')
    artist: Artist | Any = Field(default=None, union_mode='left_to_right')
    genres: list[Genre] | Any = Field(default=None, union_mode='left_to_right')
    sequence_number: int | Any = Field(None, alias='sequenceNumber', union_mode='left_to_right')
    ready_to_publish: bool | Any = Field(None, alias='readyToPublish', union_mode='left_to_right')
    display_artist_name: str | Any = Field(None, alias='displayArtistName', union_mode='left_to_right')
    original_release: AwareDatetime | Any = Field(None, alias='originalRelease', union_mode='left_to_right')
    display_artist_name_required: bool | Any = Field(None, alias='displayArtistNameRequired', union_mode='left_to_right')
    is_public: bool | Any = Field(None, alias='isPublic', union_mode='left_to_right')
    publish_date: AwareDatetime | Any = Field(None, alias='publishDate', union_mode='left_to_right')
    hash: UUID | Any = Field(default=None, union_mode='left_to_right')
    is_premium_only: bool | Any = Field(None, alias='isPremiumOnly', union_mode='left_to_right')
    created_at: AwareDatetime | Any = Field(None, alias='createdAt', union_mode='left_to_right')
    updated_at: AwareDatetime | Any = Field(None, alias='updatedAt', union_mode='left_to_right')
    duration_ms: int | Any = Field(None, alias='durationMs', union_mode='left_to_right')
    licensor: str | Any = Field(default=None, union_mode='left_to_right')
    artists: Artists | Any = Field(default=None, union_mode='left_to_right')
    mature_blocked: bool | Any = Field(None, alias='matureBlocked', union_mode='left_to_right')
    is_mature: bool | Any = Field(None, alias='isMature', union_mode='left_to_right')
    anime_ids: list[str] | Any = Field(None, alias='animeIds', union_mode='left_to_right')

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | Any = Field(default=None, union_mode='left_to_right')
    items: list[Item] | Any = Field(default=None, union_mode='left_to_right')
    count: int | Any = Field(default=None, union_mode='left_to_right')

class SearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum] | Any = Field(default=None, union_mode='left_to_right')
    total: int | Any = Field(default=None, union_mode='left_to_right')
    meta: dict[str, Any] | Any = Field(default=None, union_mode='left_to_right')
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
