from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', views.MovieRetieveUpdateDestroyView.as_view(), name='movie-detail-list'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movie-statis-view'),
]
