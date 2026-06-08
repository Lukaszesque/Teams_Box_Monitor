REPOSITORY STRUCTURE:

PYTHON/ARDUINO:
The repo is split between two services communicating with each other. Each folder contains it's respective code.

    Python -> config.py:
    A place to put any config on the client side, for example the IP address of the ESP32

    Python -> teams_client.py
    Responsible for initiating the Teams Websocket, and instructions on what needs to happen when Teams publishes a change to it's state

    Python -> 
    esp32_client.py:
    Responsible for sending out a request to the ESP32 which contains the state of teams taken from the websocket. Gets called from teams_client.py

    Python -> heartbeat.py
    Responsible for health checking the device. It probes the server for a response, and times out if the response isn't recieved, indicating that the device might not be working properly. If hearbeat is working correctly, the 'Device on' LED is lit up.

Arduino:
    teams_box_server.ino:
    Contains a simple server which recieves input from the python client and uses it to control the LED's depending on their state.