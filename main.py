import pdftitle
import os

def read_pdf_titles(folder_path):
    pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]
    for file in pdf_files:
        pdf_path = os.path.join(folder_path, file)
        title = pdftitle.get_title_from_file(pdf_path)
        print(title)

folder_path = "/Users/ilayda/Desktop/PDF"
