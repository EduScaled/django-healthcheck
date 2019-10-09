=====
Django Health Ckecks
=====

Checks django project services states: database, celery, rabbitmq. Givs separate api endpoints for every service and common status page.

Quick start
-----------

1. Add this lines to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'health_check',
        'health_check.db',
        'health_check.cache',
        'health_check.contrib.celery',
        'health_check.contrib.rabbitmq',        
        'django_health_check',
    ]

2. Include this line in your project urls.py like this::

    path('django-healthcheck/', include('django_health_check.urls')),

3. Make sure this vars is set in settings.py:
   
   BROKER_URL = amqp://myuser:mypassword@localhost:5672/myvhost
   CELERY_RESULT_BACKEND = "amqp"

4. Visit http://127.0.0.1:8000/django-healthcheck/all to check all checks is working or make requests

-----------

200 - OK , 500 - UNAVAILABLE.

### Database
`curl -v -X GET -H "Accept: application/json" http://127.0.0.1:8000/django-healthcheck/db`

### RabbitMQ
`curl -v -X GET -H "Accept: application/json" http://127.0.0.1:8000/django-healthcheck/rabbitmq`

### Celery
`curl -v -X GET -H "Accept: application/json" http://127.0.0.1:8000/django-healthcheck/celery`

### Cache
`curl -v -X GET -H "Accept: application/json" http://127.0.0.1:8000/django-healthcheck/cache`

### All
`curl -v -X GET -H "Accept: application/json" http://127.0.0.1:8000/django-healthcheck/all` 

