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
        "verse_hashtag": "text",
        "verse_french": "text",
        "verse_kirundi": "text",
        "verse_english": "text",
        "verse_image": "anImage",
        "date": datetime.now(),
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
        "verse_hashtag": "text",
        "verse_french": "text",
        "verse_kirundi": "text",
        "verse_english": "text",
        "verse_image": "anImage",
        "date": datetime.now(),
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
        "month": 1,
        "theme_hashtag": "text",
        "theme": "text",
        "year": 1,
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
        "month": 1,
        "theme_hashtag": "text",
        "theme": "text",
        "year": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302
