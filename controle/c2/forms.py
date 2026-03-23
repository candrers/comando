from django import forms

class NAMEForm(forms.Form):
    
    INTERESSE = forms.CharField(required=True,)
    