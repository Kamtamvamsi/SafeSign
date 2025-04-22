# PDF report generator
from fpdf import FPDF
import os
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "SafeSign Forensic Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def create_pdf_report(file_path, detection_type, result_summary):
    file_name = os.path.basename(file_path)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    pdf = PDF()
    pdf.add_page()

    pdf.set_font("Arial", "", 12)
    pdf.ln(10)
    pdf.cell(200, 10, f"File Analyzed: {file_name}", ln=True)
    pdf.cell(200, 10, f"Detection Type: {detection_type}", ln=True)
    pdf.cell(200, 10, f"Timestamp: {now}", ln=True)

    pdf.ln(10)
    pdf.multi_cell(0, 10, f"Summary:\n{result_summary}")

    output_path = f"uploads/{file_name}_report.pdf"
    pdf.output(output_path)

    return output_path
