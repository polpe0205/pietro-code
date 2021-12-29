from os import pipe
from subprocess import STDOUT, Popen, PIPE
import subprocess
for ip in range (100,130):
    ipAddress= '192.168.0.248.'str(ip)
    subprocess = Popen (['/bin/ping','-c 1', ipAddress], stdout = PIPE, stdin = PIPE,ßß