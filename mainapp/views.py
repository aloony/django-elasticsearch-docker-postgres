from functools import reduce
import operator

from django.db.models import Q
from rest_framework import viewsets, mixins

from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from mainapp.models import Movie
from mainapp.serializers import MovieSerializer, MovieDocumentSerializer
from mainapp.documents import MovieDocument

class MovieSearchViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        text = self.request.query_params.get('query', None)
        if not text:
            return self.queryset
        
        text_seq = text.split(' ')
        text_qs = reduce(operator.and_, 
        (Q(title__icontains=x) for x in text_seq))

        return self.queryset.filter(text_qs)

    
class MovieSearchWithESViewSet(DocumentViewSet):

    document = MovieDocument
    serializer_class = MovieDocumentSerializer

    filter_backends = [SearchFilterBackend]
    search_fields = [
        'title',
        'description'
    ]
    filter_fields = {
        'title': 'title'
    }





