from django import forms
from . import models


class verseForm(forms.ModelForm):
    class Meta:
        model = models.verse
        fields = [
            "verse_english",
            "verse_image",
            "verse_date",
            "verse_french",
            "verse_kirundi",
            "verse_hashtag",
        ]


class themeForm(forms.ModelForm):
    class Meta:
        model = models.theme
        fields = [
            "theme",
            "theme_month",
            "theme_hashtag",
        ]


class postForm(forms.ModelForm):
    class Meta:
        model = models.post
        fields = [
            "post_date",
            "post_type",
            "post_text",
        ]
