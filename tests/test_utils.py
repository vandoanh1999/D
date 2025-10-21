"""
Test file for utils module
Tệp kiểm thử cho module utils
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import calculate_sum, format_message, validate_input

def test_calculate_sum():
    """Kiểm thử hàm tính tổng / Test sum calculation"""
    assert calculate_sum(2, 3) == 5
    assert calculate_sum(0, 0) == 0
    assert calculate_sum(-1, 1) == 0
    assert calculate_sum(10.5, 5.5) == 16.0
    print("✓ test_calculate_sum passed")

def test_format_message():
    """Kiểm thử hàm định dạng thông điệp / Test message formatting"""
    assert format_message("Xin chào", "Anh") == "Xin chào, Anh!"
    assert format_message("Hello", "World") == "Hello, World!"
    print("✓ test_format_message passed")

def test_validate_input():
    """Kiểm thử hàm xác thực đầu vào / Test input validation"""
    assert validate_input("valid") == True
    assert validate_input("") == False
    assert validate_input(None) == False
    assert validate_input(123) == True
    print("✓ test_validate_input passed")

def run_all_tests():
    """Chạy tất cả các kiểm thử / Run all tests"""
    print("Đang chạy kiểm thử... / Running tests...")
    test_calculate_sum()
    test_format_message()
    test_validate_input()
    print("\nTất cả kiểm thử đã hoàn thành! / All tests passed!")

if __name__ == "__main__":
    run_all_tests()
