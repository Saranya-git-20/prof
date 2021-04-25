from django import forms 
from .models import *
  
class productForm(forms.ModelForm): 
  
    class Meta: 
        model = Product 
        fields = ['name', 'mainimage','slug','category','preview_text','detail_text','price']