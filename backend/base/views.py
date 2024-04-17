from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def handleRequest(request):
    print('hello from world', request)
    print('down', request.data.get('UserId'))

    print('data', list(request.data.items()))
    print('post', list(request.POST.items()))

    return Response({"result": "request received"})
