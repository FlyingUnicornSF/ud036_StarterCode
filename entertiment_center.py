import fresh_tomatoes
import media
"""input to the movie object? making instances for Movie Class?"""

#adding the last airbender
airbender = media.Movie("The last airbender",
                        "the twelve-year old (chronologically 112) incarnation of the current Avatar and the eponymous",
                        "http://static.tvtropes.org/pmwiki/pub/images/ATLA_3829.jpg",
                        "https://www.youtube.com/watch?v=Rz7EsOua-D4")

"""adding pitch perfect. storyline was too long and was going off the text editor's screen. Looked longer than 80 
characters. Decided to shorten it. When put it into multiple lines, it has to be changed to triple double quotes."""
pitch_perfect = media.Movie("Picth Perfect",
                            """Beca, a freshman at Barden University, is cajoled into joining The Bellas, her
                            school's all-girls singing group. Injecting some much needed energy
                            into their repertoire, The Bellas take on their male rivals in a campus competition.""",
                            "http://static.tvtropes.org/pmwiki/pub/images/pitch_perfect_poster.jpg",
                            "https://www.youtube.com/watch?v=F03N-ApQdmw")
#adding grudge.
grudge = media.Movie("The Grudge",
                     """An American nurse living and working in Tokyo is exposed to a mysterious supernatural curse one
                     that locks a person in a powerful rage before claiming their life and spreading to another victim.""",
                    "http://sim04.in.com/62/3a73ae37b52c3a4394e5009084d378c9_pt_xl.jpg",
                    "https://www.youtube.com/watch?v=YC3bzK_i9_s")

#making a list of movies to pass to fresh tomatoes
movies = [airbender, pitch_perfect, grudge]
#passing list of movies as a variable open_movies_page
fresh_tomatoes.open_movies_page(movies)


