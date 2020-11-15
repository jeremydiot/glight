from setuptools import setup
import src

setup(
    name='gcolor',
    version=src.__version__,
    install_requires=["pyusb==1.1.0"],
    author='Jérémy Diot',
    author_email='diot.jeremy@gmail.com',
    keywords='logitech device color rgb led',
    description='Python package to control lights on Logitech devices',
    url='https://github.com/jeremydiot/logitechColor',
    packages=['src', 'src.devices', 'src.commons'],
    license="MIT",
    platforms='ALL',
    entry_points={
        'console_scripts': ['gcolor=src.cli.main:main'],
    }
)
