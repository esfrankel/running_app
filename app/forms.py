from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class RunForm(FlaskForm):
    distance = FloatField('Distance (mi)', validators=[DataRequired()])
    pace = FloatField('Minutes per Mile', validators=[DataRequired()])
    latitude = FloatField('Latitude', validators=[DataRequired()])
    longitude = FloatField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Submit run data')
