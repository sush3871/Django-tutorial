from django import forms
from .models import Admin

class AdminForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Admin.objects.all(), label='Admin Name')
    
