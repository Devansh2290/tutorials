from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    print (request.user)
    return JsonResponse({"message": "Hello world!"})
