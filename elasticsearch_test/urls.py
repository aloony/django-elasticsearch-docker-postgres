from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, urlpatterns
from mainapp import views

router = routers.DefaultRouter()
router.register('search',
                views.MovieSearchViewSet,
                basename='search-movie')
router.register('es',
                views.MovieSearchWithESViewSet,
                basename='search-movie')







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

app_name = 'movie'