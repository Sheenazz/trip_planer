from django.urls import path, include
from rest_framework import routers
from . import views
from .views import SignUpView


router = routers.DefaultRouter()
router.register(r'areas', views.AreaViewSet)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('attractions', views.attraction_list, name='attraction_list'),
    path('trip/<int:pk>/', views.trip_detail, name='trip_detail'),
    path('trip/<int:pk>/edit/', views.trip_edit, name='trip_edit'),
    path('trip/new/', views.trip_new, name='trip_new'),
    path('trip/list', views.trips_list, name='trips_list'),
    path('trip/attractions', views.trip_attractions, name='trip_attractions'),
    path('trip/attraction_detail/<int:pk>/', views.attraction_detail, name='attraction_detail'),
    path('trip/attraction_edit/<int:pk>/', views.attraction_edit, name='attraction_edit'),
    path('trip/restaurants', views.trip_restaurants, name='trip_restaurants'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', views.home, name='home'),
    path('map', views.map, name='map')
]
