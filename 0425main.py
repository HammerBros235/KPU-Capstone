import numpy as np
import cv2
# Cascades 디렉토리의 haarcascade_frontalface_default.xml 파일을 Classifier로 사용
# faceCascade는 이미 학습 시켜놓은 XML 포멧이고, 이를 불러와서 변수에 저장.
faceCascade = cv2.CascadeClassifier('D:\python\Cascade\haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('D:\python\Cascade\haarcascade_eye.xml')

# def 함수는 haar알고리즘을 이용하여 얼굴눈을 찾는 함수
# input은 grayscale 이미지
# output은 얼굴과 눈에 사각형이 그려진 이미지 프레임

def detect(gray,frame):
    # 아래줄은 CascadeClassifier을 이용해서 얼굴을 인식
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(100,100),flags=cv2.CASCADE_SCALE_IMAGE)
    # 얼굴에 사각형을 테두리화 하고 눈을 탐색
    for(x, y, w, h) in faces:
        #얼굴 : 이미지 프레임의 x,y 에서 시작함, (x+넓이, y+길이)까지의 사각형 (a,b,c)는 테두리 색 2는 테두리굵기
        cv2.rectangle(frame, (x,y),(x + w, y + h), (255, 0, 0), 2)

        face_gray = gray[y:y + h, x:x +w]
        face_color = frame[y:y + h, x:x + w]

        # 아래는 얼굴영역 안에서 눈을 찾는것
        eyes = eyeCascade.detectMultiScale(face_gray, 1.1, 3)

        # 눈: 이미지 프레임의 x,y에서 시작함, (x+넓이, y+길이)까지의 사각형 (a,b,c)는 테두리 색 2는 테두리굵기
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex, ey), (ex + ew, ey+ eh), (0, 255, 0), 2)

    return frame
# 웹캠 이미지 가져오기
video_capture = cv2.VideoCapture(0)

while True:
    _, frame = video_capture.read() # 캠의 화면을 이미지로 자자름
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)

    cv2.imshow("video", canvas) # 캠 화면 출력
# q 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 리소스 해제
video_capture.release()
cv2.destroyAllWindows()

