import operator
from functools import reduce

from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from elasticsearch_dsl import Q as Q_es
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

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
    serializer_class = MovieSerializer

    def get(self, request):
        try:
            if request.query_params.get('search') is None:
                return Response(status=204)

            search = self.search_document.search().query(Q_es(
                'multi_match',
                query=request.query_params.get('search'),
                fuzziness='auto',
                fields=[
                    'title',
                    'director',
                    'description'
                ]
            ))
            es_result = search.execute()

            result = self.paginate_queryset(es_result, request, view=self)
            serializer = self.movie_serializer(result, many=True)
            return Response(serializer.data, status=200)
        except Exception as e: # bad, bad, bad. I know
            return Response(repr(e), status=500)





