from models import Venue, Artist, Show


def run(db):
	if Venue.query.count() > 0:
		print("The DB contains already some data")
		return
	
	data1 = Venue()
	data1.name = "The Musical Hop"
	data1.genres = ["Jazz", "Reggae", "Swing", "Classical", "Folk"]
	data1.address = "1015 Folsom Street"
	data1.city = "San Francisco"
	data1.state = "CA"
	data1.phone = "123-123-1234"
	data1.website = "https://www.themusicalhop.com"
	data1.facebook_link = "https://www.facebook.com/TheMusicalHop"
	data1.seeking_talent = True
	data1.seeking_description = "We are on the lookout for a local artist to play every two weeks. Please call us."
	data1.image_link = "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
	
	data2 = Venue()
	data2.name = "The Dueling Pianos Bar"
	data2.genres = ["Classical", "R&B", "Hip-Hop"]
	data2.address = "335 Delancey Street"
	data2.city = "New York"
	data2.state = "NY"
	data2.phone = "914-003-1132"
	data2.website = "https://www.theduelingpianos.com"
	data2.facebook_link = "https://www.facebook.com/theduelingpianos"
	data2.seeking_talent = False
	data2.image_link = "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"
	
	data3 = Venue()
	data3.name = "Park Square Live Music & Coffee"
	data3.genres = ["Rock n Roll", "Jazz", "Classical", "Folk"]
	data3.address = "34 Whiskey Moore Ave"
	data3.city = "San Francisco"
	data3.state = "CA"
	data3.phone = "415-000-1234"
	data3.website = "https://www.parksquarelivemusicandcoffee.com"
	data3.facebook_link = "https://www.facebook.com/ParkSquareLiveMusicAndCoffee"
	data3.seeking_talent = False
	data3.image_link = "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"
	
	artist4 = Artist()
	artist4.name = "Guns N Petals"
	artist4.genres = ["Rock n Roll"]
	artist4.city = "San Francisco"
	artist4.state = "CA"
	artist4.phone = "326-123-5000"
	artist4.website = "https://www.gunsnpetalsband.com"
	artist4.facebook_link = "https://www.facebook.com/GunsNPetals"
	artist4.seeking_venue = True
	artist4.seeking_description = "Looking for shows to perform at in the San Francisco Bay Area!"
	artist4.image_link = "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"

	artist5 = Artist()
	artist5.name = "Matt Quevedo"
	artist5.genres = ["Jazz"]
	artist5.city = "New York"
	artist5.state = "NY"
	artist5.phone = "300-400-5000"
	artist5.facebook_link = "https://www.facebook.com/mattquevedo923251523"
	artist5.seeking_venue = False
	artist5.image_link = "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80"
	
	artist6 = Artist()
	artist6.name = "The Wild Sax Band"
	artist6.genres = ["Jazz", "Classical"]
	artist6.city = "San Francisco"
	artist6.state = "CA"
	artist6.phone = "432-325-5432"
	artist6.seeking_venue = False
	artist6.image_link = "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80"

	show1 = Show(venue=data1, artist=artist4, start_time="2019-05-21T21:30:00.000Z")
	show2 = Show(venue=data3, artist=artist5, start_time="2019-06-15T23:00:00.000Z")
	show3 = Show(venue=data3, artist=artist6, start_time="2035-04-01T20:00:00.000Z")
	show4 = Show(venue=data3, artist=artist6, start_time="2035-04-08T20:00:00.000Z")
	show5 = Show(venue=data3, artist=artist6, start_time="2035-04-15T20:00:00.000Z")

	db.session.add_all([data1, data2, data3, artist4, artist5, artist6])
	db.session.commit()
