# glight
Python package to control lights on Logitech devices

## Supported device
- G213
- G403hero

## Dependencies
- pyusb1.1.0
- python3.8

## Install and remove

install glight package

add service to run glight command on startup

```bash
$ ./install.sh
$ ./uninstall.sh
```

## Usage
```
$ sudo python3 -m ./glight --help
$ sudo python3 -m ./glight g213 --static

$ sudo glight g213 --static
$ sudo glight g213 --help

$ sudo glight g403hero --static
$ sudo glight g403hero --help
```
