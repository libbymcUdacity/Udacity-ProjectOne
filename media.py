import webbrowser

class Movie():
    # Defining class init, creates space in memory to remember title, etc. for movies
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_release):
        # Initializing pieces of informatin to remember inside of class
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release = movie_release
    # Defining new function, show_trailer    
    def show_trailer(self):
        # Open the web browser with the correct URL, stored in instance variable trailer_youtube_url
        webbrowser.open(self.trailer_youtube_url)
