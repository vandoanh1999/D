# Cấu trúc dự án / Project Structure

## Tổng quan / Overview

Dự án D được tổ chức theo cấu trúc thư mục rõ ràng để dễ dàng quản lý và phát triển.
The D project is organized with a clear folder structure for easy management and development.

## Cấu trúc thư mục / Directory Structure

```
D/
├── src/                    # Mã nguồn chính / Main source code
│   ├── __init__.py        # Package initialization
│   ├── main.py            # Tệp chính / Main file
│   └── utils.py           # Các hàm tiện ích / Utility functions
│
├── tests/                  # Kiểm thử / Tests
│   ├── __init__.py        # Test package initialization
│   └── test_utils.py      # Kiểm thử utils / Utils tests
│
├── config/                 # Cấu hình / Configuration
│   ├── __init__.py        # Config package initialization
│   └── settings.py        # Cài đặt / Settings
│
├── examples/               # Ví dụ / Examples
│   └── example_usage.py   # Ví dụ sử dụng / Usage examples
│
├── docs/                   # Tài liệu / Documentation
│   └── STRUCTURE.md       # Tài liệu này / This document
│
├── .gitignore             # Git ignore file
├── LICENSE                # Giấy phép / License
└── README.md              # Tài liệu chính / Main documentation
```

## Mô tả thư mục / Directory Descriptions

### `src/`
Chứa toàn bộ mã nguồn chính của dự án.
Contains all main source code of the project.

### `tests/`
Chứa các tệp kiểm thử để đảm bảo chất lượng mã.
Contains test files to ensure code quality.

### `config/`
Chứa các tệp cấu hình cho dự án.
Contains configuration files for the project.

### `examples/`
Chứa các ví dụ minh họa cách sử dụng dự án.
Contains examples demonstrating how to use the project.

### `docs/`
Chứa tài liệu chi tiết về dự án.
Contains detailed documentation about the project.

## Hướng dẫn sử dụng / Usage Guide

### Chạy chương trình chính / Run main program:
```bash
python src/main.py
```

### Chạy kiểm thử / Run tests:
```bash
python tests/test_utils.py
```

### Chạy ví dụ / Run examples:
```bash
python examples/example_usage.py
```
