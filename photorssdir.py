#!/usr/bin/env python

import os
import stat
from operator import itemgetter

from BuildMRSS import *

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

def build_item(photo, url_prefix):
    return MRSSItem(photo, contents = [MRSSMediaContent(url_prefix + photo, type="image/jpeg")])

def build_channel(photos, url_prefix):
    channel = MRSSChannel('title', 'http://localhost/', 'description')
    channel.items = [build_item(photo, url_prefix) for photo in photos]
    return channel
    
def print_channel(channel):
    print channel_to_mrss(channel)

if __name__ == "__main__":
    print "Content-Type: text/xml\n\n"
    print_channel(build_channel(find_photos('photos/'),
                                'http://localhost/photos/'))
