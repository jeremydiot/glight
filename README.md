# logitechColor
Python package to control lights on Logitech devices

## Dependencies
- pyusb 
```bash
sudo pip3 install pyusb
```

## Installation
python3 setup.py bdist_wheel
pip install ./dist/*.whl


## Usage

## Source

## TODO
- random color
- user interface
- installation process
- start with linux session
- check input color string
- requirement ?? fonctionnement
- show line and file name with glog
- verbose
- rename to logitechLighting / glight
    - github
    - cli
    - setup
    - readme
    - ...

```
NAME 
    GColor - Control Logitech devices lights

SYNOPSIS
    gcolor DEVICE_NAME OPTIONS
OPTIONS
    -h, --help
        Show options for specific device
        
-----------------------------------------------

NAME
    G213 options

SYNOPSIS
    gcolor g213 OPTIONS
                ‾‾‾‾‾‾‾
OPTIONS
    -d, --disable
        turn off the device's lights

    -s, --static [color1... color5]
                  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ 
        static color mode

    -c, --cycle [frequency]
                 ‾‾‾‾‾‾‾‾‾
        Cycle through all colors

    -w, --wave [direction frequency]
                ‾‾‾‾‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾
        

    -b, --breathe [color frequency]
                   ‾‾‾‾‾ ‾‾‾‾‾‾‾‾‾
        Single color breathing

    -e, --start-effect [state]

VALUES
    color
        RRGGBB hexadecimal value (000000 to ffffff)
        
        default: 00A9E0

    frequency
        milliseconds number (1000 to 20000)

        default: 10000

    direction
        0, 1, 2 or 3
        
        0: letf to right
        1: right to left 
        2: center to edge
        3: edge to center

        default: 0

    state
        true or false

        default: true


    See DEVICE_NAME options 
    -s, --static [COLORS]...
                 ‾‾‾‾‾
        Static color mode

    -c, --cycle [RATE] [BRIGHTNESS]
                 ‾‾‾‾   ‾‾‾‾‾‾‾‾‾‾
        Cycle through all colors

    -b, --breathe [COLORS] [RATE] [BRIGHTNESS]
                   ‾‾‾‾‾‾   ‾‾‾‾   ‾‾‾‾‾‾‾‾‾‾
        Single color breathing

    -i, --intro true|false
                ‾‾‾‾‾‾‾‾‾‾
        Enable/disable startup effect

COLORS
    name or RGB hexadecimal value 
    
    name: see "./data/color.json" file
    hexadecimal: RRGGBB (000000 to ffffff)
    
    default: (name: Aqua, hex: 00ffff)

RATE
    milliseconds number (1000 to 20000)

    default: 10000

BRIGHTNESS
    Percentage number (0 to 100)

    default: 100

```