from .models import Memes, Tags
from django import forms

class MemesForm(forms.ModelForm):
        class Meta:
                model = Memes
                fields = "__all__"