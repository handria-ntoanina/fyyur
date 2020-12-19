from flask import render_template, flash
from forms.ShowForm import ShowForm
from initializer import app
from models import Show

#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
	data = Show.query.order_by(Show.start_time).all()
	return render_template('pages/shows.html', shows=data)


@app.route('/shows/create')
def create_shows():
	# renders form. do not touch.
	form = ShowForm()
	return render_template('forms/new_show.html', form=form)


@app.route('/shows/create', methods=['POST'])
def create_show_submission():
	# called to create new shows in the db, upon submitting new show listing form
	# TODO: insert form data as a new Show record in the db, instead
	
	# on successful db insert, flash success
	flash('Show was successfully listed!')
	# TODO: on unsuccessful db insert, flash an error instead.
	# e.g., flash('An error occurred. Show could not be listed.')
	# see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
	return render_template('pages/home.html')
