from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

# Create your views here.
@api_view(['POST'])
def handleRequest(request):

    url = 'https://apikr.lookinbody.com/inbody/GetFullInBodyDataByID'

    headers = {
        'Content-Type': 'application/json',
        'API-KEY': 'OilU7HR9nOzy7XQOvOYj7uyaBZf/lzlAysy+OIDtEF8=',
        'Account': 'devcors07',
    }

    print('receiving data', request.data.get('UserId'), request.data.get('TestDatetimes'))

    data = {
        'UserID': request.data.get('UserId'),
        'Datetimes': request.data.get('TestDatetimes'),
    }

    response = requests.post(url, headers=headers, json=data)

    # Checking the response
    if response.status_code == 200:
        print("Request was successful!")
        print("Response body:", response.text)
        return Response({"result": "success"})
    else:
        print("Request failed with status code:", response.status_code)

    return Response({"result": "fail"})
