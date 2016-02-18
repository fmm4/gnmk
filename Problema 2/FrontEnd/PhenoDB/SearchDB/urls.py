from django.conf.urls import url

from . import views

app_name = 'SearchDB'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(ur'^(?P<search_pheno>.*)$',views.results,name='results'),
]