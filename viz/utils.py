import time
import os
import random
from datetime import datetime
from .data import image_directory

def cleanup_old_charts():
    now = time.mktime(datetime.now().timetuple())
    image_directory = 'viz/static/viz/'

    for filename in os.listdir(image_directory):
        fp = image_directory + filename
        time_created = os.path.getmtime(fp)
        if os.path.isfile(fp):
            if now - time_created > 300:
                os.remove(fp)

def new_chart_filepath():
    img_dir = os.listdir(image_directory)
    keys = [int(file.split('.')[0]) for file in img_dir]
    filename = random.randint(1000000,9999999)

    while filename in keys:
        filename = random.randint(1000000,9999999)
        
    return image_directory + str(filename) + '.jpg'