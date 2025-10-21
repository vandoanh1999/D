"""
Utility functions for D project
Các hàm tiện ích cho dự án D
"""

def calculate_sum(a, b):
    """
    Tính tổng hai số
    Calculate sum of two numbers
    
    Args:
        a (int/float): Số thứ nhất / First number
        b (int/float): Số thứ hai / Second number
    
    Returns:
        int/float: Tổng của hai số / Sum of two numbers
    """
    return a + b

def format_message(message, name):
    """
    Định dạng thông điệp
    Format a message
    
    Args:
        message (str): Thông điệp / Message
        name (str): Tên / Name
    
    Returns:
        str: Thông điệp đã định dạng / Formatted message
    """
    return f"{message}, {name}!"

def validate_input(value):
    """
    Kiểm tra tính hợp lệ của đầu vào
    Validate input value
    
    Args:
        value: Giá trị cần kiểm tra / Value to validate
    
    Returns:
        bool: True nếu hợp lệ, False nếu không / True if valid, False otherwise
    """
    if value is None or value == "":
        return False
    return True
