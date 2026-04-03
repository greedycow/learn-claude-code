"""My Module - A simple hello world module."""


def greeting(name: str = "World") -> str:
    """Return a greeting message.
    
    Args:
        name: The name to greet. Defaults to "World".
    
    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


# Expose the hello function from greetings module
from .greetings import hello

__all__ = ["greeting", "hello"]
