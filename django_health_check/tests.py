from unittest import TestCase

from django_health_check.helpers import check_service


class Plugin:
    def __init__(self, status):
        self.status = status

    def identifier(self):
        return self.__class__.__name__


class DatabaseBackend(Plugin):
    def __init__(self, status):
        super().__init__(status)


class RabbitMQHealthCheck(Plugin):
    def __init__(self, status):
        super().__init__(status)


class CeleryHealthCheckCelery(Plugin):
    def __init__(self, status):
        super().__init__(status)


class HealthCheckServiceTestCase(TestCase):
    def _get_available_plugins(self, status=0):
        return [DatabaseBackend(status), RabbitMQHealthCheck(status), CeleryHealthCheckCelery(status)]


    def test_check_service_status(self):

        plugins=[]
        check_class_name = 'CeleryHealthCheckCelery'
        result, status = check_service(check_class_name, plugins)
        self.assertEquals({}, result)
        self.assertEquals(status, 500)

        #Все неработающие плагины (status=0)
        plugins = self._get_available_plugins(status=0)

        #Неизвесный plugin
        check_class_name = 'UnregistredInPluginsClassName'
        result, status = check_service(check_class_name, plugins)
        self.assertEquals({}, result)
        self.assertEquals(status, 500)

        check_class_name = 'DatabaseBackend'
        result, status = check_service(check_class_name, plugins)
        self.assertEquals(result, {check_class_name: 'unavailable'})
        self.assertEquals(status, 500500)

        check_class_name = 'RabbitMQHealthCheck'
        result, status = check_service(check_class_name, plugins)
        self.assertEquals(result, {check_class_name: 'unavailable'})
        self.assertEquals(status, 500)

        check_class_name = 'CeleryHealthCheckCelery'
        result, status = check_service(check_class_name, plugins)
        self.assertEquals(result, {check_class_name: 'unavailable'})
        self.assertEquals(status, 500)


        #Все активные плагины (status=1)
        plugins = self._get_available_plugins(status=1)

        check_class_name = 'DatabaseBackend'
        result, status = check_service(check_class_name, plugins)
        self.assertEquals(result, {check_class_name: 'working'})
        self.assertEquals(status, 200)

        check_class_name = 'RabbitMQHealthCheck'
        result, status = check_service(check_class_name, plugins)
        self.assertEquals(result, {check_class_name: 'working'})
        self.assertEquals(status, 200)

        check_class_name = 'CeleryHealthCheckCelery'
        result, status = check_service(check_class_name, plugins)
        self.assertEquals(result, {check_class_name: 'working'})
        self.assertEquals(status, 200)