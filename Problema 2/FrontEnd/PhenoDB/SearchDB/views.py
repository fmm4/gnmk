from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .forms import SearchForm
from .models import PhenoDB




def index(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect(reverse('SearchDB:results', args=(form.data.get('search_pheno'),)))
	else:
		form = SearchForm()
		template = loader.get_template('SearchDB/index.html')
	return render(request, 'SearchDB/index.html', {'form':form})

def results(request, search_pheno):
	searched_illness = search_pheno
	searched_result = PhenoDB.objects.filter(phenoilln__iexact=search_pheno)
	context = {
		'searched_result': searched_result,
		'searched_illness': searched_illness,
	}
	return render(request, 'SearchDB/results.html', context)