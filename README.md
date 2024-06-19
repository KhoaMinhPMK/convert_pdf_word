
# Hướng Dẫn Sử Dụng Mã Chia Nhỏ File PDF

## Giới Thiệu
Mã nguồn này sử dụng thư viện PyPDF2 để chia một file PDF lớn thành nhiều file nhỏ hơn dựa trên các khoảng trang mà bạn chỉ định.

## Yêu Cầu
- Python 3.x
- Thư viện PyPDF2

Bạn có thể cài đặt PyPDF2 bằng cách chạy lệnh sau:
```sh
pip install PyPDF2
```

## Hướng Dẫn Sử Dụng

### Bước 1: Chuẩn Bị File PDF Đầu Vào
- Đảm bảo bạn có sẵn file PDF mà bạn muốn chia nhỏ.
- Xác định đường dẫn tới file PDF này.

### Bước 2: Xác Định Các Khoảng Trang
- Xác định các khoảng trang bạn muốn chia. Ví dụ: `[(1, 20), (21, 46), (47, 72)]`.

### Bước 3: Chạy Mã Nguồn
- Thay đổi các tham số trong phần ví dụ sử dụng sao cho phù hợp với trường hợp của bạn.

### Ví Dụ Sử Dụng
```python
import PyPDF2

def split_pdf(input_pdf, page_ranges, output_prefix):
    # Mở file PDF đầu vào
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i, (start, end) in enumerate(page_ranges):
            writer = PyPDF2.PdfWriter()
            for page_num in range(start - 1, end):
                writer.add_page(reader.pages[page_num])
            # Lưu file PDF mới
            output_pdf = f"{output_prefix}_{i+1}.pdf"
            with open(output_pdf, 'wb') as output_file:
                writer.write(output_file)
            print(f"Tạo file {output_pdf} từ trang {start} đến trang {end}")

# Ví dụ sử dụng:
input_pdf = 'C:\Users\fujitsu\Desktop\AI_main\pdf\a.pdf'  # Đường dẫn tới file PDF đầu vào
page_ranges = [(1, 20), (21, 46), (47, 72), (73, 135), (136, 188)]  # Các khoảng trang bạn muốn chia
output_prefix = 'C:\Users\fujitsu\Desktop\AI_main\pdf\output'  # Tiền tố cho các file đầu ra

split_pdf(input_pdf, page_ranges, output_prefix)
```

### Kết Quả
- Các file PDF đầu ra sẽ được lưu với định dạng `output_prefix_i.pdf` trong thư mục được chỉ định.

### Liên Hệ
Nếu có bất kỳ vấn đề gì, vui lòng liên hệ với [pmkkhoaminh@gmail.com] để được hỗ trợ.
