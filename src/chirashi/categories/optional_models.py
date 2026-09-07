from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict
from typing import Any

class BackgroundItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class LowItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    width: int | None = None
    height: int | None = None
    type: str | None = None
    source: str | None = None

class Images(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    background: list[BackgroundItem] | None = None
    low: list[LowItem] | None = None

class Localization(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    description: str | None = None
    locale: str | None = None

class Datum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: str | None = None
    images: Images | None = None
    localization: Localization | None = None
    slug: str | None = None

class CategoriesModel(BaseModel):
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
