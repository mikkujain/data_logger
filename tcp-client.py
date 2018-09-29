# from __future__ import unicode_literals

import socket

# from devices.models import Devices, Ports, Data, Mobile, Alert

# def data(self):
# 	queryset = Alert.objects.filter()[:4]
# 	s.sendall(queryset.encode('utf-8'))

# s.close()

# if __name__ == "__main__":
# 	s = socket.socket()
# 	
# 	port = 8000

# 	s.connect((host,port))


s = socket.socket()
host = socket.gethostname()
port = 8000

s.connect((host,port))

filename = "Ethernet Alarm Data.txt"
f = open(filename,'rb')
print('Sending...')
l = "#STH:000002,000;L:264;TM:140620120347;D:5;T:01;C:04;A01:0.000;A02:00000;A03:0.975;A04:25.20;A05:00000;A06:00000;A07:00000;A08:00000;A09:35.48;A10:27.00;A11:31.81;P01:12345681;P02:00000000;P03:64924223;P04:03725855;P05:00000000;P06:00000000;K01:10000000000;O01:0000;83;#"
while (l):
    print('Sending...')
    s.sendall(l)
    l = f.read(1024)
f.close()

# var = "#STH:000002,000;L:264;TM:140620120347;D:5;T:01;C:04;A01:0.000;A02:00000;A03:0.975;A04:25.20;A05:00000;A06:00000;A07:00000;A08:00000;A09:35.48;A10:27.00;A11:31.81;P01:12345681;P02:00000000;P03:64924223;P04:03725855;P05:00000000;P06:00000000;K01:10000000000;O01:0000;83;#"

# s.sendall(var.encode('utf-8'))

s.close()