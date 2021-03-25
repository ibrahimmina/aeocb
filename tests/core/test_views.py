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
        "verse_date": datetime.now(),
        "verse_kirundi": "text",
        "verse_english": "text",
        "verse_image": "anImage",
        "verse_french": "text",
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
        "verse_date": datetime.now(),
        "verse_kirundi": "text",
        "verse_english": "text",
        "verse_image": "anImage",
        "verse_french": "text",
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
        "post_image": "anImage",
        "post_text": "text",
        "post_type": "text",
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
        "post_image": "anImage",
        "post_text": "text",
        "post_type": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_qoute_list_view():
    instance1 = test_helpers.create_core_qoute()
    instance2 = test_helpers.create_core_qoute()
    client = Client()
    url = reverse("core_qoute_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_qoute_create_view():
    client = Client()
    url = reverse("core_qoute_create")
    data = {
        "qoute_date": datetime.now(),
        "qoute_image": "anImage",
        "qoute_hashtag": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_qoute_detail_view():
    client = Client()
    instance = test_helpers.create_core_qoute()
    url = reverse("core_qoute_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_qoute_update_view():
    client = Client()
    instance = test_helpers.create_core_qoute()
    url = reverse("core_qoute_update", args=[instance.pk, ])
    data = {
        "qoute_date": datetime.now(),
        "qoute_image": "anImage",
        "qoute_hashtag": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
