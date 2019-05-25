from django import forms

from .models import Candidate, Answer, Jedi


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['email', 'name', 'planet', 'age']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'planet': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'})
        }


class TestForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text_answer']

        widgets = {
            'text_answer': forms.TextInput(attrs={'class': 'form-control'}),
        }


class JediForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Jedi.objects.all(),
                                  empty_label="Select Jedi",
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Jedi
        fields = ['name']

