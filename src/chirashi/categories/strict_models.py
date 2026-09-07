from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel
from typing import Any

class BackgroundItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class LowItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    width: int
    height: int
    type: str
    source: str

class Images(BaseModel):
    model_config = ConfigDict(defer_build=True)
    background: list[BackgroundItem]
    low: list[LowItem]

class Localization(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    description: str
    locale: str

class Datum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: str
    images: Images
    localization: Localization
    slug: str

class CategoriesModel(BaseModel):
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
