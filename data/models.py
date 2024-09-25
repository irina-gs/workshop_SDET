from typing import List

from pydantic import BaseModel


class AdditionModel(BaseModel):
    additional_info: str
    additional_number: int
    id: int | None = None


class EntityModel(BaseModel):
    addition: AdditionModel
    id: int | None = None
    important_numbers: List[int]
    title: str
    verified: bool


class AllEntitiesModel(BaseModel):
    entity: List[EntityModel]
