from rest_framework import serializers

from . import models


class verseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.verse
        fields = [
            "last_updated",
            "verse_hashtag",
            "verse_french",
            "created",
            "verse_kirundi",
            "verse_english",
            "verse_image",
            "date",
        ]

class themeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.theme
        fields = [
            "created",
            "month",
            "theme_hashtag",
            "theme",
            "year",
            "last_updated",
        ]
