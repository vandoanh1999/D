"""
Unit tests for operations module.
These tests demonstrate how GitHub Copilot can help write test cases.
"""

import pytest
from operations import add, subtract, multiply, divide, concatenate_strings, reverse_string


def test_add():
    """Test addition operation."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(100, 50) == 150


def test_subtract():
    """Test subtraction operation."""
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0
    assert subtract(0, 5) == -5
    assert subtract(100, 50) == 50


def test_multiply():
    """Test multiplication operation."""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(10, 10) == 100


def test_divide():
    """Test division operation."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(7, 2) == 3.5
    
    # Test division by zero
    with pytest.raises(ValueError):
        divide(10, 0)


def test_concatenate_strings():
    """Test string concatenation operation."""
    assert concatenate_strings("Hello", "World") == "Hello World"
    assert concatenate_strings("Việt", "Nam") == "Việt Nam"
    assert concatenate_strings("", "Test") == " Test"


def test_reverse_string():
    """Test string reversal operation."""
    assert reverse_string("Hello") == "olleH"
    assert reverse_string("Vietnam") == "manteiV"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
