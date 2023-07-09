import os
from PyPDF2 import PdfMerger, PdfReader, PageObject

def combine_pdfs(directory, output_file):
    merger = PdfMerger()

    # Add table of contents page
    page = PageObject().create_blank_page(width=72, height=118)
    page_number = 0

    for file_name in os.listdir(directory):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(directory, file_name)

            # Add file to merger
            merger.append(file_path)

            # Add outline item to table of contents
            merger.add_outline_item(title=file_name, page_number=page_number)

            # Increment page number by the number of pages in the current file
            with open(file_path, 'rb') as f:
                pdf_reader = PdfReader(f)
                page_number += len(pdf_reader.pages)

    # Write combined PDF
    with open(output_file, 'wb') as f:
        merger.write(f)

    merger.close()

def main():
    directory = r'F:\pdfs\finra\series 6'
    output_file = 'combined.pdf'

    combine_pdfs(directory, output_file)

if __name__ == '__main__':
    main()
