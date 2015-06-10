# coding=utf-8
import media
import fresh_tomatoes

# information for some of my favorite movies in this format:
# Movie(Name, Summary, Poster, Trailer URL)

# Add your own movies here:

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

garbage_day = media.Movie("Silent Night, Deadly Night",
					 "GARBAGE DAY", 
					 "http://upload.wikimedia.org/wikipedia/en/7/72/Silent_night_deadly_night_part_2_%28VHS_cover%29.jpg",
					 "https://www.youtube.com/watch?v=i7gIpuIVE3k")

shawshank_redemption = media.Movie("Shawshank Redemption",
									"Morgan Freeman is in prison with some white dude",
									"http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
									"https://www.youtube.com/watch?v=6hB3S9bIaco")

hunger_games = media.Movie("The Hunter Games",
						   "SHE SHOOTS, WITH A BOW",
						   "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
						   "www.youtube.com/watch?v=4S9a5V9ODuY")
godfather_1 = media.Movie("The Godfather",
						  "Mafia guy does mafia things",
						  "http://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
						  "www.youtube.com/watch?v=sY1S34973zA")
bourne_identity = media.Movie("The Bourne Identity",
							  "Spy guy with amnesia beats everybody up with shaky camera",
							  "http://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
							  "https://www.youtube.com/watch?v=2tqK_3mKQUw")
pulp_fiction = media.Movie("Pulp Fiction",
						   "Nobody even knows. Samuel L Jackson does things",
						   "http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
						   "www.youtube.com/watch?v=wZBfmBvvotE")

con_air = media.Movie("Con Air",
					  "Nick Cage on a plane",
					  "http://upload.wikimedia.org/wikipedia/en/1/1d/Conairinternational.jpg",
					  "https://www.youtube.com/watch?v=WXgcE6_xfR0")

snakes = media.Movie("Snakes on a Plane",
					 "Samuel L Jackson rides in a plane for the first time",
					 "http://upload.wikimedia.org/wikipedia/en/4/41/SOAP_poster.jpg",
					 "https://www.youtube.com/watch?v=u6Squ9a2kO4")
castaway = 	media.Movie("Castaway",
					   "Tom Hanks Island Adventure",
					   "http://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg",
					   "https://www.youtube.com/watch?v=PJvosb4UCLs")


# Stop adding movies :)

# Creates a list of the favorite movies to for open_movies_page(movies) in fresh_tomatoes.py
# If you added movies put them at the end of this list.
movies = [toy_story, garbage_day,hunger_games,godfather_1,bourne_identity,pulp_fiction,con_air,snakes,castaway]

# creates the html file and opens it in a new tab
fresh_tomatoes.open_movies_page(movies)
