from django.views import generic
from . import models
from . import forms


class verseListView(generic.ListView):
    model = models.verse
    form_class = forms.verseForm


class verseCreateView(generic.CreateView):
    model = models.verse
    form_class = forms.verseForm


class verseDetailView(generic.DetailView):
    model = models.verse
    form_class = forms.verseForm


class verseUpdateView(generic.UpdateView):
    model = models.verse
    form_class = forms.verseForm
    pk_url_kwarg = "pk"


class themeListView(generic.ListView):
    model = models.theme
    form_class = forms.themeForm


class themeCreateView(generic.CreateView):
    model = models.theme
    form_class = forms.themeForm


class themeDetailView(generic.DetailView):
    model = models.theme
    form_class = forms.themeForm


class themeUpdateView(generic.UpdateView):
    model = models.theme
    form_class = forms.themeForm
    pk_url_kwarg = "pk"


class postListView(generic.ListView):
    model = models.post
    form_class = forms.postForm


class postCreateView(generic.CreateView):
    model = models.post
    form_class = forms.postForm


class postDetailView(generic.DetailView):
    model = models.post
    form_class = forms.postForm


class postUpdateView(generic.UpdateView):
    model = models.post
    form_class = forms.postForm
    pk_url_kwarg = "pk"
