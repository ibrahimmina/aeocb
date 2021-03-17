from django.db import models
from django.urls import reverse


class verse(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    verse_hashtag = models.TextField(max_length=100)
    verse_french = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    verse_kirundi = models.TextField(max_length=100)
    verse_english = models.TextField(max_length=100)
    verse_image = models.ImageField(upload_to="upload/verse_images/")
    date = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_verse_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_verse_update", args=(self.pk,))


class theme(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    month = models.IntegerField()
    theme_hashtag = models.TextField(max_length=100)
    theme = models.TextField(max_length=100)
    year = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_theme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_theme_update", args=(self.pk,))
