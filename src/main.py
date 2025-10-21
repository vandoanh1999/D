#!/usr/bin/env python3
"""
Main application file for D project
Tệp chính của dự án D
"""

def main():
    """
    Hàm chính của chương trình
    Main function of the program
    """
    print("Chào mừng đến với dự án D!")
    print("Welcome to D project!")
    
    # Gọi các chức năng khác
    greet_user("Người dùng")

def greet_user(name):
    """
    Chào người dùng
    Greet the user
    
    Args:
        name (str): Tên người dùng / User name
    """
    print(f"Xin chào, {name}!")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
