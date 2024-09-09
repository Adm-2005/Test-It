import os
from PIL import Image
from flask import Flask
from config import Config
from transformers import BlipProcessor, Blip2ForConditionalGeneration

app = Flask(__name__)
app.config.from_object(Config)

if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

processor = BlipProcessor.from_pretrained("Salesforce/blip2-flan-t5-base")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-flan-t5-base")

from app import routes