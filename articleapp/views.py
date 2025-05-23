from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationFrom
from articleapp.models import Article
from commentapp.forms import CommentCreationForm


# Create your views here.
@method_decorator(login_required, name='get')
@method_decorator(login_required, name='post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationFrom
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        from django.urls import reverse
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})

class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

@method_decorator(article_ownership_required, name='get')
@method_decorator(article_ownership_required, name='post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationFrom
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        from django.urls import reverse
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})


@method_decorator(article_ownership_required, name='get')

class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 3