from dataclasses import fields
from django import forms
from .models import Data

class DataForm(forms.ModelForm):
	class Meta:
		model = Data
		fields = ['nom', 'sepal_length', 'sepal_width', 'petal_length', 'petal_width']