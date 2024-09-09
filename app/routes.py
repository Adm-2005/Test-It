import os
from app import app
from app.forms import UploadForm
from werkzeug.utils import secure_filename
from flask import render_template, request, jsonify
from services.instruction_generation import generate_instructions

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