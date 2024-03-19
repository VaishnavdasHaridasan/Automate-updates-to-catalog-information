#!/usr/bin/env python3

import os
import reports
import emails


def generate_email():
    # Generate a PDF report
    attachment = "/tmp/processed.pdf"
    title = "Processed Update"
    paragraph = """
    name: Apple<br/>
    weight: 500 lbs<br/>
    <br/>
    name: Avocado<br/>
    weight: 200 lbs<br/>
    """
    reports.generate_report(attachment, title, paragraph)

    # Generate an email
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.getenv('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    email = emails.generate_email(sender, recipient, subject, body, attachment)

    # Send the email
    emails.send_email(email)


if __name__ == "__main__":
    generate_email()
