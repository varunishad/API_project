
from django.urls import path
from . import views

urlpatterns = [
    path('api/upload-csv/', views.read_csv),
    path('api/fetch-data/', views.fetch_data),
]
