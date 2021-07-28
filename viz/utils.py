import time
import os
from datetime import datetime, timedelta
from .models import User
import pytz

# Simple functions to clean up chart image files and database entries older than 5 minutes.

def cleanup_old_charts():
    """Remove chart files older than 5 minutes."""
    now = time.mktime(datetime.now().timetuple())
    image_directory = 'viz/static/viz/'

    for filename in os.listdir(image_directory):
        fp = image_directory + filename
        time_created = os.path.getmtime(fp)
        if os.path.isfile(fp):
            if now - time_created > 300:
                os.remove(fp)

def cleanup_old_collections():
    """Remove user collections in database older than 5 minutes."""
    us = User.objects.all()
    for x in us:
        if datetime.now(pytz.utc) - x.creation_time > timedelta(minutes=5):
            print('Entry older than 5 minutes; deleting...')
            x.delete()
        else:
            print('Entry younger than 5 minutes; loading...')