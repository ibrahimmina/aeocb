from django import forms
from . import models


class verseForm(forms.ModelForm):
    class Meta:
        model = models.verse
        fields = [
            "verse_hashtag",
            "verse_french",
            "verse_kirundi",
            "verse_english",
            "verse_image",
            "date",
        ]


class themeForm(forms.ModelForm):
    class Meta:
        model = models.theme
        fields = [
            "month",
            "theme_hashtag",
            "theme",
            "year",
        ]
