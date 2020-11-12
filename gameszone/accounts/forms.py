from . import models
from django import forms
from django.contrib.auth.hashers import make_password

class UserForm(forms.ModelForm):
    password2=forms.CharField(widget=forms.PasswordInput(),initial="Password")
    class Meta:
        model=models.User
        fields=('username','password','email','image','description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'field'
        self.fields['password'].widget.attrs['class'] = 'field'
        self.fields['email'].widget.attrs['class'] = 'field'
        self.fields['password2'].widget.attrs['class'] = 'field'
        self.fields['description'].widget.attrs['class'] = 'black'



    def clean(self):
        data=super().clean()
        if passwordsError(data):
            raise forms.ValidationError('Passwords do not match')
        else:
            data['password']=make_password(data['password'])


class EditProfileForm(forms.ModelForm):
    password2=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=models.User
        fields=('username','email','image','description')

    def clean(self):
        data=super().clean()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'field'
        self.fields['email'].widget.attrs['class'] = 'field'
        self.fields['password2'].widget.attrs['class'] = 'field'
        self.fields['description'].widget.attrs['class'] = 'black'
        
class EditPassForm(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput(),initial="Password")
    password1=forms.CharField()
    password2=forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'field'
        self.fields['password1'].widget.attrs['class'] = 'field'
        self.fields['password2'].widget.attrs['class'] = 'field'

   
    
class EditLevelForm(forms.ModelForm):
    class Meta:
        model=models.User
        fields=('authorization_level',)

def passwordsError(data):
        pass1=data['password']
        pass2=data['password2']
        if pass1!=pass2:
            return True
        else:
            return False