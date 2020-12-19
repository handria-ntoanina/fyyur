from sqlalchemy import and_
from app import db
from datetime import datetime


# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

class Venue(db.Model):
	__tablename__ = 'Venue'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	city = db.Column(db.String(120))
	state = db.Column(db.String(120))
	address = db.Column(db.String(120))
	phone = db.Column(db.String(120))
	image_link = db.Column(db.String(500))
	facebook_link = db.Column(db.String(120))
	genres = db.Column(db.String(120))
	website = db.Column(db.String(120))
	seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
	seeking_description = db.Column(db.String())

	@property
	def past_shows(self):
		return Show.query.filter(and_(Show.venue_id == self.id, Show.start_time >= datetime.now())).all()
		
	@property
	def upcoming_shows(self):
		return Show.query.filter(and_(Show.venue_id == self.id, Show.start_time < datetime.now())).all()
	
	@property
	def past_shows_count(self):
		return Show.query.filter(and_(Show.venue_id == self.id, Show.start_time >= datetime.now())).count()
	
	@property
	def upcoming_shows_count(self):
		return Show.query.filter(and_(Show.venue_id == self.id, Show.start_time < datetime.now())).count()


class Artist(db.Model):
	__tablename__ = 'Artist'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	city = db.Column(db.String(120))
	state = db.Column(db.String(120))
	phone = db.Column(db.String(120))
	genres = db.Column(db.String(120))
	image_link = db.Column(db.String(500))
	facebook_link = db.Column(db.String(120))
	website = db.Column(db.String(120))
	seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
	seeking_description = db.Column(db.String())
	shows = db.relationship('Show', backref='artist', lazy=True, cascade='all, delete-orphan')
	past_shows = db.relationship('Todo', backref='list', lazy=True, cascade='all, delete-orphan')
	
	@property
	def past_shows(self):
		return Show.query.filter(and_(Show.artist_id == self.id, Show.start_time >= datetime.now())).all()
		
	@property
	def upcoming_shows(self):
		return Show.query.filter(and_(Show.artist_id == self.id, Show.start_time < datetime.now())).all()
	
	@property
	def past_shows_count(self):
		return Show.query.filter(and_(Show.artist_id == self.id, Show.start_time >= datetime.now())).count()
		
	@property
	def upcoming_shows_count(self):
		return Show.query.filter(and_(Show.artist_id == self.id, Show.start_time < datetime.now())).count()


class Show(db.Model):
	__tablename__ = 'Show'
	id = db.Column(db.Integer, primary_key=True)
	venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
	artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
	start_time = db.Column(db.DateTime, nullable=False)
