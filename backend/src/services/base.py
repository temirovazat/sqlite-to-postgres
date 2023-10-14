class Config(object):
    """Class with settings for a data class based on Pydantic."""

    arbitrary_types_allowed = True


class LoadTableError(Exception):
    """Error while loading a table."""


class LoadDataError(Exception):
    """Error while loading data."""
