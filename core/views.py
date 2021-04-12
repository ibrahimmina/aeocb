from django.views import generic
from . import models
from . import forms


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


class post_imageListView(generic.ListView):
    model = models.post_image
    form_class = forms.post_imageForm


class post_imageCreateView(generic.CreateView):
    model = models.post_image
    form_class = forms.post_imageForm


class post_imageDetailView(generic.DetailView):
    model = models.post_image
    form_class = forms.post_imageForm


class post_imageUpdateView(generic.UpdateView):
    model = models.post_image
    form_class = forms.post_imageForm
    pk_url_kwarg = "pk"
