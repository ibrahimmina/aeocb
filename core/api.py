from rest_framework import viewsets, permissions
from datetime import datetime

from . import serializers
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action


class themeViewSet(viewsets.ModelViewSet):
    """ViewSet for the theme class"""

    queryset = models.theme.objects.all()
    serializer_class = serializers.themeSerializer
    permission_classes = [permissions.IsAuthenticated]

class unAuthThemeViewSet(viewsets.ModelViewSet):
    """ViewSet for the theme class"""
    
    queryset = models.theme.objects.all()
    serializer_class = serializers.themeSerializer

    def get_queryset(self):
        date_time_obj_date = datetime.strptime(self.request.query_params.get('datetime'), '%Y-%m-%dT%H:%M')
        print (date_time_obj_date)
        queryset = models.theme.objects.filter(theme_from_date__lte=date_time_obj_date, theme_to_date__gte=date_time_obj_date)
        serializer_class = serializers.themeSerializer

        return queryset




class postViewSet(viewsets.ModelViewSet):
    """ViewSet for the post class"""

    queryset = models.post.objects.all()
    serializer_class = serializers.postSerializer
    permission_classes = [permissions.IsAuthenticated]


class post_imageViewSet(viewsets.ModelViewSet):
    """ViewSet for the post_image class"""

    queryset = models.post_image.objects.all()
    serializer_class = serializers.post_imageSerializer
    permission_classes = [permissions.IsAuthenticated]
