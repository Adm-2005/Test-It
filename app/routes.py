import os
from app import app
from PIL import Image
from app import processor, model
from app.forms import UploadForm
from werkzeug.utils import secure_filename
from flask import render_template, request, jsonify

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if request.method == "POST":
        screenshots = request.files.getlist('screenshots')
        context = request.form.get('context', "")

        image_paths = []
        for file in screenshots:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            image_paths.append(filepath)

        instructions = generate_instructions(image_paths, context)
        return jsonify({'instructions': instructions})

    return render_template('index.html', form=form)

def generate_instructions(image_paths, context):
    prompt = f"You are a helpful assistant to a Quality Assurance Engineer, use the given images of the software and context:{context} to generate instructions to test the software that should include following details: 1.Description of the test case 2.Preconditions 3.Step-by-step instructions 4.Expected result"

    images = [Image.open(img_path) for img_path in image_paths]

    inputs = processor(images=images, text=prompt, return_tensors="pt")
    # inputs = {k: v.to(device) for k, v in inputs.items()}

    generated_ids = model.generate(pixel_values=inputs['pixel_values'], max_new_tokens=150)

    instructions = processor.decode(generated_ids[0], skip_special_tokens=True)

    return instructions