from django.db import models
from django.urls import reverse
from django.db.models import signals
from django.dispatch import receiver

class theme(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    theme_from_date = models.DateField(blank=True)
    theme_hashtag = models.TextField(max_length=255,blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    theme_to_date = models.DateField(blank=True)
    theme = models.TextField(max_length=255,blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_theme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_theme_update", args=(self.pk,))


class post(models.Model):

    # Fields
    datetime = models.DateTimeField(blank=True)
    english = models.TextField(max_length=255,blank=True)
    hashtag = models.TextField(max_length=255,blank=True)
    post_type = models.CharField(max_length=30,blank=True)
    post_text = models.TextField(max_length=255)
    french = models.TextField(max_length=255,blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    kirundi = models.TextField(max_length=255,blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_post_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_post_update", args=(self.pk,))

class post_image(models.Model):

    # Relationships
    post = models.ForeignKey("core.post", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    post_image = models.ImageField(upload_to="upload/post_pre_images/",blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_post_image_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_post_image_update", args=(self.pk,))

@receiver(signals.post_save, sender=post)
def on_create_or_updated_obj(sender,created, instance, **kwargs):
    if created: 
        p = post_image(post=instance)
        p.save()