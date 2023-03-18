from .models import TASK
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=TASK
        fields=['name','priority','date']

