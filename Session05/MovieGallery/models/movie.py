from mongoengine import Document, StringField

class Movie(Document):
  title = StringField(max_length=200)
  image_url = StringField()
  link = StringField()