from django import forms
from .models import Post


class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['author']
