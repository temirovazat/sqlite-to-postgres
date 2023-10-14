from uuid import UUID

from pydantic.dataclasses import dataclass

from models.base import BaseDataclass


@dataclass
class Person(BaseDataclass):
    """Data class for persons."""

    full_name: str


@dataclass
class PersonFilmwork(BaseDataclass):
    """Data class for the relationship between persons and film works."""

    film_work_id: UUID
    person_id: UUID
    role: str
