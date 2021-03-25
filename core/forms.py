from django import forms
from . import models


class themeForm(forms.ModelForm):
    class Meta:
        model = models.theme
        fields = [
            "theme",
            "theme_month",
            "theme_hashtag",
        ]


class verseForm(forms.ModelForm):
    class Meta:
        model = models.verse
        fields = [
            "verse_hashtag",
            "verse_date",
            "verse_kirundi",
            "verse_english",
            "verse_image",
            "verse_french",
        ]


class postForm(forms.ModelForm):
    class Meta:
        model = models.post
        fields = [
            "post_date",
            "post_image",
            "post_text",
            "post_type",
        ]


class qouteForm(forms.ModelForm):
    class Meta:
        model = models.qoute
        fields = [
            "qoute_date",
            "qoute_image",
            "qoute_hashtag",
        ]
