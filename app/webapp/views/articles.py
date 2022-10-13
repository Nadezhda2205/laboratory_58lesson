from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ArticleForm
from webapp.models import Article


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})


class ArticleCreate(CreateView, SuccessDetailUrlMixin):
    template_name = 'article_create.html'
    form_class = ArticleForm
    model = Article


class ArticleView(DetailView):
    template_name = 'article.html'
    model = Article


class ArticleUpdateView(UpdateView):
    template_name = 'article_update.html'
    form_class = ArticleForm
    model = Article
    context_object_name = 'article'

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    template_name = 'article_confirm_delete.html'
    model = Article
    success_url = reverse_lazy('index')
