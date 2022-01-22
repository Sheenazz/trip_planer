from django.db import models
from django.db.models import URLField
from django.utils import timezone
from django.db import models
# Create your models here.


class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Area(models.Model):
    destination = models.CharField(max_length=200, default='')
    map_link = models.URLField(max_length=250, default='') #link do mapy
    date_of_arrival = models.DateField() #do tego może być widget - kalendarz
    date_of_departure = models.DateField()
    accommodation_link = models.URLField(max_length=250, default='') #link do noclegu

    def __str__(self):
        return self.destination


class Restaurant(models.Model):
    map = models.URLField(max_length=250)
    kind_of_food = models.CharField(max_length=250, blank=True)
    name_of_restaurant = models.CharField(max_length=250, blank=True)
    opening_hours = models.CharField(max_length=250, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, default=1)
    #screen_shots = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.name_of_restaurant


class Attraction(models.Model):
    name_of_attraction = models.CharField(max_length=200, blank=True)
    attraction_description = models.TextField()  # co, godz. otwarcia, ceny biletów
    attraction_url = models.URLField(max_length=250, default='default value')  # link do strony atrakcji
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_attraction


class PackList(models.Model):
    text = models.TextField()


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title