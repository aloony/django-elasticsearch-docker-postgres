import operator
from functools import reduce

from django.db.models import Q

from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from elasticsearch_dsl import Q as Q_es

# from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from mainapp.models import Movie
from mainapp.serializers import MovieSerializer, MovieDocumentSerializer
from mainapp.documents import MovieDocument

class MovieSearchViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    class Filter(SearchFilter):
        search_param = 'search'
        search_title = 'Search' 
        search_description = 'Finds search string in db via "icontains" lookup'

    filter_backends = [Filter]

    def get_queryset(self):
        text = self.request.query_params.get('search', None)
        if not text:
            return self.queryset
        
        text_seq = text.split(' ')
        text_qs = reduce(operator.and_, 
        (Q(title__icontains=x) for x in text_seq))

        return self.queryset.filter(text_qs)


class MovieSearchWithESAPIView(APIView, LimitOffsetPagination):

    class Filter(SearchFilter):
        search_param = 'search'
        search_title = 'Search' 
        search_description = 'Finds search string in db via elasticsearch'

    filter_backends = [Filter]


    movie_serializer = MovieSerializer
    search_document = MovieDocument

    def get(self, request):
        try:
            q = Q_es(
                'multi_match',
                query=self.request.query_params.get('search') if not None else '',
                fields = [
                'title',
                'description',
                'director'
                ])
            search = self.search_document.search().query(q)
            response = search.execute()
            result = self.paginate_queryset(response, request, view=self)
            serializer = self.movie_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e: # bad, bad, bad. I know
            return Response(f'{e}', status=500)





