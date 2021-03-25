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
        "created",
        "last_updated",
        "theme",
        "theme_month",
        "theme_hashtag",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "theme",
        "theme_month",
        "theme_hashtag",
    ]


class verseAdminForm(forms.ModelForm):

    class Meta:
        model = models.verse
        fields = "__all__"


class verseAdmin(admin.ModelAdmin):
    form = verseAdminForm
    list_display = [
        "verse_hashtag",
        "created",
        "verse_date",
        "verse_kirundi",
        "verse_english",
        "verse_image",
        "last_updated",
        "verse_french",
    ]
    readonly_fields = [
        "verse_hashtag",
        "created",
        "verse_date",
        "verse_kirundi",
        "verse_english",
        "verse_image",
        "last_updated",
        "verse_french",
    ]


class postAdminForm(forms.ModelForm):

    class Meta:
        model = models.post
        fields = "__all__"


class postAdmin(admin.ModelAdmin):
    form = postAdminForm
    list_display = [
        "post_date",
        "post_image",
        "created",
        "post_text",
        "post_type",
        "last_updated",
    ]
    readonly_fields = [
        "post_date",
        "post_image",
        "created",
        "post_text",
        "post_type",
        "last_updated",
    ]


class qouteAdminForm(forms.ModelForm):

    class Meta:
        model = models.qoute
        fields = "__all__"


class qouteAdmin(admin.ModelAdmin):
    form = qouteAdminForm
    list_display = [
        "created",
        "qoute_date",
        "last_updated",
        "qoute_image",
        "qoute_hashtag",
    ]
    readonly_fields = [
        "created",
        "qoute_date",
        "last_updated",
        "qoute_image",
        "qoute_hashtag",
    ]


admin.site.register(models.theme, themeAdmin)
admin.site.register(models.verse, verseAdmin)
admin.site.register(models.post, postAdmin)
admin.site.register(models.qoute, qouteAdmin)
