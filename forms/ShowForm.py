from datetime import datetime
from flask_wtf import Form
from wtforms import IntegerField, DateTimeField
from wtforms.validators import DataRequired


class ShowForm(Form):
    artist_id = IntegerField(
        'artist_id',
        validators=[DataRequired()]
    )
    venue_id = IntegerField(
        'venue_id',
        validators=[DataRequired()]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default=datetime.today()
    )

