from django import forms
from .models import Novels


class BookForm(forms.ModelForm):

    class Meta:
        model = Novels
        fields = '__all__'