# smarter-coffee-api
Python script that acts as an Unofficial API for a Smarter Coffee machine - http://smarter.am/coffee/

Designed to be used on a RaspberryPi, but could be run on anything with python, and easily be wrapped in a web service to act as a REST API.

Basic installation guide: http://adenforshaw.com/smarter-coffee-machine-raspberry-pi-iot-coffeetime/

Methods: a string passed as the only parameter.
- "ip" - [mandatory] the ip of the coffee machine
- "reset" - [optional] resets the machine to default settings. Useful to test with and saves your beans.
- "brew" - [optional] Starts brewing with current settings. It'll respond with success, or the appropriate error message.
- "cups [1..12]" - [optional] Sets the cup to whatever you asked. It'll respond with success, or the appropriate error message. You then have to call "brew".

Example:
```script
python smarter-coffee-api xxx.xxx.xxx.xxx --cups=3
```

Response:
- success: boolean
- message: string
- return_code

Installation:
- Clone the repo to your machine
- Edit the IP address to that of your Smarter Coffee machine
- Call from the command line e.g. $python smarter-coffee-api.py brew

Version:
- Very early version - v0.1

ToDo:
- Add more error checking
- Add more methods (cup size, brew strength etc)
- Document example of how to wrap as a web service.
