from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

@api_view(['GET', 'POST'])
def cars_list(request): # Backend code to correctly allow a user to view all cars in database, and post new cars to database

    if request.method == 'GET':
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def car_details(request, pk): # Allows user to correctly access and update a single car's details
    
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    """ #This is the normal way to do it without shortcuts#
    try:
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    """