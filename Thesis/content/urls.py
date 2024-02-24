from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_thesis, name='thesis_list'),
    path('search/', views.thesis_search, name='thesis_search'),
    path('thesis/<int:thesis_id>/', views.show_thesis_detail, name='thesis_detail'),
]
