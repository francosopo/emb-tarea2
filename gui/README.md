# INSTALL

## PYTHONPATH
Include this root directory (gui) into the PYTHONPATH environment variable

## DEPENDENCIES
install pyserial:
```sh
pip install pyserial
```

## CONFIG FILE
Create a conf.ini file inside this root (gui) directory
``ìni
[DEFAULT]
WINDOW_LENGTH=50

[SERIAL]
PORT=/dev/ttyUSB0
BAUD_RATE=115200
TIMEOUT=1
```