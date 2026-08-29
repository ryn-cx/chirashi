from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID

class PosterWideItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class PosterTallItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class PromoImageItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class ThumbnailItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class Thumbnail(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_wide: list[list[PosterWideItem]] | None = None
    poster_tall: list[list[PosterTallItem]] | None = None
    promo_image: list[list[PromoImageItem]] | None = None
    thumbnail: list[list[ThumbnailItem] | Thumbnail] | None = None

class LocalizedImages(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    poster_wide: str | None = None
    poster_tall: str | None = None
    thumbnail: str | None = None

class ExtendedMaturityRating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    system: str | None = None
    rating: str | None = None
    level: str | None = None
    advisories: list[Any] | None = None

class ContentDescriptorsWithSymbolItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None

class LanguagePresentation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_notation: str | None = None
    text_notation: str | None = None
    is_original_audio: bool | None = None
    audio_locale: str | None = None
    text_locale: str | None = None
    audio_notation_reason: str | None = None
    text_notation_reason: str | None = None

class Award(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    icon_url: str | None = None
    is_current_award: bool | None = None
    is_winner: bool | None = None

class SeriesMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    availability_status: str | None = None
    extended_description: str | None = None
    episode_count: int | None = None
    season_count: int | None = None
    extended_maturity_rating: ExtendedMaturityRating | None = None
    maturity_ratings: list[str] | None = None
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    is_mature: bool | None = None
    mature_blocked: bool | None = None
    is_subbed: bool | None = None
    is_dubbed: bool | None = None
    is_simulcast: bool | None = None
    linked_guid: str | None = None
    availability_notes: str | None = None
    audio_locales: list[str] | None = None
    subtitle_locales: list[str] | None = None
    series_launch_year: int | None = None
    tenant_categories: list[str] | None = None
    language_presentation: LanguagePresentation | None = None
    awards: list[Award] | None = None

class SearchMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    score: float | None = None
    rank: int | None = None
    popularity_score: int | float | None = None

class Field1s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    unit: str | None = None
    percentage: int | None = None

class Field2s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    unit: str | None = None
    percentage: int | None = None

class Field3s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    unit: str | None = None
    percentage: int | None = None

class Field4s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    unit: str | None = None
    percentage: int | None = None

class Field5s(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    unit: str | None = None
    percentage: int | None = None

class Up(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    unit: str | None = None

class Down(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    displayed: str | None = None
    unit: str | None = None

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_1s: Field1s | None = Field(None, alias='1s')
    field_2s: Field2s | None = Field(None, alias='2s')
    field_3s: Field3s | None = Field(None, alias='3s')
    field_4s: Field4s | None = Field(None, alias='4s')
    field_5s: Field5s | None = Field(None, alias='5s')
    average: str | None = None
    total: int | None = None
    up: Up | None = None
    down: Down | None = None

class AdBreak(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    offset_ms: int | None = None

class Version(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_locale: str | None = None
    guid: str | None = None
    original: bool | None = None
    variant: str | None = None
    season_guid: str | None = None
    media_guid: str | None = None
    is_premium_only: bool | None = None
    roles: list[str] | None = None

class LanguagePresentation2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    audio_notation: str | None = None
    text_notation: str | None = None
    is_original_audio: bool | None = None
    text_locale: str | None = None
    text_notation_reason: str | None = None
    audio_locale: str | None = None
    audio_notation_reason: str | None = None

class EpisodeMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    series_id: str | None = None
    series_title: str | None = None
    series_slug_title: str | None = None
    season_id: str | None = None
    season_title: str | None = None
    season_slug_title: str | None = None
    season_number: int | None = None
    episode_number: int | None = None
    episode: str | None = None
    sequence_number: int | None = None
    season_display_number: str | None = None
    season_sequence_number: int | None = None
    duration_ms: int | None = None
    ad_breaks: list[AdBreak] | None = None
    episode_air_date: AwareDatetime | None = None
    upload_date: AwareDatetime | None = None
    availability_starts: AwareDatetime | None = None
    availability_ends: AwareDatetime | None = None
    eligible_region: str | None = None
    is_premium_only: bool | None = None
    extended_maturity_rating: ExtendedMaturityRating | None = None
    maturity_ratings: list[str] | None = None
    content_descriptors: list[str] | None = None
    content_descriptors_with_symbol: list[ContentDescriptorsWithSymbolItem] | None = None
    is_mature: bool | None = None
    mature_blocked: bool | None = None
    available_date: Any | None = None
    free_available_date: AwareDatetime | None = None
    premium_date: Any | None = None
    premium_available_date: AwareDatetime | None = None
    is_subbed: bool | None = None
    is_dubbed: bool | None = None
    is_clip: bool | None = None
    available_offline: bool | None = None
    linked_guid: str | None = None
    tenant_categories: list[str] | None = None
    subtitle_locales: list[str] | None = None
    availability_notes: str | None = None
    audio_locale: str | None = None
    versions: list[Version] | None = None
    closed_captions_available: bool | None = None
    identifier: str | None = None
    availability_status: str | None = None
    roles: list[str] | None = None
    language_presentation: LanguagePresentation2 | None = None

class Availability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    end_date: AwareDatetime | None = Field(None, alias='endDate')
    start_date: AwareDatetime | None = Field(None, alias='startDate')

class Artist(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    name: str | None = None
    slug: str | None = None

class Genre(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_value: str | None = Field(None, alias='displayValue')
    id: str | None = None

class MainArtistItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    connector: str | None = None
    id: str | None = None
    name: str | None = None
    roles: list[str] | None = None
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    slug: str | None = None

class Artists(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    main_artist: list[MainArtistItem] | None = Field(None, alias='MainArtist')

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    external_id: str | None = None
    channel_id: str | None = None
    linked_resource_key: str | None = None
    new: bool | None = None
    title: str | None = None
    description: str | None = None
    promo_title: str | None = None
    promo_description: str | None = None
    type: str | None = None
    slug: str | None = None
    slug_title: str | None = None
    last_public: AwareDatetime | None = None
    images: Images | None = None
    localized_images: LocalizedImages | None = None
    series_metadata: SeriesMetadata | None = None
    search_metadata: SearchMetadata | None = None
    language_presentation: LanguagePresentation | None = None
    rating: Rating | None = None
    episode_metadata: EpisodeMetadata | None = None
    streams_link: str | None = None
    availability: Availability | None = None
    copyright: str | None = None
    maturity_ratings: dict[str, Any] | None = Field(None, alias='maturityRatings')
    artist: Artist | None = None
    genres: list[Genre] | None = None
    sequence_number: int | None = Field(None, alias='sequenceNumber')
    ready_to_publish: bool | None = Field(None, alias='readyToPublish')
    display_artist_name: str | None = Field(None, alias='displayArtistName')
    original_release: AwareDatetime | None = Field(None, alias='originalRelease')
    display_artist_name_required: bool | None = Field(None, alias='displayArtistNameRequired')
    is_public: bool | None = Field(None, alias='isPublic')
    publish_date: AwareDatetime | None = Field(None, alias='publishDate')
    hash: UUID | None = None
    is_premium_only: bool | None = Field(None, alias='isPremiumOnly')
    created_at: AwareDatetime | None = Field(None, alias='createdAt')
    updated_at: AwareDatetime | None = Field(None, alias='updatedAt')
    duration_ms: int | None = Field(None, alias='durationMs')
    licensor: str | None = None
    artists: Artists | None = None
    mature_blocked: bool | None = Field(None, alias='matureBlocked')
    is_mature: bool | None = Field(None, alias='isMature')
    anime_ids: list[str] | None = Field(None, alias='animeIds')

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    items: list[Item] | None = None
    count: int | None = None

class SearchModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    data: list[Datum] | None = None
    total: int | None = None
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
