# Importing fresh_tomatoes and media files
import fresh_tomatoes
import media

# Instances of movies with values (title, storyline, etc.)
elf = media.Movie("Elf", "The story of an elf who goes to New York City to find his dad.", "http://upload.wikimedia.org/wikipedia/en/d/df/Elf_movie.jpg", "https://www.youtube.com/watch?v=gW9wRNqQ_P8", "November 7, 2003")
captain_phillips = media.Movie("Captain Phillips", "The story of a merchant mariner, Captain Richard Phillips, who was taken hostage by pirates in the Indian Ocean led by Abduwali Muse.", "http://upload.wikimedia.org/wikipedia/en/a/a8/Captain_Phillips_Poster.jpg", "https://www.youtube.com/watch?v=_3ASoBrFGlc", "October 11, 2013")
the_blind_side = media.Movie("The Blind Side", "The story a homeless boy who became an All American football player with the help of a caring woman and her family.", "http://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg", "https://www.youtube.com/watch?v=dJ3kwMq18-8", "November 20, 2009")

# Defining an array (movies) with elf, captain_phillips, etc.
movies = [elf, captain_phillips, the_blind_side]
# Giving list as input to the open_movies_page function
fresh_tomatoes.open_movies_page(movies)
