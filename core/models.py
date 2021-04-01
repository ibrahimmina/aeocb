from django.db import models
from django.urls import reverse
from django.db.models import signals
from django.dispatch import receiver
from PIL import Image, ImageDraw, ImageFont
import datetime
from django.core.files.storage import FileSystemStorage

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

    @property
    def get_photo_url(self):
        if self.verse_image and hasattr(self.verse_image, 'url'):
            return self.verse_image.url
        else:
            return "/static/emptyimage.png"

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
    
    @property
    def get_photo_url(self):
        if self.post_image and hasattr(self.post_image, 'url'):
            return self.post_image.url
        else:
            return "/static/emptyimage.png"



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

    @property
    def get_photo_url(self):
        if self.qoute_image and hasattr(self.qoute_image, 'url'):
            return self.qoute_image.url
        else:
            return "/static/emptyimage.png"

@receiver(signals.post_save, sender=verse)
def on_create_or_updated_obj(sender,created, instance, **kwargs):
    if created:

        verse_theme = theme.objects.filter(theme_month__month=instance.verse_date.month)
        post_text =  instance.verse_french + "\n" + instance.verse_english + "\n" +  instance.verse_kirundi + "\n" + verse_theme[0].theme_hashtag + "\n" + instance.verse_hashtag + "\n"
        image = Image.open(instance.verse_image)
        image_file = 'upload/post_images/verse_' + str(instance.verse_date) + ".png"
        image.save('media/' + image_file)
        p = post(post_date=instance.verse_date,post_type="verse",post_text=post_text, post_image=image_file)
        p.save()
    else:
        verse_theme = theme.objects.filter(theme_month__month=instance.verse_date.month)
        post_text =  instance.verse_french + "\n" + instance.verse_english + "\n" +  instance.verse_kirundi + "\n" + verse_theme[0].theme_hashtag + "\n" + instance.verse_hashtag + "\n"

        post_verse = post.objects.filter(post_date=instance.verse_date,post_type="verse")
        post_verse.post_text = post_text
        post_verse.save()

        # create Image object with the input image

        #image = Image.open(instance.verse_image)

        # initialise the drawing context with
        # the image object as background

        #draw = ImageDraw.Draw(image)

        # create font object with the font file and specify
        # desired size

        #font = ImageFont.load_default()

        # starting position of the message

        #(x, y) = (150, 150)
        #name = post_text
        #color = 'rgb(255, 255, 255)' # white color
        #draw.text((x, y), name, fill=color, font=font)

        # save the edited image

        #image.save('post_folder/' + str(p.post_date) + ".jpg")
