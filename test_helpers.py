import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from core import models as core_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_core_theme(**kwargs):
    defaults = {}
    defaults["theme_from_date"] = datetime.now()
    defaults["theme_hashtag"] = ""
    defaults["theme_to_date"] = datetime.now()
    defaults["theme"] = ""
    defaults.update(**kwargs)
    return core_models.theme.objects.create(**defaults)
def create_core_post(**kwargs):
    defaults = {}
    defaults["datetime"] = datetime.now()
    defaults["english"] = ""
    defaults["hashtag"] = ""
    defaults["post_type"] = ""
    defaults["post_text"] = ""
    defaults["french"] = ""
    defaults["kirundi"] = ""
    defaults.update(**kwargs)
    return core_models.post.objects.create(**defaults)
def create_core_post_image(**kwargs):
    defaults = {}
    defaults["post_image"] = ""
    if "post" not in kwargs:
        defaults["post"] = create_core_post()
    defaults.update(**kwargs)
    return core_models.post_image.objects.create(**defaults)
