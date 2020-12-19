from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import dateutil.parser
import babel

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

def format_datetime(value, format='medium'):
	date = dateutil.parser.parse(value)
	if format == 'full':
		format = "EEEE MMMM, d, y 'at' h:mma"
	elif format == 'medium':
		format = "EE MM, dd, y h:mma"
	# babel cannot find the local using LC_TIME
	return babel.dates.format_datetime(date, format, locale='en')


app.jinja_env.filters['datetime'] = format_datetime
