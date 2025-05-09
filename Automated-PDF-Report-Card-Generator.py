import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_report_cards(file_path):
    try:
        data = pd.read_excel(file_path)
        required_columns = {'Student ID', 'Name', 'Subject', 'Score'}

        if not required_columns.issubset(data.columns):
            missing = required_columns - set(data.columns)
            raise ValueError(f"Missing required columns: {missing}")

        grouped = data.groupby('Student ID')
        for student_id, group in grouped:
            total_score = group['Score'].sum()
            average_score = group['Score'].mean()
            student_name = group['Name'].iloc[0]

            subject_scores = group[['Subject', 'Score']].values.tolist()
            subject_scores.insert(0, ['Subject', 'Score'])

            file_name = f"report_card_{student_id}.pdf"
            pdf = SimpleDocTemplate(file_name, pagesize=letter)
            elements = []
            styles = getSampleStyleSheet()

            elements.append(Paragraph(f"Report Card for {student_name}", styles['Title']))
            elements.append(Paragraph(f"Student ID: {student_id}", styles['Normal']))
            elements.append(Paragraph(f"Total Score: {total_score}", styles['Normal']))
            elements.append(Paragraph(f"Average Score: {average_score:.2f}", styles['Normal']))

            table = Table(subject_scores)
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
            pdf.build(elements)
            print(f"Report card generated: {file_name}")

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except ValueError as ve:
        print(f"Data Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
generate_report_cards("student_scores.xlsx")
