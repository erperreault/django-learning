import time
import os
from datetime import datetime

def cleanup_old_charts():
    now = time.mktime(datetime.now().timetuple())
    image_directory = 'viz/static/viz/'

    for filename in os.listdir(image_directory):
        fp = image_directory + filename
        time_created = os.path.getmtime(fp)
        if os.path.isfile(fp):
            if now - time_created > 300:
                os.remove(fp)