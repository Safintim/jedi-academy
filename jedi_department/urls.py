from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('candidate_form', views.candidate_form, name='candidate_form'),
    path('jedi_form', views.jedi_form, name='jedi_form'),
    path('test_form', views.test_form, name='test_form'),
    path('candidates', views.candidates, name='candidates'),
]
