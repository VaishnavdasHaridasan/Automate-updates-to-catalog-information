#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date

def generate_report(attachment, title, paragraph):
    # Create a SimpleDocTemplate object with specified file path
    report = SimpleDocTemplate(attachment)
    # Define styles for the report
    styles = getSampleStyleSheet()
    # Create a title and date for the report
    report_title = Paragraph(title, styles["h1"])
    current_date = date.today().strftime("%B %d, %Y")
    report_date = Paragraph(f"Processed Update on {current_date}", styles["h3"])
    # Create a paragraph with the provided content
    report_paragraph = Paragraph(paragraph, styles["BodyText"])
    # Add elements to the report
    report_content = [report_title, report_date, Paragraph("<br/><br/>", styles["BodyText"]), report_paragraph]
    # Build the PDF report
    report.build(report_content)

if __name__ == "__main__":
    attachment = "/tmp/processed.pdf"
    title = "Processed Update"
    paragraph = """
    name: Apple<br/>
    weight: 500 lbs<br/>
    <br/>
    name: Avocado<br/>
    weight: 200 lbs<br/>
    """
    generate_report(attachment, title, paragraph)
