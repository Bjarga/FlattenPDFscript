import os
import fitz  # PyMuPDF
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def convert_pdf_to_image_and_back(pdf_path, output_pdf_path):
    # Open the PDF using PyMuPDF
    pdf_document = fitz.open(pdf_path)
    
    # Create a new PDF
    c = canvas.Canvas(output_pdf_path, pagesize=letter)

    for i in range(pdf_document.page_count):
        page = pdf_document.load_page(i)
        
        # Convert the page to an image using PyMuPDF
        img = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Adjust scaling as needed
        
        # Save the image as a jpeg
        img_path = f"temp_{i}.jpg"
        img.save(img_path, 'JPEG')

        # Draw this image on the PDF.
        c.drawImage(img_path, 0, 0, width=600, height=800)  # adjust width and height as needed

        # Start the next page
        c.showPage()

    # Save the PDF
    c.save()

# Source and destination folder names
source_folder = "QC_reports_2023"
destination_folder = "QC_reports_2023_flat"

# Loop through all files in the source directory
for filename in os.listdir(source_folder):
    # Check if the file is a PDF
    if filename.endswith(".pdf"):
        # Create the full paths for the source and destination files
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Process the file
        convert_pdf_to_image_and_back(source_path, destination_path)
