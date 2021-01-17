import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

# To test this image repository, Google Vision API credentials are needed
# An account can be created on GCP to download the JSON credentials file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'vision_api.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()

text_to_search = input("Please enter text you want to find in the set of images: \n")
print("Thank you. Searching for text: " + text_to_search)

# This should be assigned to the 
directory = ''

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Loads the image into memory
        with io.open(filename, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        # Performs text detection on the image file
        responseText = client.text_detection(image=image)

        image_text = ""

        texts = responseText.text_annotations
        print('Text:')

        for i in range(len(texts)):
            if (i != 0):
                image_text += texts[i].description
                image_text += " "

        print(image_text)

        for word in image_text.split():
            if word == text_to_search:
                print("match found")

        

