import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-healthcheck',
    version='1.0',
    packages=find_packages(),
    test_suite='tests',
    install_requires=['django-health-check==3.9.0'],
    include_package_data=True,
    license='MIT License',
    description='Checks django project services states: database, celery, rabbitmq. Givs separate api endpoints for every service and common status page.',
    long_description=README,
    keywords="Django health checks rabbit celery database",
    url='https://www.example.com/',
    author='Vladimir Mikryukov',
    author_email='motobiker2008@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
