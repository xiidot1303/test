from django.forms import ModelForm
from .models import *
from django import forms
from datetime import date
from django.utils.translation import gettext_lazy as _

class DateSelectorWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        
        days = [(day, day) for day in range(1, 32)]
        days.insert(0, ('.....', '....'))
        months = [('....', '....'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5,'5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')]

        years = [(year, year) for year in [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]
        years.insert(0, ('....', '...'))
        widgets = [
            
            forms.Select(attrs=attrs, choices=months),
            forms.Select(attrs=attrs, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.month, value.year]
        elif isinstance(value, str):
            if value[0] == '.':
                year, month = ['...', '...']    
            else:
                
                month, year = value.split('/')


            return [month, year]
        return [None, None]

    def value_from_datadict(self, data, files, name):

        #month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        month = data['date_card_0']
        year = data['date_card_1']
        return '{}/{}'.format(month, year)

class OldDateSelector(forms.MultiWidget):
    def __init__(self, attrs=None):
        
        days = [(day, day) for day in range(1, 32)]
        days.insert(0, ('.....', '....'))
        months = [('....', '....'), (1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5,'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')]

        years = [(year, year) for year in [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]]
        years.insert(0, ('....', '...'))
        widgets = [
            forms.Select(attrs={'class': 'form-control',}, choices=days),
            forms.Select(attrs={'class': 'form-control',}, choices=months),
            forms.Select(attrs={'class': 'form-control',}, choices=years),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if isinstance(value, date):
            return [value.day, value.month, value.year]
        elif isinstance(value, str):
            if value[0] == '-':
                year, month, day = ['...', '...', '...']    
            else:
                year, month, day = value.split('-')

            return [day, month, year]
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        day, month, year = super().value_from_datadict(data, files, name)
        # DateField expects a single string that it can parse into a date.
        return '{}-{}-{}'.format(year, month, day)    


class AccForm(ModelForm, forms.Form):
    note = forms.CharField(max_length=20, widget=forms.Select(choices=[('dewd', 'dew')]))
    class Meta:
        
        model = Account
        
 
        
        fields = {'pseudonym', 'month', 'year', 'status', 'day_payment', 'document', 'summa', 'card_number', 'comment'}
        required = {
            'day_payment': False
        }
        widgets = {
            
         
            'day_payment': OldDateSelector, 
             
            
            }
           
    field_order = ['pseudonym', 'month', 'year', 'status', 'day_payment', 'summa', 'card_number', 'document', 'note', 'comment']


class ProfForm(ModelForm):
    class Meta:
        model = Profile
        fields = {'login', 'parol', 'pseudonym','code', 'number','published', 'name', 'prefix', 'type_payment', 'valute_card', 'card_number', 'date_card', 'owner_card'}
        help_texts = {
            'parol': _('help'),
        }

        labels = {
            'parol': _('Writer'),
        }
        widgets = {
            
            'date_card': DateSelectorWidget,
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'parol': forms.TextInput(attrs={'class': 'form-control',}),
            'pseudonym': forms.TextInput(attrs={'class': 'form-control',}),
            'code': forms.TextInput(attrs={'class': 'form-control',}),
            'number': forms.TextInput(attrs={'class': 'form-control',}),
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'prefix': forms.TextInput(attrs={'class': 'form-control',}),
            'type_payment': forms.TextInput(attrs={'class': 'form-control',}),
            'valute_card': forms.TextInput(attrs={'class': 'form-control',}),
            'card_number': forms.TextInput(attrs={'class': 'form-control',}),
            'date_card': forms.TextInput(attrs={'class': 'form-control',}),
            'owner_card': forms.TextInput(attrs={'class': 'form-control',}),
            
            "published": OldDateSelector,   
            
            
        }
    field_order = ['login', 'parol','name', 'published', 'pseudonym','code', 'number', 'prefix', 'type_payment', 'valute_card', 'card_number', 'date_card', 'owner_card']
class SecurityForm(ModelForm):
    class Meta:
        model = security
        fields = {'parol'}
        widgets = {
            "parol": forms.PasswordInput(),
        }

class SendmessageForm(forms.Form):
    select = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

    field_order = ['select', 'message']


class Addadmin(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=30)
    email = forms.CharField(max_length=100)

class SendContract(ModelForm):
    class Meta:
        model = contract
        fields = {'file'}
    field_order = ['file']


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = {'composition', 'type', 'artist', 'isrc', 'producer', 'operator', 'autor_script', 'painter', 'copyright', 'release_date', 'territory', 'link'}
    field_order = ['composition', 'type', 'artist', 'isrc', 'producer', 'operator', 'autor_script', 'painter', 'copyright', 'release_date', 'territory', 'link']

class AudioForm(ModelForm):
    class Meta:

        model = Audio
        fields = {'composition', 'artist', 'autor_music', 'autor_text', 'album', 'isrc', 'genre', 'copyright', 'related_rights', 'upc', 'release_date', 'territory', 'link'}

    field_order = ['composition', 'artist', 'autor_music', 'autor_text', 'album', 'isrc', 'genre', 'copyright', 'related_rights', 'upc', 'release_date', 'territory', 'link']


