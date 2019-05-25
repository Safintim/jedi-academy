from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('candidate_form', views.candidate_form, name='candidate_form'),
    path('jedai_form', views.jedi_form, name='jedai_form'),
    path('test_form', views.test_form, name='test_form'),
    path('candidates', views.candidates, name='candidates'),
]
