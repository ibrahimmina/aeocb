from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("theme", api.themeViewSet)
router.register("verse", api.verseViewSet)
router.register("post", api.postViewSet)
router.register("qoute", api.qouteViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("core/theme/", views.themeListView.as_view(), name="core_theme_list"),
    path("core/theme/create/", views.themeCreateView.as_view(), name="core_theme_create"),
    path("core/theme/detail/<int:pk>/", views.themeDetailView.as_view(), name="core_theme_detail"),
    path("core/theme/update/<int:pk>/", views.themeUpdateView.as_view(), name="core_theme_update"),
    path("core/verse/", views.verseListView.as_view(), name="core_verse_list"),
    path("core/verse/create/", views.verseCreateView.as_view(), name="core_verse_create"),
    path("core/verse/detail/<int:pk>/", views.verseDetailView.as_view(), name="core_verse_detail"),
    path("core/verse/update/<int:pk>/", views.verseUpdateView.as_view(), name="core_verse_update"),
    path("core/post/", views.postListView.as_view(), name="core_post_list"),
    path("core/post/create/", views.postCreateView.as_view(), name="core_post_create"),
    path("core/post/detail/<int:pk>/", views.postDetailView.as_view(), name="core_post_detail"),
    path("core/post/update/<int:pk>/", views.postUpdateView.as_view(), name="core_post_update"),
    path("core/qoute/", views.qouteListView.as_view(), name="core_qoute_list"),
    path("core/qoute/create/", views.qouteCreateView.as_view(), name="core_qoute_create"),
    path("core/qoute/detail/<int:pk>/", views.qouteDetailView.as_view(), name="core_qoute_detail"),
    path("core/qoute/update/<int:pk>/", views.qouteUpdateView.as_view(), name="core_qoute_update"),
)
