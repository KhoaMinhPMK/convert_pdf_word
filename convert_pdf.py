import pdfplumber
import re
import csv
from docx import Document

def preprocess_text(text):
    # Chuyển thành chữ thường
    text = text.lower()
    # Xóa kí tự đặc biệt dấu câu
    text = re.sub(r'[^\w\s]', '', text)
    return text

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
            text += "\n"
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text
        text += "\n"
    return text

def extract_problems_from_text(text):
    problems = []
    # Xử lý văn bản trích xuất để đảm bảo nó không bị ngắt dòng không mong muốn
    text = text.replace('\n', ' ')
    # Tìm tất cả các đoạn văn bản bắt đầu bằng "Bài" kết thúc trước "Lời giải"
    matches = re.findall(r'(Bài \d+.*?)(?=Lời giải)', text, re.DOTALL)
    for match in matches:
        # Loại bỏ từ "Bài ... ." ở đầu "Lời giải" ở cuối
        match = re.sub(r'Bài \d+\.\s*', '', match)
        match = re.sub(r'Lời giải.*', '', match)
        # Tiền xử lý văn bản
        match = preprocess_text(match)
        problems.append(match)
    return problems

def save_problems_to_csv(problems, file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['label', 'problem'])
        for problem in problems:
            writer.writerow(['bài toán hóa học', problem])

def extract_problems_from_file(file_path):
    if file_path.lower().endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format")
    
    problems = extract_problems_from_text(text)
    return problems

# Đường dẫn đến file cần xử lý
file_path = 'output_5.pdf'  # hoặc 'output_5.docx'
# Đường dẫn đến file CSV
csv_file_path = 'output/op5.csv'

# Trích xuất các bài toán từ file
problems = extract_problems_from_file(file_path)

# Lưu các bài toán vào file CSV
save_problems_to_csv(problems, csv_file_path)
