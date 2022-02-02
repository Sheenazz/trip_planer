import folium
import geocoder
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets

from .forms import AreaForm, AttractionForm, RestaurantForm, SearchForm
from .models import Attraction, Area, Search
from .serializers import AreaSerializer

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

def post_list(request):
    return render(request, 'planer/index.html', {})


def home(request):
    return render(request, 'planer/home.html', {})


def map(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/map')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    if address == None:
        m = folium.Map(location=[19, -21], zoom_start=2)
        m = m._repr_html_()
        context = {
            'm': m,
            'form': form,
        }
        return render(request, 'planer/map.html', context)
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Your address input is invalid')
    # create map object
    m = folium.Map(location=[19, -21], zoom_start=2)
    folium.Marker([lat, lng], tooltip='Click for more',
                  popup=country).add_to(m)
    # get HTML representation of map object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'planer/map.html', context)


def attraction_list(request):
    attractions = Attraction.objects.all().order_by('name_of_attraction')
    return render(request, 'planer/attraction_list.html', {'attractions': attractions})


def trips_list(request):
    trips = Area.objects.all().order_by('destination')
    return render(request, 'planer/trips_list.html', {'trips': trips})


def trip_new(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            return redirect('trip_detail', pk=trip.pk)
    else:
        form = AreaForm()
    return render(request, 'planer/trip_edit.html', {'form': form})


def trip_edit(request, pk):
    tripedit = get_object_or_404(Area, pk=pk)
    if request.method == "POST":
        form = AreaForm(request.POST, instance=tripedit)
        if form.is_valid():
            tripedit = form.save(commit=False)
            tripedit.save()
            return redirect('trip_detail', pk=tripedit.pk)
    else:
        form = AreaForm(instance=tripedit)
    return render(request, 'planer/trip_edit.html', {'form': form})


def trip_detail(request, pk):
    myarea = get_object_or_404(Area, pk=pk)
    return render(request, 'planer/trip_detail.html', {'area': myarea})


def trip_attractions(request):
    if request.method == "POST":
        form = AttractionForm(request.POST)
        if form.is_valid():
            attraction = form.save(commit=False)
            attraction.save()
            return redirect('attraction_detail', pk=attraction.pk)
    else:
        form = AttractionForm()
    return render(request, 'planer/attraction_edit.html', {'form': form})


def trip_restaurants(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.save()
            return redirect('trip_restaurant', pk=restaurant.pk)
    else:
        form = RestaurantForm()
    return render(request, 'planer/restaurant_edit.html', {'form': form})


def attraction_detail(request, pk):
    myattraction = get_object_or_404(Attraction, pk=pk)
    return render(request, 'planer/attraction_detail.html', {'attraction': myattraction})


def attraction_edit(request, pk):
    attractionedit = get_object_or_404(Attraction, pk=pk)
    if request.method == "POST":
        form = AttractionForm(request.POST, instance=attractionedit)
        if form.is_valid():
            attractionedit = form.save(commit=False)
            attractionedit.save()
            return redirect('attraction_detail', pk=attractionedit.pk)
    else:
        form = AttractionForm(instance=attractionedit)
    return render(request, 'planer/attraction_edit.html', {'form': form})


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all().order_by('destination')
    serializer_class = AreaSerializer
    http_method_names = ['get']


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


