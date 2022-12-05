from django.urls import path
from . import views

# This is where we define and store our url endpoints for each view. This url file is ONLY for the 'cars' app
urlpatterns = [
    path('', views.cars_list), # Connects an endpoint to a view function that displays all cars in database
    path('<int:pk>/', views.car_details),
]