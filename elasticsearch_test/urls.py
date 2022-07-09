from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from mainapp import views

router = routers.SimpleRouter()
router.register('search',
                views.MovieSearchViewSet,
                basename='search-movie')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('es/', views.MovieSearchWithESAPIView.as_view(), name='es-search-movie'),
    path('', include_docs_urls(title='Documentation'))
]

app_name = 'movie'