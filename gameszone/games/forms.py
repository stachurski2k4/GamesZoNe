from . import models
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=('message',)

class VersionForm(forms.ModelForm):
    class Meta:
        model=models.Version
        fields=('download','version_str')

class GameForm(forms.ModelForm):
    class Meta:
        model=models.Game
        fields=('title','image','status','description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'field'
        self.fields['status'].widget.attrs['class'] = 'field'

class ImageForm(forms.ModelForm):
    class Meta:
        model=models.ScreenShot
        fields=('image',)