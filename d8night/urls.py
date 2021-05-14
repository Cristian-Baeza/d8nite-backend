from django.urls import path
from .views import current_user, UserList, ActivityViewSet, DateViewSet, ProfileViewSet, breweries_list, yelp_api_zip, google_maps_api_zip, google_places_api_zip_keyword, weather_api_zip
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path("breweries/<int:zip>", breweries_list, name='breweries_list'),
    path("restaurants/<int:zip>", yelp_api_zip, name="yelp_api_zip"),
    path("maps/<int:zip>", google_maps_api_zip, name="google_maps_api_zip"),
    path("maps/<int:zip>/<str:keyword>", google_places_api_zip_keyword, name="google_places_api_zip_keyword"),
    path("weather/<int:zip>", weather_api_zip, name="weather_api_zip"),
]

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'dates', DateViewSet, basename='date')
router.register(r'profiles', ProfileViewSet, basename='profile')
urlpatterns = urlpatterns + router.urls