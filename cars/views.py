from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car

@api_view(['GET'])
def cars_list(request):

    car = Car.objects.all()

    serializer = CarSerializer(car, many=True)

    return Response(serializer.data)