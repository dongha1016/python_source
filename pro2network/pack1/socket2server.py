import socket
import sys

HOST = ''  # HOST = '127.0.0.1'과 같은 의미 
PORT = 7788
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversock.bind((HOST, PORT))
    serversock.listen(5)   # client와 연결 정보수(리스너 설정)
    print('서버(무한루핑) 서비스 중...')

    while(True):
        conn, addr = serversock.accept()   # 수동적으로 연결을 받아들임
        print('client info : ', addr[0], ' ', addr[1])
        print(conn.recv(1024).decode()) # 수신 메시지 출력
        
        # 메시지 송신 to client - 송신이기 때문에 encode로
        conn.send(('from server : ' + str(addr[1]) + ' 너도 잘지내라').encode('utf_8'))


except Exception as err:
    print('err: ', err)
    sys.exit() # 강제종료
finally:
    conn.close()
    serversock.close()