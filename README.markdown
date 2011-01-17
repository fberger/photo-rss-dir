Testing
=======

To test the cgi script change the location of PHOTO_DIR in the settings.py file to point to the photos folder in the photo-rss-dir. Then run:

   python -m CGIHTTPServer
   curl http://localhost:8000/cgi-bin/photorssdir.py

The result should look like this:

    <?xml version="1.0" encoding="UTF-8"?><rss xmlns:media="http://search.yahoo.com/mrss/" version="2.0"><channel><title>title</title><link>http://localhost/</link><description>description</description><item><title>gpl.jpg</title><media:content type="image/jpeg" url="http://localhost/photos/gpl.jpg" /></item></channel></rss>

