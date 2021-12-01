from setuptools import setup

setup(
    name='pretty_time_package',
    version='0.1',
    description='description',
    url='http://github.com/name/package_name',
    author='Alex',
    author_email='AlexVE36@yandex.ru',
    license='MIT',
    packages=['my_namespace.get_pretty_time_package'],
namespace_packages=['my_namespace'],
    entry_points={
        'console_scripts': [
            'get_time_pp=my_namespace.get_pretty_time_package.pretty_time:main'
        ]
    }
)
