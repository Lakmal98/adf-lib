class ValidationError(Exception):
    """Base exception for validation errors in the ADF library."""

    pass


class RequiredFieldError(ValidationError):
    """Exception raised when a required field is missing."""

    pass


class InvalidMarkError(ValidationError):
    """Exception raised when an invalid mark type is provided."""

    pass