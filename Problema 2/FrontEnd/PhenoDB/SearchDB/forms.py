from django import forms
from .models import PhenoDB

class SearchForm(forms.Form):
	search_pheno = forms.CharField(label='Informe a doenca de interesse na caixa abaixo:',
		max_length = 100)