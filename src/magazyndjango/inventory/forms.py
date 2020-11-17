from django import forms
from .models import Inventory


class InventoryAddForm(forms.ModelForm):
	name			= forms.CharField(label='Nazwa ', widget= forms.TextInput())
	description		= forms.CharField(label='Opis ', widget= forms.Textarea(attrs={"rows": 10,
																					"cols": 50
																				}))
	quantity		= forms.DecimalField(label='Ilość ')
	unit			= forms.CharField(label='Jednostka Magazynowa ', widget= forms.TextInput())
	place			= forms.CharField(label='Sektor ', widget=forms.TextInput())

	class Meta:
		model = Inventory
		fields =[
			'name',
			'description',
			'quantity',
			'unit',
			'place'
		]
