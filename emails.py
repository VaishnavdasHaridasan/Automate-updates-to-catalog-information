#!/usr/bin/env python3

import email.message
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):
    """Generates an email message with attachment."""
    # Create a basic email message
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Add attachment if provided
    if attachment_path:
        filename = os.path.basename(attachment_path)
        with open(attachment_path, "rb") as attachment_file:
            message.add_attachment(
                attachment_file.read(),
                maintype="application",
                subtype="octet-stream",
                filename=filename
            )

    return message

def send_email(email_message):
    """Sends the email message."""
    # Connect to SMTP server
    mail_server = smtplib.SMTP('localhost')
    # Send email
    mail_server.send_message(email_message)
    # Close connection
    mail_server.quit()
