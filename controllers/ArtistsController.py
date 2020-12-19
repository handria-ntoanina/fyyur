from flask import render_template, request, flash, redirect, url_for
from forms.ArtistForm import ArtistForm
from initializer import app, db
from models import Artist
import traceback

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
	data = Artist.query.order_by(Artist.name).all()
	return render_template('pages/artists.html', artists=data)


@app.route('/artists/search', methods=['POST'])
def search_artists():
	search_term = request.form.get('search_term', '')
	query = Artist.query.filter(Artist.name.ilike(f'%{search_term}%')).order_by(Artist.name)
	response = {
		"count": query.count(),
		"data": query.all()
	}
	
	return render_template('pages/search_artists.html', results=response, search_term=search_term)


@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
	data = Artist.query.get(artist_id)
	return render_template('pages/show_artist.html', artist=data)


#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
	form = ArtistForm()
	artist = {
		"id": 4,
		"name": "Guns N Petals",
		"genres": ["Rock n Roll"],
		"city": "San Francisco",
		"state": "CA",
		"phone": "326-123-5000",
		"website": "https://www.gunsnpetalsband.com",
		"facebook_link": "https://www.facebook.com/GunsNPetals",
		"seeking_venue": True,
		"seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
		"image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"
	}
	# TODO: populate form with fields from artist with ID <artist_id>
	return render_template('forms/edit_artist.html', form=form, artist=artist)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
	# TODO: take values from the form submitted, and update existing
	# artist record with ID <artist_id> using the new attributes
	
	return redirect(url_for('show_artist', artist_id=artist_id))


#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
	form = ArtistForm()
	return render_template('forms/new_artist.html', form=form)


@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
	try:
		artist = Artist()
		artist.name = request.form['name']
		artist.city = request.form['city']
		artist.state = request.form['state']
		artist.phone = request.form['phone']
		artist.image_link = request.form['image_link']
		artist.facebook_link = request.form['facebook_link']
		artist.genres = request.form.getlist('genres')
		artist.website = request.form['website']
		artist.seeking_venue = 'seeking_venue' in request.form
		artist.seeking_description = request.form['seeking_description']
		db.session.add(artist)
		db.session.commit()
		flash('Artist ' + request.form['name'] + ' was successfully listed!')
	except:
		db.session.rollback()
		traceback.print_exc()
		flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
	finally:
		db.session.close()
	
	return render_template('pages/home.html')
