"""
Operations Module - Demonstrates basic mathematical and string operations
This module provides simple functions for common operations that GitHub Copilot can help with.
"""


def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract second number from first number.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide first number by second number.
    
    Args:
        a: First number (numerator)
        b: Second number (denominator)
    
    Returns:
        Quotient of a and b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def concatenate_strings(str1, str2):
    """
    Concatenate two strings with a space in between.
    
    Args:
        str1: First string
        str2: Second string
    
    Returns:
        Concatenated string
    """
    return f"{str1} {str2}"


def reverse_string(text):
    """
    Reverse a string.
    
    Args:
        text: String to reverse
    
    Returns:
        Reversed string
    """
    return text[::-1]


def main():
    """
    Main function to demonstrate the operations.
    """
    print("=== Copilot Operations Demo ===")
    print()
    
    # Mathematical operations
    print("Mathematical Operations:")
    print(f"Add: 5 + 3 = {add(5, 3)}")
    print(f"Subtract: 10 - 4 = {subtract(10, 4)}")
    print(f"Multiply: 6 * 7 = {multiply(6, 7)}")
    print(f"Divide: 20 / 4 = {divide(20, 4)}")
    print()
    
    # String operations
    print("String Operations:")
    print(f"Concatenate: 'Hello' + 'World' = {concatenate_strings('Hello', 'World')}")
    print(f"Reverse: 'Vietnam' = {reverse_string('Vietnam')}")
    print()


if __name__ == "__main__":
    main()
