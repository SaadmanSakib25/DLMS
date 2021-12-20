from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def receive_data(request):
    received_values=request.body.decode('utf-8')
    print(received_values)
    return HttpResponse("Forward,500")