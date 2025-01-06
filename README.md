# **Automated Report Generator**

**Name:** Soham Dutta  
**Company:** CODTECH IT Solutions  
**ID:** CT08EIL  
**Domain:** Python Programming  

---

## **Objective**  
Develop a Python application that automates the generation of internship completion reports in PDF format. The program reads data from a CSV file and structures it into a professional and visually appealing document.

---

## **Key Features**

1. **CSV Data Reading**  
   - Reads tabular data from a specified CSV file using Python's `csv` module.

2. **PDF Report Generation**  
   - Utilizes **ReportLab** to generate a polished PDF report.  
   - Includes:  
     - A dynamic title for the report.  
     - A personalized completion certificate statement with the specified date.  
     - A table displaying the data from the CSV file.

3. **Styling and Formatting**  
   - Professional styling with ReportLab's **TableStyle** and `Paragraph` objects.  
   - Highlights:  
     - Header row styled with a grey background and white text.  
     - Gridlines and beige background for table rows.  
   - Adjustable font styles for headers, body text, and table elements.

4. **Customizable Output**  
   - The program allows users to specify:  
     - The input CSV file.  
     - The output PDF file path.  
     - A title for the report.  
     - The completion date for the internship certificate.

5. **Reusability**  
   - Modular functions for reading CSV data and generating PDFs, enabling easy customization and integration.

---

## **Technologies Used**

- **Python Modules:**  
  - **`csv`**: Reads data from CSV files.  
  - **`reportlab`**: Generates professional PDF reports with tables, styles, and text elements.

---

## **Outcome**

The application provides an efficient solution for creating internship completion reports with a professional appearance. It saves time and effort while ensuring accuracy and consistency in report formatting.

---

## **Sample Use Case**

1. Input CSV File: `sample_data.csv`  
   - Contains tabular data such as internship details or performance metrics.  
2. Output PDF File: `internship_report.pdf`  
   - A professionally styled report generated with the provided title and completion date.  

---

## Screenshot

![sample-data](https://github.com/user-attachments/assets/3e499540-3383-4331-abae-b56fc4e57413)

![sample-data-pdf](https://github.com/user-attachments/assets/603aaa76-617c-4877-aed3-29e36981d011)
