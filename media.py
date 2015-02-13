import webbrowser

class Video():
	""" This class will store title and duration information shared with children classes. """
	def __init__(self, video_title, video_duration):
		self.title = video_title
		self.duration = video_duration
		

class Movie(Video):
	""" This class will store movie related information. """
	def __init__(self, video_title, video_duration, movie_storyline, poster_image, trailer_youtube, movie_release_date):
		Video.__init__(self, video_title, video_duration)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.release_date = movie_release_date
		
	#Calls webbrowser method 'open' to open movie trailer url	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)