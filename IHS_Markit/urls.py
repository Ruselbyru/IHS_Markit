from django.urls import path
from .views import TopAuthorsView


urlpatterns = [
    path('top10/', TopAuthorsView.as_view()),
]