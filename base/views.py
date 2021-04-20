from django.views import generic
from django.urls import reverse_lazy
from .models import Article


# in what order should these be displayed?
# in order of date published
class ArticleIndex(generic.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'base/articles/index.html'


class ArticleDetail(generic.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'base/articles/show.html'


# maybe this should redirect to article and then user has a button to publish
# which then publishes and redirects to articles
class ArticleCreate(generic.CreateView):
    model = Article
    fields = '__all__'
    template_name = 'base/articles/new.html'
    success_url = reverse_lazy('articles')


class ArticleUpdate(generic.UpdateView):
    model = Article
    fields = "__all__"
    template_name = 'base/articles/edit.html'
    success_url = reverse_lazy('articles')


class ArticleDelete(generic.DeleteView):
    model = Article
    context_object_name = 'article'
    template_name = 'base/articles/confirm-delete.html'
    success_url = reverse_lazy('articles')
