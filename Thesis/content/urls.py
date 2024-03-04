from django.urls import path
from . import views

app_name = "content"

urlpatterns = [
    path('', views.show_thesis, name='thesis_list'),
    path('search/', views.thesis_search, name='thesis_search'),
    path('<int:year>/<int:month>/<int:day>/<slug:thesis>/',views.thesis_details,name = "thesis_details")
]
