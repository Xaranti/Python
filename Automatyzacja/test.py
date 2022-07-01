import os
f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
your_ip=f.read()