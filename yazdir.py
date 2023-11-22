import os
from PyPDF2 import PdfReader

def write_pdf_titles_to_txt(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for filename in os.listdir(folder_path):
            if filename.endswith('.pdf'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'rb') as pdf_file:
                    pdf = PdfReader(pdf_file)
                    title = pdf.metadata.title
                    if title:
                        file.write(f'{filename}: {title}\n')
                    else:
                        file.write(f'{filename}: No title\n')

folder_path = '/Users/ilayda/Desktop/PDF'
output_file = 'pdf_titles.txt'
write_pdf_titles_to_txt(folder_path, output_file)

