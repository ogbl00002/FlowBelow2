from django.shortcuts import render
from django.http import HttpResponse
from .models import Sensor, Sensor_time_value

def sensor_list_view(request):
    sensor_objects = Sensor.objects.all()
    context = {
        'sensor_objects': sensor_objects
    }
    return render(request, 'list_sensors.html', context)

def index(request):
    context = {
        'timeData': Sensor_time_value.objects.all().filter(id_tag='A81758FFFE045989')
    }
    return render(request, 'homepage.html',context)
