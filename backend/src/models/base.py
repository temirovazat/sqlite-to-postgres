import time
from datetime import datetime
from typing import Any, ClassVar
from uuid import UUID

from pydantic import validator
from pydantic.dataclasses import dataclass
from pydantic.fields import ModelField

MILLISECOND_DELAY = 0.001


@dataclass
class BaseDataclass(object):
    """Base data class."""

    id: UUID
    __dataclass_fields__: ClassVar[dict]

    def __post_init__(self):
        """After class initialization, a one-millisecond delay is applied to sort data by load time."""
        time.sleep(MILLISECOND_DELAY)
        class_name = type(self).__name__
        if class_name in {'Person', 'Genre', 'Filmwork'}:
            self.modified = datetime.utcnow()
        self.created = datetime.utcnow()

    @validator('*', pre=True)
    def change_none_to_default(cls, value: Any, field: ModelField) -> Any:
        """
        Return the default value when None is passed to a field.

        Args:
            value: Value passed to the field.
            field: Data class field.

        Returns:
            Any: Default value if None is passed, or the passed value.
        """
        return field.default if value is None else value
