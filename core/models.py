from django.db import models
from django.urls import reverse
from django.db.models import signals
from django.dispatch import receiver
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive


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

    @property
    def get_photo_status(self):
        if self.post_image and hasattr(self.post_image, 'url'):
            return "Yes"
        else:
            return "No"

@receiver(signals.post_save, sender=post)
def on_create_or_updated_obj(sender,created, instance, **kwargs):
    if created: 
        p = post_image(post=instance)
        p.save()
        
"""         gauth = GoogleAuth()
        
        GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = "media/credentials/client_secrets.json"
        # Try to load saved client credentials
        gauth.LoadCredentialsFile("media/credentials/mycreds.txt")
        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved creds
            gauth.Authorize()
        # Save the current credentials to a file
        gauth.SaveCredentialsFile("media/credentials/mycreds.txt")

        drive = GoogleDrive(gauth)
        post_file_name = str(instance.datetime) + instance.post_type
        post_directory_name = str(instance.datetime)
        post_text = instance.post_text

        root_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

        for directory in root_list:  
            if (directory['title'] == "Posts"):
                directoryId = directory['id']
            
        directory = drive.CreateFile({'title': post_directory_name, 
            "parents": [{"kind": "drive#fileLink", "id": directoryId}], 
            "mimeType": "application/vnd.google-apps.folder"})    
        directory.Upload()
        print (directory['id'])

        post = drive.CreateFile({'title': post_file_name, 
            "parents": [{"kind": "drive#fileLink", "id": directory['id']}]})  # Create GoogleDriveFile instance with title 'Hello.txt'.
        post.SetContentString(post_text) # Set content of the file from given string.
        post.Upload() """