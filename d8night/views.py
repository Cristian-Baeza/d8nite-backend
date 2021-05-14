# Tyler Abbott 4/29/2021
# Currently using default User viewmodels, will require editing when user preferences info are added to the model

from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, ActivitySerializer, DateSerializer, ProfileSerializer
from .models import Activity, Date, Profile
import requests

# Hush-hush API stuff
yelp_api_key = 'Bearer UOioGfcH4D4494f9CTiJVzIphw_FUUcTKRph-4MGiM5SFyCC30NTHiQ5wraDc9zcLWjwrU2uCfe-RnITG-xPrgRecaFwyORP8XCxCgMyNdgvpxnWx-oBZbEVTm6MYHYx'
openweather_api_key = 'e54e1cddb271267c48a0a71a0d126ce7'

# User authentication stuff
@api_view(['GET'])
def current_user(request):
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Activities
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# Dates
class DateViewSet(viewsets.ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer

# Profile
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# BreweryDB API Handler
def breweries_list(request, zip):
    response = requests.get(f'https://api.openbrewerydb.org/breweries?by_postal={zip}').json()
    return JsonResponse(response, safe=False)

# Finds yelp businesses by zip
def yelp_api_zip(request, zip):
    headers = {"Authorization": yelp_api_key}
    response = requests.get(f'https://api.yelp.com/v3/businesses/search?location={zip}', headers=headers).json()
    return JsonResponse(response, safe=False)

# Finds Google Maps by zip
def google_maps_api_zip(request, zip):
    response = requests.get(f'https://www.google.com/maps/embed/v1/place?key=AIzaSyB97bf2HbQfZY0XuX-6XIKjI9Ho-Xjg18U&q={zip}&zoom=18&maptype=satellite')
    return HttpResponse(response)

# Finds Google Places by zip and keyword
def google_places_api_zip_keyword(request, zip, keyword):
    response = requests.get(f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={keyword}+in+{zip}&key=AIzaSyD8bqz9WPIUpFxIEM3eG6O6u1om8jv7e0o').json()
    return JsonResponse(response, safe=False)

# Finds weather for area by zip code
def weather_api_zip(request, zip):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid={openweather_api_key}&units=imperial').json()
    return JsonResponse(response, safe=False)