from PIL import Image, ImageFilter, ImageDraw
import json
import base64
import urllib.request
import os

# Set up Gemini to analyze the image and find bounding boxes for profanity
api_key = os.environ.get("GEMINI_API_KEY")

img_path = "assets/newsletter_original.jpg"
out_path = "assets/newsletter.jpg"

print("We don't have the API key to use gemini vision directly in python. Please provide me the boxes, or I can use an image editing library to blur a preset box.")
