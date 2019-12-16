# bottlewaste-rpi
A server-client based classifier attached with a robot.

## System Structure
![system_archi.png](system_archi.png)

## Hardware
```
- Raspberry PI 3B
- PI camera module
- Arduino
```
## Usage
#### For stream the PI camera module as server run following command -
``` python
    $ python stream_vfeed.py
```
#### To predict from the stream as a client run -
``` python
    $ python predict.py
```
#### Send data to arduino run -
``` python
    $ python to_arduino.py
```
