#!/usr/bin/env python
import sys
import socket
import argparse

#method names to validate
API_METHOD_BREW = "brew"
API_METHOD_RESET = "reset"
API_METHOD_CUPS = "cups"

parser = argparse.ArgumentParser()
parser.add_argument("ip", help="the ip the coffee machine is on")
parser.add_argument("--reset", help="resets the machine to default settings", action='store_true')
parser.add_argument("--brew", help="starts brewing with current settings", action='store_true')
parser.add_argument("--cups", help="sets the cup quantity (1..12). You have to call brew next", type=int, default=0)
args = parser.parse_args()

#IP address of the smarter coffee machine on your network
TCP_IP = args.ip
TCP_PORT = 2081
BUFFER_SIZE = 10

#method to call
if args.brew:
	message_to_send = "7"
elif args.reset:
	message_to_send = "\x10"
elif args.cups >= 1 and args.cups <= 12:
	message_to_send = "\x36%s\x7e" % chr(args.cups)
else:
  print 'no valid command'
  sys.exit()

#make connection to machine and send message
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(message_to_send)
	data = s.recv(BUFFER_SIZE)
	s.close()
except socket.error, msg:
	print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
	sys.exit();

#convert response from machine to unicode
return_code = unicode(data)

#set default values to ouput
success=0
message=""

#find out what the machine response means
if return_code =="\x03\x00~":
	success=1
	message="success"
elif return_code=="\x03\x01~":
	message="already brewing"
elif return_code=="\x03\x04~":
	message="invalid command"
elif return_code=="\x03\x05~":
	message="no carafe"
elif return_code=="\x03\x06~":
	message="no water"
elif return_code=="\x03i~":
	success=1
	message="reset"
else:
	message="check machine"

#ouput to whatever called this script
print 'success (n=0,y=1): ' + success + ', message: ' + message+ ', return_code: '+ repr(data)[1:10]

quit()
sys.exit()
