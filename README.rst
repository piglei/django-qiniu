django-qiniu
============

This package interages `Qiniu`_ could storage with `Django`_ framework.

Configuration
-------------

Add below lines in your django project's settings.py: ::

    QINIU_ACCESS_KEY = 'your_key'
    QINIU_SECRET_KEY = 'your_secret'
    QINIU_BUCKET_DEFAULT = 'your_bucket_name'

How To Use
----------

Use django-qiniu in your django project is very simple.

1. Add Field To Your Model
~~~~~~~~~~~~~~~~~~~~~~~~~~

Add `QiniuFileField` or `QiniuImageField` to your models.py to store file in
qiniu. ::

    from django.db import models
    from django_qiniu.fields import QiNiuImageField, QiniuFileField

    def qiniu_key_maker_file(instance, filename):
        """
        
        Args:
        ~~~~~

        - instance, your model instance being saved
        - filename, original filename
        
        This function should return a string object which is the key of qiniu.
        """

    def qiniu_key_maker_user_image(instance, filename):
        pass

    class Photo(models.Model):
        qiniu_file = QiNiuFileField(upload_to=qiniu_key_maker_file, null=True)
        qiniu_image = QiNiuImageField(upload_to=qiniu_key_maker_image, null=True)

QiniuFileField's init method uses these parameters:

- upload_to, a function to generate qiniu key, see upper codes.
- upload_bucket, bucket_name, if not given, will use settings.QINIU_BUCKET_DEFAULT as default.
- domain, your qiniu static domain ,if not givin, will use ('%s.qiniudn.com' % upload_bucket)
  as default.

QiniuImageField is a subclass of QiniuFileField and designed to store especially image files.

2. Save your uploaded file in views.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    f = request.FILES['file']
    obj = Photo()   
    obj.qiniu_file = f
    # Calling save method will upload this file to qiniu server
    obj.save()

How to use saved qiniu instance?
--------------------------------

QiniuFileField
~~~~~~~~~~~~~~

You can get the file url by: **instance.qiniu_file.url**

QiniuImageField
~~~~~~~~~~~~~~~

For QiniuImageField, There is a convient method called `get_image_view` which is used
to get thumbnails of your images, such as: ::

    instance.qiniu_image.get_image_view(mode=1, width=280, height=280, quality=75)
    instance.qiniu_image.get_image_view(mode=2, width=640, quality=75)

For more information, visit(http://docs.qiniu.com/api/v6/image-process.html)

.. _Qiniu: http://www.qiniu.com
.. _Django: https://www.djangoproject.com/

