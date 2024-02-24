from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_thesis),
    path('search/', views.thesis_search, name='thesis_search'),
]
