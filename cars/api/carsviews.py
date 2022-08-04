
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import CarsSerializer
from rest_framework.throttling import UserRateThrottle
from cars.models import Cars


class CarsAPIView(APIView):
    serializer_class = CarsSerializer
    throttle_scope = "cars_app"

    def get_queryset(self):
        cars = Cars.objects.all()
        return cars

 
        
        try:
            id = request.query_params["id"]
            if id != None:
                car = Cars.objects.get(id=id)
                serializer = CarsSerializer(car)
        except:
            cars = self.get_queryset()
            serializer = CarsSerializer(cars, many=True)

        return Response(serializer.data)

        car_data = request.data

        new_car = Cars.objects.create(car_brand=car_data["car_brand"], car_model=car_data[
            "car_model"], production_year=car_data["production_year"], car_body=car_data["car_body"], engine_type=car_data["engine_type"])

        new_car.save()

        serializer = CarsSerializer(new_car)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        car_object = Cars.objects.get(id=id)

        data = request.data

        car_object.car_brand = data["car_brand"]
        car_object.car_model = data["car_model"]
        car_object.production_year = data["production_year"]
        car_object.car_body = data["car_body"]
        car_object.engine_type = data["engine_type"]

        car_object.save()

        serializer = CarsSerializer(car_object)
        return Response(serializer.data)
