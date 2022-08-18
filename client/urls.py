from django.urls import path, include
from .views import client, client_general


urlpatterns = [

    path('', client_general),
    path('<int:client_number>/', client),
]
