from django.urls import path
from . import views
from .views import thesis_search

urlpatterns = [
    path('', views.show_thesis),
    path('search/', thesis_search, name='thesis_search')
]
