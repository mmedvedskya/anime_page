from django import forms
from django.forms import ModelForm
from .models import Personal_Info, Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['person']
        widgets = {
            'fav_film': forms.Textarea(attrs={
                'rows': 2,
                'cols': 40,
                'class': 'form-control',
            })
        }

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = Personal_Info
        fields = '__all__'