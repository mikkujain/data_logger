import socket

target = "localhost"

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect(('localhost', 5000))

dic = "#STH:0000010,000;L:264;TM:140620120347;D:5;T:01;C:04;A01:0.100;A02:02000;A03:0.975;A04:25.20;A05:00000;A06:00000;A07:00000;A08:00000;A09:35.48;A10:27.00;A11:31.81;P01:12345681;P02:00000000;P03:64924223;P04:03725855;P05:00000000;P06:00000000;K01:10000000000;O01:0000;83;#"
# send some data (in this case a HTTP GET request)
client.send(dic)

# receive the response data (4096 is recommended buffer size)
response = client.recv(4096)

print response
