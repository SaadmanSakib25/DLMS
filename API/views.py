from django.http import JsonResponse, response
from ImageProcessor.engine import processor
def index(request):
    response = processor()
    return JsonResponse(response)