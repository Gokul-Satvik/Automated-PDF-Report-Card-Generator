# Automated-PDF-Report-Card-Generator
This Python project automates the creation of student report cards by reading data from an Excel file and generating personalized PDF reports. It utilizes the pandas library for data analysis and ReportLab for PDF creation.
Approach
  1. Read Data
    o Load the data from the Excel file using the pandas library.
    o Validate the presence of required columns: Student ID, Name, Subject, and
      Score.
  2. Process Data
    o Group the data by Student ID.
    o Calculate total and average scores for each student.
    o Prepare subject-wise scores for the table.
  3. Generate PDFs
    o Use the ReportLab library to create a PDF for each student.
    o Include student details: name, total score, average score, and subject-wise
      scores in a table.
  
  4. Save Files
    o Save the PDF files in the format report_card_<StudentID>.pdf.
  5. Error Handling
    o Handle missing files, columns, and invalid data gracefully.
