import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def read_data_from_file(file_path):

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def generate_pdf_report(data, output_path, title, completion_date):
  
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Adding title
    title_paragraph = Paragraph(f"<b>{title}</b>", styles['Title'])
    elements.append(title_paragraph)
    elements.append(Spacer(1, 12))

    # Adding completion certificate information
    completion_paragraph = Paragraph(
        f"<b>Completion Certificate</b><br/>" 
        f"This certifies completion of the internship on <b>{completion_date}</b>.",
        styles['BodyText']
    )
    elements.append(completion_paragraph)
    elements.append(Spacer(1, 24))

    # Creating table from data
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    # Building the PDF
    doc.build(elements)
    print(f"Report generated successfully: {output_path}")

if __name__ == "__main__":
    input_file = 'sample_data.csv'  
    output_file = 'internship_report.pdf'
    report_title = 'Automated Internship Report'
    completion_date = 'January 15, 2025'  

    # Reading data and generating report
    data = read_data_from_file(input_file)
    generate_pdf_report(data, output_file, report_title, completion_date)