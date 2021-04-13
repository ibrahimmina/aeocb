from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("theme", api.themeViewSet)
router.register("themes", api.unAuthThemeViewSet, basename='theme')
router.register("post", api.postViewSet)
router.register("post_image", api.post_imageViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("core/theme/", views.themeListView.as_view(), name="core_theme_list"),
    path("core/theme/create/", views.themeCreateView.as_view(), name="core_theme_create"),
    path("core/theme/detail/<int:pk>/", views.themeDetailView.as_view(), name="core_theme_detail"),
    path("core/theme/update/<int:pk>/", views.themeUpdateView.as_view(), name="core_theme_update"),
    path("core/post/", views.postListView.as_view(), name="core_post_list"),
    path("core/post/create/", views.postCreateView.as_view(), name="core_post_create"),
    path("core/post/detail/<int:pk>/", views.postDetailView.as_view(), name="core_post_detail"),
    path("core/post/update/<int:pk>/", views.postUpdateView.as_view(), name="core_post_update"),
    path("core/post_image/", views.post_imageListView.as_view(), name="core_post_image_list"),
    path("core/post_image/create/", views.post_imageCreateView.as_view(), name="core_post_image_create"),
    path("core/post_image/detail/<int:pk>/", views.post_imageDetailView.as_view(), name="core_post_image_detail"),
    path("core/post_image/update/<int:pk>/", views.post_imageUpdateView.as_view(), name="core_post_image_update"),
    path("core/post_image/updateNew/<int:pk>/", views.post_imageUpdate, name="core_post_image_updateNew"),
)
