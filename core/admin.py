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
        "last_updated",
        "verse_hashtag",
        "verse_french",
        "created",
        "verse_kirundi",
        "verse_english",
        "verse_image",
        "date",
    ]
    readonly_fields = [
        "last_updated",
        "verse_hashtag",
        "verse_french",
        "created",
        "verse_kirundi",
        "verse_english",
        "verse_image",
        "date",
    ]


class themeAdminForm(forms.ModelForm):

    class Meta:
        model = models.theme
        fields = "__all__"


class themeAdmin(admin.ModelAdmin):
    form = themeAdminForm
    list_display = [
        "created",
        "month",
        "theme_hashtag",
        "theme",
        "year",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "month",
        "theme_hashtag",
        "theme",
        "year",
        "last_updated",
    ]


admin.site.register(models.verse, verseAdmin)
admin.site.register(models.theme, themeAdmin)
