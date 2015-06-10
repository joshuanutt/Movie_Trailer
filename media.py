import webbrowser

class Video():
	#__doc__
	""" this class stores infromation related to all videos """

	def __init__(self, title, summary):
		self.title = title
		self.summary = summary


class Movie(Video):
	# __doc__
	""" This class provides a way to store movie related information """

	def __init__(self, title, summary, poster_image, trailer_youtube):
		self.title = title
		self.summary = summary
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
