#!/usr/bin/env python

import os
import stat
from operator import itemgetter
import datetime

from BuildMRSS import *

import settings
import facebook

image_extensions = ['jpeg', 'jpg']

def is_image(filename):
    for extension in image_extensions:
        if filename.endswith(extension):
            return True
    return False

def get_facebook_photos():
    try:
        graph = facebook.GraphAPI(settings.FACEBOOK_OAUTH_TOKEN)
        photos = graph.get_connections('me', 'photos')
        data = photos['data']
        photos = []
        for photo in data:
            created_time = datetime.datetime.strptime(photo['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
            source = photo['source']
            photos.append((source, created_time))
        return photos
    except:
        return []

def find_photos(dir, url_prefix):
    '''
    Finds the photos on the hard drive and returns them ordered by date
    '''
    photos = [(url_prefix + photo, datetime.datetime.utcfromtimestamp(os.stat(os.path.join(dir, photo))[stat.ST_MTIME])) for photo in os.listdir(dir) if is_image(photo.lower())]
    photos.extend(get_facebook_photos())
    return [photo[0] for photo in sorted(photos, key=itemgetter(1), reverse=True)]

def build_item(photo):
    return MRSSItem(photo, contents = [MRSSMediaContent(photo, type="image/jpeg")])

def build_channel(photos):
    channel = MRSSChannel('title', 'http://localhost/', 'description')
    channel.items = [build_item(photo) for photo in photos]
    return channel
    
def print_channel(channel):
    print channel_to_mrss(channel)

if __name__ == "__main__":
    print "Content-Type: text/xml; charset=utf-8\n"
    print_channel(build_channel(find_photos(settings.PHOTO_DIR,
                                            settings.SERVER_PATH)))

