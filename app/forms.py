from collections.abc import Iterable
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import TextAreaField, SubmitField
from wtforms.fields import MultipleFileField
from werkzeug.datastructures import FileStorage
from wtforms.validators import StopValidation

class MultipleFileAllowed():
    """Implements Flask-WTF's FileAllowed validation for a MultipleFileField"""
    def __init__(self, upload_set, message=None):
        self.upload_set = upload_set
        self.message = message

    def __call__(self, form, field):
        if not (all(isinstance(item, FileStorage) for item in field.data) and field.data):
            return
        
        for data in field.data:
            filename = data.filename.lower()

            if isinstance(self.upload_set, Iterable):
                if any(filename.endswith('.' + x) for x in self.upload_set):
                    return

                raise StopValidation(self.message or field.gettext(
                    'File does not have an approved extension: {extensions}'
                ).format(extensions=', '.join(self.upload_set)))

            if not self.upload_set.file_allowed(field.data, filename):
                raise StopValidation(self.message or field.gettext(
                    'File does not have an approved extension.'
                ))
        

class UploadForm(FlaskForm):
    screenshots = MultipleFileField('Project Screenshots', validators=[FileRequired(), MultipleFileAllowed(['.jpg', '.png', '.jpeg', '.tif'])])
    optional_context = TextAreaField('Optional Context')
    # TO-DO: Add ReCaptcha v2 
    submit = SubmitField('Describe Test Instructions')