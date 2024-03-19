#!/usr/bin/env python3

import requests
import os

# Define the URL of the web server where images will be uploaded
UPLOAD_URL = "http://[linux-instance-IP-Address]/upload"

# Define the directory containing the modified JPEG images
IMAGE_DIRECTORY = "/home/<username>/supplier-data/images"

def upload_images():
    # Iterate through each file in the image directory
    for filename in os.listdir(IMAGE_DIRECTORY):
        # Check if the file is a JPEG image
        if filename.endswith(".jpeg"):
            # Construct the full path to the image file
            filepath = os.path.join(IMAGE_DIRECTORY, filename)
            # Open the image file in binary mode
            with open(filepath, "rb") as file:
                # Prepare the file data to be sent in the POST request
                files = {"file": file}
                # Send a POST request to upload the image to the web server
                response = requests.post(UPLOAD_URL, files=files)
                # Check if the upload was successful
                if response.status_code == 201:
                    print(f"Uploaded {filename} successfully.")
                else:
                    print(f"Failed to upload {filename}.")

if __name__ == "__main__":
    upload_images()
