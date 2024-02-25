from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_thesis, name='thesis_list'),
    path('search/', views.thesis_search, name='thesis_search'),
]
