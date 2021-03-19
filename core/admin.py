from django.contrib import admin
from django import forms

from . import models


class verseAdminForm(forms.ModelForm):

    class Meta:
        model = models.verse
        fields = "__all__"


class verseAdmin(admin.ModelAdmin):
    form = verseAdminForm
    list_display = [
        "verse_english",
        "last_updated",
        "created",
        "verse_image",
        "verse_date",
        "verse_french",
        "verse_kirundi",
        "verse_hashtag",
    ]
    readonly_fields = [
        "verse_english",
        "last_updated",
        "created",
        "verse_image",
        "verse_date",
        "verse_french",
        "verse_kirundi",
        "verse_hashtag",
    ]


class themeAdminForm(forms.ModelForm):

    class Meta:
        model = models.theme
        fields = "__all__"


class themeAdmin(admin.ModelAdmin):
    form = themeAdminForm
    list_display = [
        "theme",
        "theme_month",
        "created",
        "theme_hashtag",
        "last_updated",
    ]
    readonly_fields = [
        "theme",
        "theme_month",
        "created",
        "theme_hashtag",
        "last_updated",
    ]


class postAdminForm(forms.ModelForm):

    class Meta:
        model = models.post
        fields = "__all__"


class postAdmin(admin.ModelAdmin):
    form = postAdminForm
    list_display = [
        "post_date",
        "last_updated",
        "created",
        "post_type",
        "post_text",
    ]
    readonly_fields = [
        "post_date",
        "last_updated",
        "created",
        "post_type",
        "post_text",
    ]


admin.site.register(models.verse, verseAdmin)
admin.site.register(models.theme, themeAdmin)
admin.site.register(models.post, postAdmin)
