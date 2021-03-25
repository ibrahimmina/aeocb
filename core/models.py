from django.db import models
from django.urls import reverse


class theme(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    theme = models.TextField(max_length=255,blank=True)
    theme_month = models.DateField(blank=True)
    theme_hashtag = models.TextField(max_length=255,blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_theme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_theme_update", args=(self.pk,))


class verse(models.Model):

    # Fields
    verse_hashtag = models.TextField(max_length=255,blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    verse_date = models.DateField(blank=True)
    verse_kirundi = models.TextField(max_length=255,blank=True)
    verse_english = models.TextField(max_length=255,blank=True)
    verse_image = models.ImageField(upload_to="upload/verse_images/",blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    verse_french = models.TextField(max_length=255,blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_verse_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_verse_update", args=(self.pk,))


class post(models.Model):

    # Fields
    post_date = models.DateField(blank=True)
    post_image = models.ImageField(upload_to="upload/post_images/",blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    post_text = models.TextField(max_length=255,blank=True)
    post_type = models.CharField(max_length=30,blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_post_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_post_update", args=(self.pk,))


class qoute(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    qoute_date = models.DateField(blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    qoute_image = models.ImageField(upload_to="upload/qoute_images/",blank=True)
    qoute_hashtag = models.CharField(max_length=255,blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_qoute_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_qoute_update", args=(self.pk,))
