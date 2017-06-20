import fresh_tomatoes
import media
"""input to the movie object? making instances for Movie Class?"""
airbender = media.Movie("The last airbender",
                        "the twelve-year old (chronologically 112) incarnation of the current Avatar and the eponymous",
                        "http://static.tvtropes.org/pmwiki/pub/images/ATLA_3829.jpg",
                        "https://www.youtube.com/watch?v=Rz7EsOua-D4")

pitch_perfect = media.Movie("Picth Perfect","eca, a freshman at Barden University, is cajoled into joining The Bellas, her school's all-girls singing group. Injecting some much needed energy into their repertoire, The Bellas take on their male rivals in a campus competition.",
                            "http://static.tvtropes.org/pmwiki/pub/images/pitch_perfect_poster.jpg",
                            "https://www.youtube.com/watch?v=F03N-ApQdmw")

grudge = media.Movie("The Grudge",
"An American nurse living and working in Tokyo is exposed to a mysterious supernatural curse, one that locks a person in a powerful rage before claiming their life and spreading to another victim.",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxODg1Nzc3NF5BMl5BanBnXkFtZTcwMjM0MjEzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=YC3bzK_i9_s")


#print(airbender.storyline)

#airbender.show_trailer()
movies = [airbender, pitch_perfect, grudge]
fresh_tomatoes.open_movies_page(movies)


