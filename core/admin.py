from django.contrib import admin
from django import forms

from . import models


class themeAdminForm(forms.ModelForm):

    class Meta:
        model = models.theme
        fields = "__all__"


class themeAdmin(admin.ModelAdmin):
    form = themeAdminForm
    list_display = [
        "last_updated",
        "theme_from_date",
        "theme_hashtag",
        "created",
        "theme_to_date",
        "theme",
    ]
    readonly_fields = [
        "last_updated",
        "theme_from_date",
        "theme_hashtag",
        "created",
        "theme_to_date",
        "theme",
    ]


class postAdminForm(forms.ModelForm):

    class Meta:
        model = models.post
        fields = "__all__"


class postAdmin(admin.ModelAdmin):
    form = postAdminForm
    list_display = [
        "datetime",
        "english",
        "hashtag",
        "post_type",
        "post_text",
        "french",
        "last_updated",
        "kirundi",
        "created",
    ]
    readonly_fields = [
        "datetime",
        "english",
        "hashtag",
        "post_type",
        "post_text",
        "french",
        "last_updated",
        "kirundi",
        "created",
    ]


class post_imageAdminForm(forms.ModelForm):

    class Meta:
        model = models.post_image
        fields = "__all__"


class post_imageAdmin(admin.ModelAdmin):
    form = post_imageAdminForm
    list_display = [
        "last_updated",
        "post_image",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "post_image",
        "created",
    ]


admin.site.register(models.theme, themeAdmin)
admin.site.register(models.post, postAdmin)
admin.site.register(models.post_image, post_imageAdmin)
