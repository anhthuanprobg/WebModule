from flask import Flask, render_template
import mlab
from models.movie import Movie

app = Flask(__name__)
mlab.connect()

@app.route("/")
def index():
  movie_list = Movie.objects()
  print(len(movie_list))
  for movie in movie_list:
    print(movie.image_url)
  return render_template("index.html", movies=movie_list)

if __name__ == "__main__":
  app.run(debug=True)