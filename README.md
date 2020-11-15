# glight
Python package to control lights on Logitech devices

## Supported device
- G213
- G403hero

## Dependencies
- pyusb1.1.0
- python3.8

## Installation
```bash
$ python3 setup.py test
$ python3 setup.py bdist_wheel # generate package
$ sudo pip3 install ./dist/*.whl # install package
```

## Usage
```
$ sudo glight g213 --static
$ sudo glight g213 --help

$ sudo glight g403hero --static
$ sudo glight g403hero --help
```