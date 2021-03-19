from rest_framework import serializers

from . import models


class verseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.verse
        fields = [
            "verse_english",
            "last_updated",
            "created",
            "verse_image",
            "verse_date",
            "verse_french",
            "verse_kirundi",
            "verse_hashtag",
        ]

class themeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.theme
        fields = [
            "theme",
            "theme_month",
            "created",
            "theme_hashtag",
            "last_updated",
        ]

class postSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.post
        fields = [
            "post_date",
            "last_updated",
            "created",
            "post_type",
            "post_text",
        ]
