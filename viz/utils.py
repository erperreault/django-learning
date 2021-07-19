import time
import os
import random
from datetime import datetime, timedelta
from .data import image_directory
from .models import User
import pytz

def cleanup_old_charts():
    now = time.mktime(datetime.now().timetuple())
    image_directory = 'viz/static/viz/'

    for filename in os.listdir(image_directory):
        fp = image_directory + filename
        time_created = os.path.getmtime(fp)
        if os.path.isfile(fp):
            if now - time_created > 300:
                os.remove(fp)

def cleanup_old_collections():
    us = User.objects.all()
    for x in us:
        if datetime.now(pytz.utc) - x.creation_time > timedelta(minutes=5):
            print('Entry older than 5 minutes; deleting...')
            x.delete()
        else:
            print('Entry younger than 5 minutes; loading...')


def new_chart_filepath():
    img_dir = os.listdir(image_directory)
    keys = [int(file.split('.')[0]) for file in img_dir]
    filename = random.randint(1000000,9999999)

    while filename in keys:
        filename = random.randint(1000000,9999999)
        
    return image_directory + str(filename) + '.jpg'