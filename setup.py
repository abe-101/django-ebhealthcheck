from setuptools import find_packages, setup

setup(
    name='django-ebhealthcheck',
    version='1.0',
    license='BSD',
    author='Sam Kingston',
    author_email='sam@sjkwi.com.au',
    description='Django app to add an instance\'s public IP to ALLOWED_HOSTS for Elastic Beanstalk\'s health check system',
    url='https://github.com/sjkingo/django-ebhealthcheck',
    install_requires=['requests'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
