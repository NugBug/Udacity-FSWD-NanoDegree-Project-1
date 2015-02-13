import video_db
import media

toy_story = media.Movie("Toy Story", 
					    "81 min",
						"A story of a boy and his toys that come to life, but the boy has no clue how awesome his toys are.",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"http://www.youtube.com/watch?v=vwyZH85NQC4",
						"1995")

avatar = media.Movie("Avatar",
					 "162 min",
					 "A marine on an alien planet that turns into a really big blue alien.",
					 "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY",
					 "2009")
					 
the_thing = media.Movie("The Thing",
					 "109 min",
					 "A weird alien tricks people into thinking he is their friend.",
					 "http://upload.wikimedia.org/wikipedia/en/c/c1/ThingPoster.jpg",
					 "https://www.youtube.com/watch?v=ouZkkIsLiNg",
					 "1982")
					 
commando = media.Movie("Commando",
					 "90 min",
					 "A commando is upset some drug warlords and a Freddie Mercury look alike kidnapped Alyssa Milano.",
					 "http://upload.wikimedia.org/wikipedia/en/d/d9/Commandoposter.jpg",
					 "https://www.youtube.com/watch?v=pPhISgw3I2w",
					 "1985")
					 
army_of_darkness = media.Movie("Army of Darkness",
					 "81 min",
					 "You're good Ash!  I'm bad Ash!",
					 "http://upload.wikimedia.org/wikipedia/en/4/46/Army_of_Darkness_poster.jpg",
					 "https://www.youtube.com/watch?v=4vvJCg2JsIc",
					 "1992")
					 
die_hard = media.Movie("Die Hard",
					 "131 min",
					 "The best action movie ever made.  Ever.  It is also the best Christmas movie ever made.",
					 "http://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",
					 "https://www.youtube.com/watch?v=2TQ-pOvI6Xo",
					 "1988")
					 
movies = [toy_story, avatar, the_thing, commando, army_of_darkness, die_hard]
video_db.open_movies_page(movies)
