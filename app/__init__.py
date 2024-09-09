import os
from PIL import Image
from flask import Flask
from config import Config
from transformers import Blip2Processor, Blip2ForConditionalGeneration

app = Flask(__name__)
app.config.from_object(Config)

if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b")

from app import routes