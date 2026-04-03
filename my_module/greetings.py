"""Greetings module with simple greeting functions."""


def hello() -> None:
    """Print a classic Hello, World! message."""
    print("Hello, World!")


def custom_hello(name: str) -> None:
    """Print a custom greeting.
    
    Args:
        name: The name to include in the greeting.
    """
    print(f"Hello, {name}!")
