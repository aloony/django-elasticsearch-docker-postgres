from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet


from mainapp.models import Movie
from mainapp.documents import MovieDocument

class MovieSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = [
            'title',
            'description',
            'director'
        ]
    
class MovieDocumentSerializer(DocumentSerializer):

    class Meta:
        document = MovieDocument
        fields = [
            'title',
            'description',
            'director'
        ]







