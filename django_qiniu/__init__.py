# -*- coding: utf-8 -*-
import qiniu.conf
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

__author__ = 'piglei <piglei2007@gmail.com>'
__version__ = (0, 0, 1)

for attr in ('QINIU_ACCESS_KEY', 'QINIU_SECRET_KEY', 'QINIU_BUCKET_DEFAULT'):
    if not hasattr(settings, attr):
        raise ImproperlyConfigured("You must define the %s before using django-qiniu" % attr)

qiniu.conf.ACCESS_KEY = settings.QINIU_ACCESS_KEY
qiniu.conf.SECRET_KEY = settings.QINIU_SECRET_KEY


