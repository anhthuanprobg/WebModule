import mlab
from models.movie import Movie

mlab.connect()

found_movies = Movie.objects(title__icontains="love") # match # contains
print(len(found_movies))
print(found_movies[0].title)
# print(found_movie.title)
# print(found_movie.link)