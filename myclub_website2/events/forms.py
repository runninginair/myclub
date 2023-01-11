from django import forms
from django.forms import ModelForm
from .models import Venue


# Create a venue form
class VenueForm(ModelForm):
	class Meta:
		model = Venue

		# fields = "__all__"
		fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')

		labels = {
			# 'name': "Enter Your Venue Here",
			'name': "",
			'address': "",
			'zip_code': "",
			'phone': "",
			'web': "",
			'email_address': "",
		}

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Venue Name'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Address'}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Zip Code'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Phone'}),
			'web': forms.TextInput(attrs={'class':'form-control', 'Placeholder':'Web Address'}),
			'email_address': forms.EmailInput(attrs={'class':'form-control', 'Placeholder':'Email'}),
		}