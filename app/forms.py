from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

class RunForm(FlaskForm):
    distance = DecimalField('Distance (mi)', validators=[DataRequired()])
    pace = DecimalField('Minutes per Mile', validators=[DataRequired()])
    submit = SubmitField('Submit run data')
