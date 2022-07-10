import operator
from functools import reduce

from django.db.models import Q

from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from elasticsearch_dsl import Q as Q_es

from mainapp.documents import MovieDocument
from mainapp.serializers import MovieDocumentSerializer, MovieSerializer

class MovieSearchWithESAPIView(APIView, LimitOffsetPagination):

    class Filter(SearchFilter):
        search_param = 'search'
        search_title = 'Search' 
        search_description = 'Finds search string in db via elasticsearch'

    filter_backends = [Filter]

    pagination_class = LimitOffsetPagination
    movie_serializer = MovieSerializer
    search_document = MovieDocument

    def get(self, request):
        try:
            q = Q_es(
                'multi_match',
                query=self.request.query_params.get('search') if self.request.query_params.get('search') is not None else '',
                fields = [
                'title',
                'description',
                'director'
                ])
            search = self.search_document.search().query(q)
            es_result = search.execute()

            result = self.paginate_queryset(es_result, request, view=self)
            serializer = self.movie_serializer(result, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e: # bad, bad, bad. I know
            return Response(repr(e), status=500)





