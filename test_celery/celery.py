from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://ron:ron123@localhost/ron_vhost',
             #backend='rpc://',
             include=['test_celery.tasks'])
