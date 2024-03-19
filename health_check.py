#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
import os

def check_cpu_usage():
    """Check CPU usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage > 80

def check_disk_space():
    """Check available disk space."""
    disk_usage = shutil.disk_usage("/")
    disk_space_percent = disk_usage.free / disk_usage.total * 100
    return disk_space_percent < 20

def check_memory():
    """Check available memory."""
    available_memory = psutil.virtual_memory().available / (1024 ** 2)  # Convert to MB
    return available_memory < 500

def check_hostname_resolution():
    """Check if hostname "localhost" resolves to "127.0.0.1"."""
    try:
        localhost_ip = socket.gethostbyname("localhost")
        return localhost_ip != "127.0.0.1"
    except:
        return True

def main():
    """Main function to check system health and send email if needed."""
    error_messages = []

    # Check CPU usage
    if check_cpu_usage():
        error_messages.append("Error - CPU usage is over 80%")

    # Check disk space
    if check_disk_space():
        error_messages.append("Error - Available disk space is less than 20%")

    # Check available memory
    if check_memory():
        error_messages.append("Error - Available memory is less than 500MB")

    # Check hostname resolution
    if check_hostname_resolution():
        error_messages.append("Error - localhost cannot be resolved to 127.0.0.1")

    # Send email if there are any errors
    if error_messages:
        error_message = "\n".join(error_messages)
        subject = "Error - Health Check"
        body = "Please check your system and resolve the issue as soon as possible."
        emails.generate_email("automation@example.com", os.getenv('USER') + "@example.com", subject, body)
        print("Email sent!")

if __name__ == "__main__":
    main()
