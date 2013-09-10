# -*- coding: utf-8 -*-
import os
import time
import random
import hashlib

def get_random_filename(basename=None, ext=None):
    name = hashlib.sha1(
            str(random.random()) + \
            str(time.time())).hexdigest()
    if basename:
        ext = os.path.splitext(basename)[1]
    if ext:
        name = '%s%s' % (name, ext)
    return name

def get_size(file):
    file.seek(0, 2)
    size = file.tell()
    file.seek(0)
    return size


