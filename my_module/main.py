"""Main script to test the my_module package."""

from my_module import greeting, hello


def main() -> None:
    """Run the test script."""
    # Test the hello function
    print("Testing hello() function:")
    hello()
    
    # Test the greeting function
    print("\nTesting greeting() function:")
    print(greeting())
    print(greeting("Claude"))
    print(greeting("Python Developer"))


if __name__ == "__main__":
    main()
