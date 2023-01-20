from django import forms
from .models import * 

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['owner']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']