from django import forms
from .models import Lion

class TwoBlogPost(forms.ModelForm):
    class Meta:
        model = Lion
        fields = ['title', 'body']