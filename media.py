import webbrowser
#forcing it to open in Chrome. because good God who use safari or IE?
_chrome_launcher = webbrowser.get('open -a /Applications/Google\ Chrome.app %s')

class Movie():
    """Creating Movie class. Take movie title, story line, and
    link to poster image and trailer youtube"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        _chrome_launcher.open(self.trailer_youtube_url)