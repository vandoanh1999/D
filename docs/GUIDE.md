# Hướng dẫn phát triển / Development Guide

## Bắt đầu / Getting Started

### Yêu cầu / Requirements
- Python 3.6 hoặc cao hơn / Python 3.6 or higher

### Cài đặt / Installation
1. Clone repository:
   ```bash
   git clone https://github.com/vandoanh1999/D.git
   cd D
   ```

2. Cài đặt dependencies (nếu có):
   ```bash
   pip install -r requirements.txt
   ```

## Cách sử dụng / How to Use

### 1. Chạy chương trình chính / Run Main Program
```bash
python src/main.py
```

### 2. Chạy các ví dụ / Run Examples
```bash
python examples/example_usage.py
```

### 3. Chạy kiểm thử / Run Tests
```bash
python tests/test_utils.py
```

## Quy tắc đóng góp / Contribution Guidelines

1. Tạo branch mới cho tính năng / Create a new branch for features
2. Viết code rõ ràng và có chú thích / Write clear and commented code
3. Thêm kiểm thử cho code mới / Add tests for new code
4. Cập nhật tài liệu nếu cần / Update documentation if needed
5. Tạo Pull Request / Create a Pull Request

## Cấu trúc code / Code Structure

### Thêm chức năng mới / Adding New Features
1. Tạo module mới trong `src/`
2. Thêm kiểm thử trong `tests/`
3. Cập nhật tài liệu trong `docs/`
4. Thêm ví dụ trong `examples/`

### Quy ước đặt tên / Naming Conventions
- Tệp: `snake_case.py`
- Hàm: `snake_case()`
- Class: `PascalCase`
- Hằng số / Constants: `UPPER_CASE`

## Liên hệ / Contact
- GitHub: [@vandoanh1999](https://github.com/vandoanh1999)
