import socket

dst_ip = str(input("Enter Server IP: "))

s = socket.socket()
#S = socket.socket()
print ("Successful creation of socket:")
dport = 12345
s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("socket is listening")
c, addr = s.accept()
print ('Got connection from:', addr)

rcmsg = c.recv(1024).decode()
map = {
  'key1': 'val1','key2': 'val2','key3': 'val3','key4': 'val4', 'key5': 'val5','key6': 'val6'
}
while rcmsg:
	if rcmsg in map:
		final_responce = map[rcmsg]
	else:
		final_responce = 'Error 404: Not found'
	c.send(final_responce.encode())
	rcmsg = c.recv(1024).decode()