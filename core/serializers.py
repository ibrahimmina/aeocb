from rest_framework import serializers

from . import models


class themeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.theme
        fields = [
            "last_updated",
            "theme_from_date",
            "theme_hashtag",
            "created",
            "theme_to_date",
            "theme",
        ]

class postSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.post
        fields = [
            "datetime",
            "english",
            "hashtag",
            "post_type",
            "post_text",
            "french",
            "last_updated",
            "kirundi",
            "created",
        ]

class post_imageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.post_image
        fields = [
            "last_updated",
            "post_image",
            "created",
        ]
