#import our libraries

from openai import OpenAI
from PIL import Image,ImageOps,ImageFilter
from io import BytesIO
import requests


# Set API key and prompt
client= OpenAI()

def main():
    while True:
        print("\n1. Generate an image with DALL-E")
        print("2. Create variations of an image")
        print("0. Exit")
        
        option = input("Choose an option: ")

        if option == "1":
            prompt = input("Enter the prompt for DALL-E: ")
            # Generate the image with DALL-E
            generate_image(prompt)
        elif option == "2":
            image_path = input("Enter the path of the image: ")
            # Open the image file
            create_variations(image_path)
        elif option == "0":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please enter a valid number.")