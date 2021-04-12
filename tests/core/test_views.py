import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_theme_list_view():
    instance1 = test_helpers.create_core_theme()
    instance2 = test_helpers.create_core_theme()
    client = Client()
    url = reverse("core_theme_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_theme_create_view():
    client = Client()
    url = reverse("core_theme_create")
    data = {
        "theme_from_date": datetime.now(),
        "theme_hashtag": "text",
        "theme_to_date": datetime.now(),
        "theme": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_theme_detail_view():
    client = Client()
    instance = test_helpers.create_core_theme()
    url = reverse("core_theme_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_theme_update_view():
    client = Client()
    instance = test_helpers.create_core_theme()
    url = reverse("core_theme_update", args=[instance.pk, ])
    data = {
        "theme_from_date": datetime.now(),
        "theme_hashtag": "text",
        "theme_to_date": datetime.now(),
        "theme": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_post_list_view():
    instance1 = test_helpers.create_core_post()
    instance2 = test_helpers.create_core_post()
    client = Client()
    url = reverse("core_post_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_post_create_view():
    client = Client()
    url = reverse("core_post_create")
    data = {
        "datetime": datetime.now(),
        "english": "text",
        "hashtag": "text",
        "post_type": "text",
        "post_text": "text",
        "french": "text",
        "kirundi": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_post_detail_view():
    client = Client()
    instance = test_helpers.create_core_post()
    url = reverse("core_post_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_post_update_view():
    client = Client()
    instance = test_helpers.create_core_post()
    url = reverse("core_post_update", args=[instance.pk, ])
    data = {
        "datetime": datetime.now(),
        "english": "text",
        "hashtag": "text",
        "post_type": "text",
        "post_text": "text",
        "french": "text",
        "kirundi": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_post_image_list_view():
    instance1 = test_helpers.create_core_post_image()
    instance2 = test_helpers.create_core_post_image()
    client = Client()
    url = reverse("core_post_image_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_post_image_create_view():
    post = test_helpers.create_core_post()
    client = Client()
    url = reverse("core_post_image_create")
    data = {
        "post_image": "anImage",
        "post": post.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_post_image_detail_view():
    client = Client()
    instance = test_helpers.create_core_post_image()
    url = reverse("core_post_image_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_post_image_update_view():
    post = test_helpers.create_core_post()
    client = Client()
    instance = test_helpers.create_core_post_image()
    url = reverse("core_post_image_update", args=[instance.pk, ])
    data = {
        "post_image": "anImage",
        "post": post.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
