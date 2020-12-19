from flask import render_template, flash, request
from forms.ShowForm import ShowForm
from initializer import app, db
from models import Show
import traceback


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
	form = ShowForm()
	if not form.validate_on_submit():
		return render_template('forms/new_show.html', form=form)
	
	try:
		show = Show()
		show.artist_id = request.form['artist_id']
		show.venue_id = request.form['venue_id']
		show.start_time = request.form['start_time']
		db.session.add(show)
		db.session.commit()
		flash('Show was successfully listed!')
	except:
		db.session.rollback()
		traceback.print_exc()
		flash('An error occurred. Show could not be listed.')
	finally:
		db.session.close()
	
	return render_template('pages/home.html')
