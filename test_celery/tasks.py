from __future__ import absolute_import
from test_celery.celery import app
import time


@app.task
def longtime_add(x, y):
    print ('long time add task begins')
    # sleep 5 seconds
    time.sleep(10)
    print ('long time add task finished')
    return x + y

@app.task
def longtime_minus(x, y):
    print ('long time minus task begins')
    # sleep 5 seconds
    time.sleep(10)
    print ('long time minus task finished')
    return x - y
