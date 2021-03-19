import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_verse_list_view():
    instance1 = test_helpers.create_core_verse()
    instance2 = test_helpers.create_core_verse()
    client = Client()
    url = reverse("core_verse_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_verse_create_view():
    client = Client()
    url = reverse("core_verse_create")
    data = {
        "verse_english": "text",
        "verse_image": "anImage",
        "verse_date": datetime.now(),
        "verse_french": "text",
        "verse_kirundi": "text",
        "verse_hashtag": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_verse_detail_view():
    client = Client()
    instance = test_helpers.create_core_verse()
    url = reverse("core_verse_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_verse_update_view():
    client = Client()
    instance = test_helpers.create_core_verse()
    url = reverse("core_verse_update", args=[instance.pk, ])
    data = {
        "verse_english": "text",
        "verse_image": "anImage",
        "verse_date": datetime.now(),
        "verse_french": "text",
        "verse_kirundi": "text",
        "verse_hashtag": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


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
        "theme": "text",
        "theme_month": datetime.now(),
        "theme_hashtag": "text",
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
        "theme": "text",
        "theme_month": datetime.now(),
        "theme_hashtag": "text",
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
        "post_date": datetime.now(),
        "post_type": "text",
        "post_text": "text",
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
        "post_date": datetime.now(),
        "post_type": "text",
        "post_text": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
