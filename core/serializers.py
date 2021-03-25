from rest_framework import serializers

from . import models


class themeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.theme
        fields = [
            "created",
            "last_updated",
            "theme",
            "theme_month",
            "theme_hashtag",
        ]

class verseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.verse
        fields = [
            "verse_hashtag",
            "created",
            "verse_date",
            "verse_kirundi",
            "verse_english",
            "verse_image",
            "last_updated",
            "verse_french",
        ]

class postSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.post
        fields = [
            "post_date",
            "post_image",
            "created",
            "post_text",
            "post_type",
            "last_updated",
        ]

class qouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.qoute
        fields = [
            "created",
            "qoute_date",
            "last_updated",
            "qoute_image",
            "qoute_hashtag",
        ]
