from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationFrom(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'aditable text-left',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']

