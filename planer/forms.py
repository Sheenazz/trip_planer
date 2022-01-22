from django import forms

from .models import Area, Restaurant, Attraction, Search


class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')
    class Meta:
        model = Search
        fields = ('address',)


class DateInput(forms.DateInput):
    input_type = 'date'


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ('destination', 'map_link', 'date_of_arrival', 'date_of_departure', 'accommodation_link')
        widgets = {
            'date_of_arrival': DateInput(),
            'date_of_departure': DateInput(),
        }


class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = ('name_of_attraction', 'attraction_description', 'attraction_url', 'area')


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('map', 'kind_of_food', 'name_of_restaurant', 'opening_hours', 'area')
