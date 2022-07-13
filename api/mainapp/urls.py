from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.MovieSearchWithESAPIView.as_view(), name='es-search-movie'),
]