from django import forms
from . import models


class themeForm(forms.ModelForm):
    class Meta:
        model = models.theme
        fields = [
            "theme_from_date",
            "theme_hashtag",
            "theme_to_date",
            "theme",
        ]


class postForm(forms.ModelForm):
    class Meta:
        model = models.post
        fields = [
            "datetime",
            "english",
            "hashtag",
            "post_type",
            "post_text",
            "french",
            "kirundi",
        ]


class post_imageForm(forms.ModelForm):
    class Meta:
        model = models.post_image
        fields = [
            "post_image",
            "post",
        ]
