# from celery import Celery
#
# # Celery config to use rabbitmq
# celery_app = Celery('tasks', broker='pyamqp://guest@rabbitmq:5672//')
#
# celery_app.conf.update(
#     result_backend='rpc://',
# )