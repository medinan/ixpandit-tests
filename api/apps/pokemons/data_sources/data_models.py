from decimal import Decimal
from typing import List

from pydantic import BaseModel


class EvolutionModel(BaseModel):
    name: str
    order: int


class HeldItemsModel(BaseModel):
    name: str


class AbilitiesModel(BaseModel):
    name: str


class TypesModel(BaseModel):
    name: str


class StatModel(BaseModel):
    name: str
    base_stat: int
    effort: int


class PokemonModel(BaseModel):
    poke_id: int
    name: str
    height: Decimal
    weight: Decimal
    image: str
    evolutions: List[EvolutionModel] = []
    held_items: List[HeldItemsModel] = []
    abilities: List[AbilitiesModel] = []
    types: List[TypesModel] = []
    stats: List[StatModel] = []
