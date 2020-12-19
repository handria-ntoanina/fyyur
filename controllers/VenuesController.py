from flask import render_template, request, flash, redirect, url_for
from forms.VenueForm import VenueForm
from sqlalchemy import and_
from initializer import app, db
from models import Venue


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
	area = db.session.query(Venue.city, Venue.state).group_by(Venue.city, Venue.state).order_by(Venue.city, Venue.state).all()
	data = []
	
	class Area:
		city = ''
		state = ''
		venues = None
	for city, state in area:
		a = Area()
		a.city = city
		a.state = state
		a.venues = Venue.query.filter(and_(Venue.city == city, Venue.state == state)).order_by(Venue.name).all()
		data.append(a)
		
	return render_template('pages/venues.html', areas=data);


@app.route('/venues/search', methods=['POST'])
def search_venues():
	search_term = request.form.get('search_term', '')
	query = Venue.query.filter(Venue.name.ilike(f'%{search_term}%')).order_by(Venue.name)
	response = {
		"count": query.count(),
		"data": query.all()
	}
	
	return render_template('pages/search_venues.html', results=response, search_term=search_term)


@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
	# shows the venue page with the given venue_id
	return render_template('pages/show_venue.html', venue=Venue.query.get(venue_id))


#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
	form = VenueForm()
	return render_template('forms/new_venue.html', form=form)


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
	# TODO: insert form data as a new Venue record in the db, instead
	# TODO: modify data to be the data object returned from db insertion
	
	# on successful db insert, flash success
	flash('Venue ' + request.form['name'] + ' was successfully listed!')
	# TODO: on unsuccessful db insert, flash an error instead.
	# e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
	# see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
	return render_template('pages/home.html')


@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
	# TODO: Complete this endpoint for taking a venue_id, and using
	# SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
	
	# BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
	# clicking that button delete it from the db then redirect the user to the homepage
	db.session.delete(Venue.query.get(venue_id))
	db.session.commit()
	return redirect(url_for('index'))


@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
	form = VenueForm()
	venue = {
		"id": 1,
		"name": "The Musical Hop",
		"genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
		"address": "1015 Folsom Street",
		"city": "San Francisco",
		"state": "CA",
		"phone": "123-123-1234",
		"website": "https://www.themusicalhop.com",
		"facebook_link": "https://www.facebook.com/TheMusicalHop",
		"seeking_talent": True,
		"seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
		"image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
	}
	# TODO: populate form with values from venue with ID <venue_id>
	return render_template('forms/edit_venue.html', form=form, venue=venue)


@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
	# TODO: take values from the form submitted, and update existing
	# venue record with ID <venue_id> using the new attributes
	return redirect(url_for('show_venue', venue_id=venue_id))