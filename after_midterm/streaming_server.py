import socket
import cv2
import numpy as np

BUF_SIZE = 8192  # 버퍼 크기 설정 (데이터 전송 시 한 번에 전송되는 데이터의 최대 크기)
LENGTH = 10  # 전송할 데이터의 길이 정보를 나타내는 문자열의 길이

videoFile = 'test.mp4'  # 전송할 비디오 파일
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP/IP 소켓 생성
sock.bind(('', 5000))  # 모든 인터페이스에서 5000번 포트로 들어오는 연결을 수락하도록 바인딩
sock.listen(5)  # 동시에 5개까지의 클라이언트 연결 대기

while True:
    csock, addr = sock.accept()  # 클라이언트 연결 수락
    print('Client connected:', addr)  # 클라이언트의 주소 출력
    
    cap = cv2.VideoCapture(videoFile)  # 비디오 파일을 읽기 위한 객체 생성
    
    while cap.isOpened():  # 비디오 파일이 정상적으로 열렸는지 확인
        ret, frame = cap.read()  # 비디오에서 한 프레임씩 읽기
        if ret:  # 프레임 읽기가 성공했는지 확인
            temp = csock.recv(BUF_SIZE)  # 클라이언트로부터 데이터 받기 (동기화를 위해 사용)
            if not temp:  # 연결이 종료되었는지 확인
                break
            
            result, imgEncode = cv2.imencode('.jpg', frame)  # 현재 프레임을 JPEG 이미지로 인코딩
            data = np.array(imgEncode)  # 인코딩된 이미지를 numpy 배열로 변환
            byteData = data.tobytes()  # numpy 배열을 바이트 데이터로 변환
            
            # 인코딩된 이미지의 길이 정보를 클라이언트에 전송
            # zfill(LENGTH)을 사용하여 항상 일정한 길이를 가지도록 0으로 채움
            csock.send(str(len(byteData)).zfill(LENGTH).encode())
            
            temp = csock.recv(BUF_SIZE)  # 클라이언트로부터 데이터 받기 (동기화를 위해 사용)
            if not temp:  # 연결이 종료되었는지 확인
                break
            
            csock.send(byteData)  # 인코딩된 이미지 데이터 전송
        else:
            break  # 비디오의 끝에 도달하면 반복문 종료
    
    cap.release()  # 비디오 파일 닫기
    cv2.destroyAllWindows()  # 생성된 모든 OpenCV 윈도우 제거
    csock.close()  # 클라이언트 소켓 연결 종료
