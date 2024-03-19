#! /usr/bin/env python3

import os
import requests


def process_text_files(directory):
    fruits_data = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r") as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = int(lines[1].strip(" lbs\n"))
                description = lines[2].strip()
                image_name = os.path.splitext(filename)[0] + ".jpeg"
                fruit = {
                    "name": name,
                    "weight": weight,
                    "description": description,
                    "image_name": image_name
                }
                fruits_data.append(fruit)

    return fruits_data


def upload_fruits_data(fruits_data, url):
    for fruit in fruits_data:
        response = requests.post(url, json=fruit)
        if response.status_code == 201:
            print(f"Successfully uploaded {fruit['name']} data.")
        else:
            print(f"Failed to upload {fruit['name']} data. Status code: {response.status_code}")


if __name__ == "__main__":
    descriptions_dir = "~/supplier-data/descriptions"
    url = "http://[linux-instance-external-IP]/fruits"

    # Expand the home directory path
    descriptions_dir = os.path.expanduser(descriptions_dir)

    # Process text files and get fruits data
    fruits_data = process_text_files(descriptions_dir)

    # Upload fruits data
    upload_fruits_data(fruits_data, url)
