from rest_framework import serializers
from .models import Movie, Ratings, Comments


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'rated', 'released', 'runtime', 'genre', 'director', 'writer',
                  'actors', 'plot', 'language', 'country', 'awards', 'poster', 'metascore', 'imdb_rating', 'imdb_votes',
                  'imdb_id', 'type', 'dvd', 'box_office', 'production', 'website', 'response']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ['rating_id', 'source', 'value', 'movie_id']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment_id', 'comment', 'movie_id']
