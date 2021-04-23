from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article
from .forms import UserSignUpForm


class SignUpView(generic.edit.CreateView):
    template_name = 'base/users/new.html'
    success_url = reverse_lazy('articles')
    form_class = UserSignUpForm

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('articles')
        return super(SignUpView, self).get(*args, **kwargs)

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class CustomLoginView(LoginView):
    template_name = "base/sessions/new.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("articles")


class CustomLogoutView(LogoutView):
    next_page = "articles"


class ArticleIndex(generic.ListView):
    model = Article
    context_object_name = "articles"
    template_name = "base/articles/index.html"


class ArticleDetail(LoginRequiredMixin, generic.DetailView):
    model = Article
    context_object_name = "article"
    template_name = "base/articles/show.html"


# maybe this should redirect to article and then user has a button to publish
class ArticleCreate(LoginRequiredMixin, generic.CreateView):
    model = Article
    fields = ["title", "body", "published"]
    template_name = "base/articles/new.html"
    success_url = reverse_lazy("articles")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreate, self).form_valid(form)


class ArticleUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Article
    fields = ["title", "body", "published"]
    template_name = "base/articles/edit.html"
    success_url = reverse_lazy("articles")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(ArticleUpdate, self).dispatch(request, *args, **kwargs)


class ArticleDelete(LoginRequiredMixin, generic.DeleteView):
    model = Article
    context_object_name = "article"
    template_name = "base/articles/confirm-delete.html"
    success_url = reverse_lazy("articles")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404("You are not allowed to delete this Post")
        return super(ArticleDelete, self).dispatch(request, *args, **kwargs)
