from django.db import models
from django.urls import reverse
from django.db.models import signals
from django.dispatch import receiver
from PIL import Image, ImageDraw, ImageFont
import datetime
from django.core.files.storage import FileSystemStorage


class verse(models.Model):

    # Fields
    verse_english = models.TextField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    verse_image = models.ImageField(upload_to="upload/verse_images/")
    verse_date = models.DateField()
    verse_french = models.TextField(max_length=255)
    verse_kirundi = models.TextField(max_length=255)
    verse_hashtag = models.TextField(max_length=255)

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
    theme = models.TextField(max_length=255)
    theme_month = models.DateField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    theme_hashtag = models.TextField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_theme_month(self):
        return str(self.theme_month.month)

    def get_absolute_url(self):
        return reverse("core_theme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_theme_update", args=(self.pk,))


class post(models.Model):

    # Fields
    post_date = models.DateField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    post_type = models.CharField(max_length=30)
    post_text = models.TextField(max_length=255)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("core_post_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("core_post_update", args=(self.pk,))

@receiver(signals.post_save, sender=verse)
def on_create_or_updated_obj(sender, instance, **kwargs):
   if kwargs['created']:

        verse_theme = theme.objects.filter(theme_month__month=instance.verse_date.month)
        post_text = verse_theme[0].theme_hashtag + "\n" + instance.verse_english + "\n" + instance.verse_french + "\n" + instance.verse_kirundi + "\n" + instance.verse_hashtag + "\n"
        
        p = post(post_date=instance.verse_date,post_type="verse",post_text=post_text)
        p.save()

        # create Image object with the input image
        
        image = Image.open(instance.verse_image)
        
        # initialise the drawing context with
        # the image object as background
        
        draw = ImageDraw.Draw(image)

        # create font object with the font file and specify
        # desired size
        
        font = ImageFont.load_default()
        
        # starting position of the message
        
        (x, y) = (150, 150)
        name = post_text
        color = 'rgb(255, 255, 255)' # white color
        draw.text((x, y), name, fill=color, font=font)
        
        # save the edited image
         
        image.save('post_folder/' + str(p.post_date) + ".jpg")



   else:
      print ("New Verse Updated")
      #logic for sending user updated email to user