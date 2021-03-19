from rest_framework import viewsets, permissions

from . import serializers
from . import models


class verseViewSet(viewsets.ModelViewSet):
    """ViewSet for the verse class"""

    queryset = models.verse.objects.all()
    serializer_class = serializers.verseSerializer
    permission_classes = [permissions.IsAuthenticated]


class themeViewSet(viewsets.ModelViewSet):
    """ViewSet for the theme class"""

    queryset = models.theme.objects.all()
    serializer_class = serializers.themeSerializer
    permission_classes = [permissions.IsAuthenticated]


class postViewSet(viewsets.ModelViewSet):
    """ViewSet for the post class"""

    queryset = models.post.objects.all()
    serializer_class = serializers.postSerializer
    permission_classes = [permissions.IsAuthenticated]
