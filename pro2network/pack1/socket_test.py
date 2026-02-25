# socket: 소켓(Socket)은 프로세스가 네트워크 세계로 데이터를 내보내거나
# 혹은 그 세계로부터 데이터를 받기 위한 실제적인 창구 역할을 한다.
# 그러므로 프로세스가 데이터를 보내거나 받기 위해서는 
# 반드시 소켓을 열어서 소켓에 데이터를 써보내거나 소켓으로부터 
# 데이터를 읽어들여야 한다.
# socket이란 TCP/IP의 프로그래머 인터페이스이다. 
# 통신 기기간 대화가 가능하도록 하는 통신방식으로 클라이언트/서버 모델에 기초한다
# 연결지향: TCP/IP
# 비연결지향

# socket 통신 확인

import socket

# 각 서비스별 포트번호 출력
print(socket.getservbyname('http', 'tcp'))  # www 환경 전송규약
print(socket.getservbyname('ssh', 'tcp'))   # 원격 컴퓨터 접속(보안)
print(socket.getservbyname('ftp', 'tcp'))   # 파일 전송
print(socket.getservbyname('smtp', 'tcp'))  # 메일 송수신
print(socket.getservbyname('pop3', 'tcp'))  # 이메일

# 'daum', 'naver' 사이트의 ip 주소 확인 
print(socket.getaddrinfo('www.daum.net', 80, proto = socket.SOL_TCP))   
print(socket.getaddrinfo('www.naver.com', 80, proto = socket.SOL_TCP))  

# 실제 사이트에 접속할 때는 도메인 이름을 통해 ip를 확인하여 접속하는 것
# ping : 상대방에게 핑을 날려 연결이 정상적인지 확인