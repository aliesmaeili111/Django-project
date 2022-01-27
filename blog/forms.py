from dataclasses import field
import imp
from xml.etree.ElementTree import Comment
from django import forms
from  . models import Comment

class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ('name','email','comment')