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
input_pdf = 'C:\\Users\\fujitsu\\Desktop\\AI_main\\pdf\\a.pdf'  # Đường dẫn tới file PDF đầu vào
page_ranges = [(1, 20), (21, 46), (47, 72), (73, 135), (136, 188)]  # Các khoảng trang bạn muốn chia
output_prefix = 'C:\\Users\\fujitsu\\Desktop\\AI_main\\pdf\\output'  # Tiền tố cho các file đầu ra

split_pdf(input_pdf, page_ranges, output_prefix)
