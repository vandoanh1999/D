# D - Copilot Operations Demo

Dự án demo hỗ trợ GitHub Copilot với các thao tác cơ bản / Project demonstrating GitHub Copilot support with basic operations.

## Mô tả / Description

Repository này chứa các ví dụ về cách sử dụng GitHub Copilot để hỗ trợ phát triển phần mềm với các thao tác cơ bản.

This repository contains examples of how to use GitHub Copilot to support software development with basic operations.

## Tính năng / Features

- ✅ Các phép toán số học cơ bản (cộng, trừ, nhân, chia)
- ✅ Các thao tác chuỗi (nối chuỗi, đảo ngược)
- ✅ Mã nguồn có comment rõ ràng cho Copilot
- ✅ Unit tests đầy đủ
- ✅ Hỗ trợ tiếng Việt

## Cài đặt / Installation

```bash
# Clone repository
git clone https://github.com/vandoanh1999/D.git
cd D

# Cài đặt dependencies (nếu muốn chạy tests)
pip install -r requirements.txt
```

## Sử dụng / Usage

### Chạy chương trình demo / Run demo program:

```bash
python operations.py
```

### Chạy tests / Run tests:

```bash
pytest test_operations.py -v
```

## Hỗ trợ Copilot / Copilot Support

Dự án này được thiết kế để làm việc tốt với GitHub Copilot:

- Tất cả hàm đều có docstrings rõ ràng
- Code được tổ chức logic và dễ đọc
- Tests có tên và mô tả rõ ràng
- Comments hỗ trợ Copilot đề xuất code

This project is designed to work well with GitHub Copilot:

- All functions have clear docstrings
- Code is organized logically and readable
- Tests have clear names and descriptions
- Comments support Copilot code suggestions

## Cấu trúc dự án / Project Structure

```
D/
├── operations.py       # Module chứa các thao tác cơ bản
├── test_operations.py  # Unit tests cho operations module
├── requirements.txt    # Python dependencies
├── README.md          # Tài liệu dự án
├── LICENSE            # MIT License
└── .gitignore         # Git ignore file
```

## License

MIT License - Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

---

🇻🇳 Made in Việt Nam 
