from uuid import UUID

from pydantic.dataclasses import dataclass

from models.base import BaseDataclass


@dataclass
class Genre(BaseDataclass):
    """Data class for genres."""

    name: str
    description: str = ''


@dataclass
class GenreFilmwork(BaseDataclass):
    """Data class for the relationship between genres and filmworks."""

    film_work_id: UUID
    genre_id: UUID
