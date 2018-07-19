from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField
from wtforms.validators import DataRequired

class RunForm(FlaskForm):
    distance = DecimalField('Distance (mi)', validators=[DataRequired()])
    pace = DecimalField('Minutes per Mile', validators=[DataRequired()])
    latitude = DecimalField('Latitude', validators=[DataRequired()])
    longitude = DecimalField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Submit run data')
