from campus.models import Restaurant, Item, BusinessHours
from django import forms

class SaveRestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name', 'location', 'phone_number', 'description')

        widgets = {
            'name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'location': forms.EmailInput(attrs = {
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'description': forms.TextInput(attrs = {
                'class': 'form-control'
            })
        }

    