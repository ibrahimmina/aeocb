from django.views import generic
from . import models
from . import forms
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image, ImageDraw, ImageFont,ImageFilter
import os
from django.conf import settings
from django.core.files.base import ContentFile
from io import BytesIO
from django.core.files import File
from django.urls import reverse


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


def post_imageUpdate(request, pk):
    print (pk)
    
    #load Image to background
    post_image=request.FILES['post_image']
    background = Image.open(post_image)
    background_width, background_height = background.size
    
    #load logo to logo
    logo = Image.open(settings.MEDIA_ROOT + '/static/logo-aeocb.png')
    logo_width, logo_height = logo.size

    #print sizes
    print (request._post)
    print ("logo size: " + str(logo.size))
    print ("Image size: " + str(background.size))

    #get ratios
    logo_width_ratio = int(request._post['current_logo_width']) / logo_width
    logo_height_ratio = int(request._post['current_logo_height']) / logo_height
    image_width_ratio = int(request._post['current_image_width']) / background_width
    image_height_ratio =int(request._post['current_image_height']) / background_height

    #resize logo
    new_logo_width = int(logo_width  * logo_width_ratio)
    new_logo_height = int(logo_height  * logo_height_ratio)
    new_logo_size = (new_logo_width,new_logo_height)
    logo = logo.resize(new_logo_size)
    
    #Add Logo to Background
    logo_left = int(int(request._post['logo_move_horizontal_input']) * (1/image_width_ratio))
    
    if ((logo_left + new_logo_width) > background_width):
        logo_left = background_width - new_logo_width

    logo_top = int(int(request._post['logo_move_vertical_input']) * (1/image_height_ratio))
    
    if ((logo_top + new_logo_height) > background_height):
        logo_top = background_height - new_logo_height

    
    background.paste(logo,(logo_left,logo_top),logo)

    #Add Text to Background
    font = ImageFont.truetype(settings.MEDIA_ROOT + "/font/WorkSans-VariableFont_wght.ttf", int(request._post['text_size_input']), encoding="unic")
    if (request._post['text_font_input'] == "Work Sans"):
        font = ImageFont.truetype(settings.MEDIA_ROOT + "/font/WorkSans-VariableFont_wght.ttf", int(request._post['text_size_input']), encoding="unic")
    elif (request._post['text_font_input'] == "Space Grotesk"):
        font = ImageFont.truetype(settings.MEDIA_ROOT + "/font/SpaceGrotesk-VariableFont_wght.ttf", int(request._post['text_size_input']), encoding="unic")
    elif (request._post['text_font_input'] == "Fira Sans"):
        font = ImageFont.truetype(settings.MEDIA_ROOT + "/font/FiraSans-Regular.ttf", int(request._post['text_size_input']), encoding="unic")
    message = request._post['post_text_final']
    draw = ImageDraw.Draw(background)
    (x, y) = (int(int(request._post['text_move_horizontal_input']) * int(1/image_width_ratio)),int(int(request._post['text_move_vertical_input'])* int(1/image_height_ratio)))
    color = request._post['text_color_input']
    draw.text((x, y), message, fill=color, font=font)

    #Save Background
    #thumb_io = BytesIO()
    #background.save(settings.MEDIA_ROOT + "/upload/post_images/test.png" , quality=95)
    blob = BytesIO()
    background.save(blob, format='JPEG', quality=100)
    post_image_object = models.post_image.objects.get(id=pk)
    if post_image_object.post_image and hasattr(post_image_object.post_image, 'url'):
        post_image_object.post_image.delete() 
        post_image_object.save()
    post_image_object.post_image.save(str(pk) + '.jpg', File(blob), save=False)
    post_image_object.save()

    return HttpResponseRedirect(reverse("core_post_image_detail", args=(pk,)))