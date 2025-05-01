from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationFrom(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']
