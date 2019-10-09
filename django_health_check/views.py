from django.http import JsonResponse
from health_check.views import MainView

from django_health_check.helpers import check_service


class RabbitMQHealthCheckView(MainView):
    def render_to_response_json(self, plugins, status):
        check_class_name = 'RabbitMQHealthCheck'
        result, status = check_service(check_class_name, plugins)
        return JsonResponse(result, status=status)

    def render_to_response(self, plugins, status):
        raise NotImplementedError


class DBHealthCheckView(MainView):
    def render_to_response_json(self, plugins, status):
        check_class_name = 'DatabaseBackend'
        result, status = check_service(check_class_name, plugins)
        return JsonResponse(result, status=status)

    def render_to_response(self, plugins, status):
        raise NotImplementedError


class CeleryHealthCheckView(MainView):
    def render_to_response_json(self, plugins, status):
        check_class_name = 'CeleryHealthCheckCelery'
        result, status = check_service(check_class_name, plugins)
        return JsonResponse(result, status=status)

    def render_to_response(self, plugins, status):
        raise NotImplementedError


class CacheHealthCheckView(MainView):
    def render_to_response_json(self, plugins, status):
        check_class_name = 'CacheBackend'
        result, status = check_service(check_class_name, plugins)
        return JsonResponse(result, status=status)

    def render_to_response(self, plugins, status):
        raise NotImplementedError