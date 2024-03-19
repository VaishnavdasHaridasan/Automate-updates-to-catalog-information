#!/usr/bin/env python3

from PIL import Image
import os


def process_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".tiff"):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    # Convert RGBA to RGB format if necessary
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')

                    # Resize the image
                    resized_img = img.resize((600, 400))

                    # Save the resized image as JPEG
                    output_filename = os.path.splitext(filename)[0] + '.jpeg'
                    output_filepath = os.path.join(directory, output_filename)
                    resized_img.save(output_filepath, 'JPEG')

                    print(f"Processed {filename} successfully.")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    images_directory = "~/supplier-data/images"
    process_images(images_directory)
