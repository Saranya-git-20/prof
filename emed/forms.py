from django import forms
#from emed.models import UserProfileInfo,Category,Product
from django.contrib.auth.models import User
from django.core import validators
import re

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    def clean(self): 
        	super(UserForm, self).clean() 
        	password = self.cleaned_data.get('password')
        	if ((len(password) < 5) and (len(password) <14)):
        		self._errors['password'] = self.error_class(['Post Should Contain a minimum of 10 characters'])
        	elif re.search('[0-9]',password) is None:
        		self._errors['password'] = self.error_class(['Make sure your password has a number in it'])
        	elif re.search('[A-Z]',password) is None:
        		self._errors['password'] = self.error_class(['The alphabets must be between [A-Z]'])

        		
        	return self.cleaned_data 

    

    class Meta():
        model = User
        fields = ('username','password','email')
        

  
         

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')
