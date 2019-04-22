from django.conf.urls import url
from health_check.views import MainView

from health_checkers.views import RabbitMQHealthCheckView, DBHealthCheckView, CeleryHealthCheckView

urlpatterns = [
    url(r'rabbitmq', RabbitMQHealthCheckView.as_view(), name='rabbitmq_health_check'),
    url(r'db', DBHealthCheckView.as_view(), name='db_health_check'),
    url(r'celery', CeleryHealthCheckView.as_view(), name='celery_health_check'),
    url(r'all', MainView.as_view(), name='health_check_home'),
]

