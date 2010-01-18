#!/usr/bin/env python

import os
import stat
from operator import itemgetter

internal_path = '.'
relative_url_path = '.'

image_extensions = ['jpeg', 'jpg']

def is_image(filename):
    for extension in image_extensions:
        if filename.endswith(extension):
            return True
    return False

def find_photos(dir):
    '''
    Finds the photos on the hard drive and returns them ordered by date
    '''
    photos = [(photo, os.stat(os.path.join(dir, photo))[stat.ST_MTIME]) for photo in os.listdir(dir) if is_image(photo.lower())]
    return [photo[0] for photo in sorted(photos, key=itemgetter(1))]

def build_feed(photos):
    
