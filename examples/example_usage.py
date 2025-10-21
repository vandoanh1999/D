#!/usr/bin/env python3
"""
Example usage of D project modules
Ví dụ sử dụng các module của dự án D
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import calculate_sum, format_message, validate_input

def example_1():
    """Ví dụ 1: Tính toán đơn giản / Example 1: Simple calculation"""
    print("=== Ví dụ 1: Tính toán / Example 1: Calculation ===")
    result = calculate_sum(10, 20)
    print(f"10 + 20 = {result}")
    print()

def example_2():
    """Ví dụ 2: Định dạng thông điệp / Example 2: Message formatting"""
    print("=== Ví dụ 2: Định dạng thông điệp / Example 2: Message Formatting ===")
    message = format_message("Chào bạn", "Việt Nam")
    print(message)
    print()

def example_3():
    """Ví dụ 3: Kiểm tra đầu vào / Example 3: Input validation"""
    print("=== Ví dụ 3: Kiểm tra đầu vào / Example 3: Input Validation ===")
    
    test_values = ["valid", "", None, 123]
    for value in test_values:
        is_valid = validate_input(value)
        print(f"Giá trị / Value: {value} -> Hợp lệ / Valid: {is_valid}")
    print()

if __name__ == "__main__":
    print("Chương trình ví dụ cho dự án D")
    print("Example program for D project")
    print("=" * 50)
    print()
    
    example_1()
    example_2()
    example_3()
    
    print("=" * 50)
    print("Hoàn thành! / Completed!")
