from setuptools import setup

import glight.constants as constants

setup(
    name=constants.PROGRAM_NAME,
    version=constants.VERSION,
    install_requires=["pyusb==1.1.0"],
    author='Jérémy Diot',
    author_email='diot.jeremy@gmail.com',
    keywords='logitech device color light rgb led',
    description='Python package to control lights on Logitech devices',
    url='https://github.com/jeremydiot/logitechColor',
    packages=['glight', 'glight.devices', 'glight.commons', 'glight.cli'],
    license="MIT",
    platforms='ALL',
    entry_points={
        'console_scripts': [constants.PROGRAM_NAME+'=glight.__main__:main'],
    }
)
