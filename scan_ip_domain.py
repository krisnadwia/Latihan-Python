# import libraries
import socket
import subprocess
import os
import sys

# aktivitas membersihkan layar
subprocess.call('clear', shell=True)

# masukkan domain
try:
    server = input('masukkan domain: ')
    serverip = socket.gethostbyname(server)
    # tampilkan IP
    print('IP address nya adalah: ', serverip)
except socket.error:
    print('cek internet Anda')
    sys.exit()