port = 2222 # номер порта, идентифицирующий сокет
host = '0.0.0.0' # сервер и клиент выполняются на локальном компьютере
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM # переносимый API сокетов	

def server_start():
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind((host, port))
	sock.listen(50)
	return sock

def server_thread(sock, i):
	while True:
		conn, addr = sock.accept()
		serv_name = serv_thread[i].getName()
		#print(serv_name,' connection ')
		while True:
			data = conn.recv(1024)
			# print(serv_name, ' working; data=', data)
			if not data or data == (b'close'): break
			conn.send(data)
		#print(serv_name,' connection closed')
		conn.close()

sock = server_start()
serv_thread = []
for i in range(10):
	serv_thread.append(Thread(target=server_thread, args=(sock,i)))
	serv_thread[i].daemon = True 
	serv_thread[i].start()
	serv_thread[i].setName('serv%s'%i)
	print(serv_thread[i].getName(), ' started')
try:
        while True: pass
except KeyboardInterrupt:
        print('interrupted!')
