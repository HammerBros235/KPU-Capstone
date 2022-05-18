# 지금은 개발중이므로 한 공간에 넣어놓고 하지만, 완성될 쯤에는 클래스별로 파일로 쪼갠 후, import로 연결시킬 생각압니다.

import cv2
import sys
from AttFuncs import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5 import QtGui
from Chat import *  # 채팅 구현 클래스 import
from ChatBox import *  # 채팅창 구현 클래스 import
from Host import *  # 호스트 구현 클래스 import
from Participant import *  # 참여자 구현 클래스 import
from Problem import *  # 문제 구현 클래스 import
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor

from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import psutil
import collections
from my_function import *
from gaze_tracking import GazeTracking


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class problem_resister(QWidget):  # 문제 등록 창
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 200, 900, 700)  # 위치 및 크기 조정

        global problem_info  # 문제 정보
        global init  # 최초 생성일 경우 확인
        global mode  # 등록, 수정 등등 모드 확인

        if mode == "register":  # 등록 모드일 경우

            problem_register_final = QPushButton('최종 등록 버튼', self)
            problem_register_final.resize(325, 80)

            self.setWindowTitle('문제 만들기')  # 창 제목

            problem_register_final.move(25, 0)

            if init:  # 최초 생성일 경우
                problem_info = QLabel('항목들을 기입하고 최종 등록 버튼을 눌러주세요',
                                      self)
                problem_info.move(500, 0)
                init = False
            else:  # 아닌 경우
                problem_info = QLabel('항목들을 기입하고 최종 등록 버튼을 눌러주세요',
                                      self)
                problem_info.move(500, 0)
                init = False

            problem_title = QLabel('문제 제목 : ', self)  # 라벨(문자열)
            problem_importance = QLabel('중요도(%) : ', self)
            problem_right = QLabel('문제의 정답 : ', self)
            problem_photo = QLabel('사진 첨부하기(선택) : ', self)
            problem_contents = QLabel('문제 내용 : ', self)

            problem_title_edit = QLineEdit(self)  # edit창 (입력받는 곳)
            problem_importance_edit = QLineEdit(self)
            problem_right_edit = QLineEdit(self)
            problem_photo_edit = QPushButton('내부 저장소에서 가져오기', self)  # 사진, 미구현
            problem_contents_edit = QTextEdit(self)

            problem_contents_edit.resize(600, 120)  # 크기조정

            problem_title_edit.move(100, 100)  # 위치조정
            problem_importance_edit.move(100, 200)
            problem_right_edit.move(100, 300)
            problem_photo_edit.move(150, 390)
            problem_contents_edit.move(100, 450)

            problem_title.move(0, 100)
            problem_importance.move(0, 200)
            problem_right.move(0, 300)
            problem_photo.move(0, 400)
            problem_contents.move(0, 500)

            def addP(self):  # 문제를 problems에 넣는 함수
                global problem_info  # 문제 정보
                global problem_num  # 문제 번호
                global myUI  # 최초 윈도우 자신 (self를 대입해서 정의)
                global problems  # 첫번째 윈도우에서 정의한 문제들 집합
                global pMain  # 문제 윈도우 자신 (self를 대입해서 정의)

                problem = Problem()  # 문제 생성

                # 이제 if문들로 정보가 제대로 입력되었는지 확인
                if problem_title_edit.text() == '':
                    problem_info.setText("제목을 입력해주세요")

                elif problem_importance_edit.text() == '':
                    problem_info.setText("중요도를 입력해주세요")

                elif problem_importance_edit.text().isnumeric() == False:
                    problem_info.setText("정수의 중요도를 입력해주세요 (0~100)")

                elif int(problem_importance_edit.text()) > 100:
                    problem_info.setText("정수의 중요도를 입력해주세요 (0~100)")

                elif problem_right_edit.text() == '':
                    problem_info.setText("문제의 정답을 입력해주세요")

                elif problem_contents_edit.toPlainText() == '':
                    problem_info.setText("문제의 내용을 입력해주세요")

                else:  # 문제 정보들 입력
                    problem.title = problem_title_edit.text()
                    problem.num = problem_num
                    problem_num += 1
                    problem.importance = problem_importance_edit.text()
                    problem.right = problem_right_edit.text()
                    problem.contents = problem_contents_edit.toPlainText()
                    problems.append(problem)
                    problem_info.setText("문제를 성공적으로 만들었습니다")

                    myUI.window = problem_main()

            problem_register_final.clicked.connect(addP)  # 버튼을 위의 addP 함수랑 연결

        elif mode == "edit":  # 수정 모드일 경우, 아래 내용은 등록모드와 유사하므로 주석은 패스
            global checkedP

            problem_register_final = QPushButton('최종 수정 버튼', self)
            problem_register_final.resize(325, 80)

            self.setWindowTitle('문제 수정하기')

            problem_register_final.move(25, 0)

            if init:
                problem_info = QLabel('항목들을 기입하고 최종 등록 버튼을 눌러주세요',
                                      self)
                problem_info.move(500, 0)
                init = False
            else:
                problem_info = QLabel('항목들을 기입하고 최종 등록 버튼을 눌러주세요',
                                      self)
                problem_info.move(500, 0)
                init = False

            problem_title = QLabel('문제 제목 : ', self)
            problem_importance = QLabel('중요도(%) : ', self)
            problem_right = QLabel('문제의 정답 : ', self)
            problem_photo = QLabel('사진 첨부하기(선택) : ', self)
            problem_contents = QLabel('문제 내용 : ', self)

            problem_title_edit = QLineEdit(checkedP.title, self)
            problem_importance_edit = QLineEdit(checkedP.importance, self)
            problem_right_edit = QLineEdit(checkedP.right, self)
            problem_photo_edit = QPushButton('내부 저장소에서 가져오기', self)
            problem_contents_edit = QTextEdit(checkedP.contents, self)

            problem_contents_edit.resize(600, 120)

            problem_title_edit.move(100, 100)
            problem_importance_edit.move(100, 200)
            problem_right_edit.move(100, 300)
            problem_photo_edit.move(150, 390)
            problem_contents_edit.move(100, 450)

            problem_title.move(0, 100)
            problem_importance.move(0, 200)
            problem_right.move(0, 300)
            problem_photo.move(0, 400)
            problem_contents.move(0, 500)

            def editP(self):
                global problem_info
                global problem_num
                global myUI
                global problems
                global pMain

                problem = checkedP
                if problem_title_edit.text() == '':
                    problem_info.setText("제목을 입력해주세요")

                elif problem_importance_edit.text() == '':
                    problem_info.setText("중요도를 입력해주세요")

                elif problem_importance_edit.text().isnumeric() == False:
                    problem_info.setText("정수의 중요도를 입력해주세요 (0~100)")

                elif int(problem_importance_edit.text()) > 100:
                    problem_info.setText("정수의 중요도를 입력해주세요 (0~100)")

                elif problem_right_edit.text() == '':
                    problem_info.setText("문제의 정답을 입력해주세요")

                elif problem_contents_edit.toPlainText() == '':
                    problem_info.setText("문제의 내용을 입력해주세요")

                else:
                    problem.title = problem_title_edit.text()
                    problem.importance = problem_importance_edit.text()
                    problem.right = problem_right_edit.text()
                    problem.contents = problem_contents_edit.toPlainText()
                    problem_info.setText("문제를 성공적으로 수정했습니다")
                    myUI.window = problem_main()

            problem_register_final.clicked.connect(editP)

        elif mode == "preview":  # 미리보기 모드일 경우, 아래 내용은 등록모드와 유사하므로 주석은 패스

            self.setWindowTitle('문제 미리보기')

            problem_title = QLabel('문제 제목 : ', self)
            problem_importance = QLabel('중요도(%) : ', self)
            problem_right = QLabel('문제의 정답 : ', self)
            problem_contents = QLabel('문제 내용 : ', self)

            problem_title_edit = QLabel(checkedP.title, self)
            problem_importance_edit = QLabel(checkedP.importance, self)
            problem_right_edit = QLabel(
                checkedP.right+"  /  (실제 화면에서는 정답이 보이지 않고 정답 적는 칸이 있습니다)", self)
            problem_contents_edit = QLabel(checkedP.contents, self)

            problem_contents_edit.resize(600, 120)

            problem_title_edit.move(100, 100)
            problem_importance_edit.move(100, 200)
            problem_right_edit.move(100, 300)
            problem_contents_edit.move(100, 450)

            problem_title.move(0, 100)
            problem_importance.move(0, 200)
            problem_right.move(0, 300)
            problem_contents.move(0, 500)

        self.show()  # 이게 있어야 버튼이나 라벨들이 보입니다.


class problem_main(QMainWindow):  # 문제 윈도우

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 200, 700, 600)  # 위치, 크기 조정
        global pMain  # 자기 자신 (self)
        global problems  # 문제들 집합

        pMain = self
# -------------------------------------------------
# 해당 내용은 문제들을 UI로 넣기 위한 스크롤이 있는 위젯을 만드는 과정입니다.
# 안드로이드 스튜디오랑 달라서 고생을 많이 한 부분입니다.
        self.scrollW = QWidget()
        self.scrollW2 = QWidget()

        self.scrollW2.setMinimumSize(500, 600)
        self.setCentralWidget(self.scrollW)

        self.scrollBox = QVBoxLayout()
        self.scrollP = QScrollArea(self)
        self.scrollP.resize(500, 600)
        self.scrollW.setLayout(self.scrollBox)
        self.scrollP.setWidget(self.scrollW2)
        self.scrollBox.addWidget(self.scrollP)

        for problem in problems:
            problem.radio = QRadioButton(
                str(problem.num)+"  "+problem.title, pMain.scrollW2)
            problem.radio.resize(400, 20)
            problem.radio.move(20, 20*problem.num)
# -----------------------------------------------------

        problem_register = QPushButton('문제 등록', self)  # 문제 관련 버튼 등록
        problem_delete = QPushButton('문제 삭제', self)
        problem_edit = QPushButton('문제 수정', self)
        problem_question = QPushButton('문제 출제', self)
        problem_preview = QPushButton('문제 미리보기', self)
        problem_autoSet = QPushButton('자동 설정', self)

        problem_register.resize(100, 100)  # 크기 조정
        problem_delete.resize(100, 100)
        problem_edit.resize(100, 100)
        problem_question.resize(100, 100)
        problem_preview.resize(100, 100)
        problem_autoSet.resize(100, 100)

        problem_register.move(800, 0)  # 위치 조정
        problem_delete.move(800, 100)
        problem_edit.move(800, 200)
        problem_question.move(800, 300)
        problem_preview.move(800, 400)
        problem_autoSet.move(800, 500)

        def problem_register_layout(self):  # 등록 함수
            global mode

            mode = "register"  # 모드 설정
            myUI.window = problem_resister()

        def problem_delete_layout(self):  # 삭제 함수
            for problem in problems:
                if problem.radio.isChecked():
                    problem.radio.setParent(None)
                    index = problems.index(problem)
                    problems.remove(problem)

        def problem_edit_layout(self):  # 수정 함수
            global mode
            global checkedP

            for problem in problems:
                if problem.radio.isChecked():
                    mode = "edit"  # 모드 설정
                    checkedP = problem
                    myUI.window = problem_resister()
                    break  # 체크된 문제를 찾은 후 루프 탈출

        def problem_question_layout(self):  # 출제 함수, 미구현
            print("not implemented")

        def problem_preview_layout(self):  # 미리보기 함수
            global mode
            global checkedP

            for problem in problems:
                if problem.radio.isChecked():
                    mode = "preview"  # 모드 설정
                    checkedP = problem
                    myUI.window = problem_resister()
                    break

        def problem_autoSet_layout(self):  # 자동 설정, 미구현
            print("not implemented")

        problem_register.clicked.connect(
            problem_register_layout)  # 버튼을 함수들과 연결
        problem_delete.clicked.connect(problem_delete_layout)
        problem_edit.clicked.connect(problem_edit_layout)
        problem_question.clicked.connect(problem_question_layout)
        problem_preview.clicked.connect(problem_preview_layout)
        problem_autoSet.clicked.connect(problem_autoSet_layout)

        self.setWindowTitle('문제제공')
        self.resize(900, 600)
        self.show()


class participation_give(QMainWindow):  # 참여도 부여 윈도우

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 200, 900, 700)  # 위치, 크기 조정
        global problems

# ---------------위의 스크롤 복붙---------------------------
        self.scrollW = QWidget()
        self.scrollW2 = QWidget()

        self.scrollW2.setMinimumSize(500, 600)
        self.setCentralWidget(self.scrollW)

        self.scrollBox = QVBoxLayout()
        self.scrollP = QScrollArea(self)
        self.scrollP.resize(500, 600)
        self.scrollW.setLayout(self.scrollBox)
        self.scrollP.setWidget(self.scrollW2)
        self.scrollBox.addWidget(self.scrollP)
# ------------------------------------------------
        tempNum = 1  # 아래의 for문에서 위치 변경을 위해 정의

        for participant in participants:  # 참여자들을 UI로 보이게 하는 작업
            if participant.exit:
                participantsB = QCheckBox(str(participant.name)+"        참여도: "+str(
                    participant.participation)+"  (자리비움)", self.scrollW2)
            else:
                participantsB = QCheckBox(str(
                    participant.name)+"        참여도: "+str(participant.participation), self.scrollW2)

            participant.radio = participantsB
            participantsB.resize(400, 20)  # 크기 조정
            participantsB.move(20, 20*tempNum)  # 위치 조정
            tempNum += 1  # 위치를 한단계 내림

        give = QPushButton('참여도 부여', self)  # 참여도 부여 버튼, 누르면 참여도를 부여
        give.resize(100, 100)
        give.move(800, 0)

        howMuchGive = QLabel("부여할 참여도 : ", self)  # 라벨(문자열)
        howMuchGive.move(420, 20)

        error = QLabel("정수의 참여도를 입력하세요 ", self)  # 라벨 (문자열)
        error.resize(200, 20)
        error.move(420, 70)

        howMuchGive = QLineEdit(self)  # 문자열 입력 받는 곳 (참여도를 얼마나 부여할지)
        howMuchGive.move(500, 20)

        def participationAdd(self):  # 실제 참여도 부여를 구현한 함수
            global participants

            for participant in participants:

                if participant.radio.isChecked():  # 체크된 것을 확인

                    whole_number = False  # 정수가 아닌걸로 초기화

                    try:  # 정수인지 확인
                        int(howMuchGive.text())
                        whole_number = True  # 맞으면 true

                    except ValueError:
                        whole_number = False  # 틀리면 False

                    if whole_number:  # 정수인가?
                        # 맞을 경우 참여도 부여
                        participant.participation += int(howMuchGive.text())

                        if participant.participation < 0:  # 0이 최소
                            participant.participation = 0

                        elif participant.participation > 100:  # 100이 최대
                            participant.participation = 100

            myUI.window = participation_give()  # 창을 다시 띄워서 변경사항 적용

        give.clicked.connect(participationAdd)  # 버튼과 함수를 연결

        self.setWindowTitle('참여도부여')  # 창 제목
        self.resize(900, 600)  # 창 크기
        self.show()  # UI 보여주기


class graph(QMainWindow):  # 그래프 윈도우

    def __init__(self):
        super().__init__()
        self.setWindowTitle('graph_win')
        self.setGeometry(100, 200, 900, 700)  # 위치, 크기 조정
        
        self.main_widget = QWidget()
        vbox = QVBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)


#---------------------------------------
        gaze_centered = collections.deque(np.zeros(10))
        gaze_centered_avg = collections.deque(np.zeros(10))
        
        global cnt
        cnt = 0

        self.fig = plt.figure(figsize=(12, 6), facecolor='#DEDEDE')
        self.canvas = FigureCanvasQTAgg(self.fig)
        
        self.ax = plt.subplot(121)
        self.ax1 = plt.subplot(122)

        self.ax.set_facecolor('#DEDEDE')
        self.ax1.set_facecolor('#DEDEDE')
        
        vbox.addWidget(self.canvas)
        self.addToolBar(NavigationToolbar(self.canvas, self))

        animation = FuncAnimation(plt.gcf(), my_function, interval=1000)
#---------------------------------------
        self.ani = animation
        self.canvas.draw()
        self.show()

# --------------------------------------------------------

# 비디오 보여주는 클래스, 전체적으로 잘 몰라서 주석을 달 수 없습니다..
# 다만 길이가 길진 않습니다.


class ShowVideo(QObject):

    flag = 0

    camera = cv2.VideoCapture(0)

    ret, image = camera.read()
    height, width = image.shape[:2]

    VideoSignal1 = pyqtSignal(QtGui.QImage)

    def __init__(self, parent=None):
        super(ShowVideo, self).__init__(parent)

    @pyqtSlot()
    def startVideo(self):

        def detect(gray, frame):
            

            qt_image1 = QtGui.QImage(gray.data,
                                     self.width,
                                     self.height,
                                     gray.strides[0],
                                     QtGui.QImage.Format_RGB888)
            self.VideoSignal1.emit(qt_image1)
            push_button1.hide()
            # image_viewer1.move(5, 20)

            loop = QEventLoop()
            QTimer.singleShot(25, loop.quit)  # 25 ms
            loop.exec_()

            return frame

        global image
        video_capture = cv2.VideoCapture(0)
        

        global coordinate_info
        
        gaze = GazeTracking()
        while True:
            _, frame = video_capture.read()  # 캠의 화면을 이미지로 자자름
            
            gaze.refresh(frame)
            frame = gaze.annotated_frame()
            
            text = ""
            if gaze.is_blinking():
                text = "Blinking"
                coordinate_info.setText("실시간 시선: 깜박임 감지")
            elif gaze.is_right():
                text = "Looking right"
                coordinate_info.setText("실시간 시선: 우측 시선 감지")
            elif gaze.is_left():
                text = "Looking left"
                coordinate_info.setText("실시간 시선: 좌측 시선 감지")
            elif gaze.is_center():
                text = "Looking center"
                coordinate_info.setText("실시간 시선: 중앙 시선 감지")
                
            cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()
            cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
            cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    
            gray = cv2.cvtColor(frame, cv2.cv2.COLOR_BGR2RGB)
            canvas = detect(gray, frame)

            k = cv2.waitKey(1) & 0xff
            # FF는 끝의 8bit만을 이용한다는 뜻으로 ASCII 코드의 0~255값만 이용하겠다는 의미로 해석됨. (NumLock을 켰을때도 마찬가지)

    @pyqtSlot()
    def canny(self):
        self.flag = 1 - self.flag


class ImageViewer(QWidget):
    global x2, y2, w2, h2, ex2, ey2, ew2, eh2
    x2, y2, w2, h2, ex2, ey2, ew2, eh2 = 1, 1, 1, 1, 100, 100, 100, 100

    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(Qt.WA_OpaquePaintEvent)

    def paintEvent(self, event):  # 실제 사각형을 그리는 함수, 이벤트를 받을때마다 동작하는 것 같습니다.
        # 아직 고쳐햐할 부분입니다
        painter = QtGui.QPainter(self)
        painter.setBrush(QColor(25, 0, 90, 10))
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    def initUI(self):
        self.setWindowTitle('Test')

    @pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()
# ------------------------------------------------------------------------------------------------


class MyApp(QWidget):  # 최초의 윈도우이자 (웹캠영상, 채팅, 버튼3개)가 기본적으로 들어가있는 윈도우

    def __init__(self):
        super().__init__()
        self.buttons = []
        self.initUI()

    def initUI(self):

        global chatBox, host, participants, myUI, problems, problem_num, init, mode, checkedP, isExit
        global points, point_index, pD
        points = []
        point_index = 0
        pD = pDiff(Point(100, 100, 100, 100), Point(200, 200, 150, 150))

        chatBox = ChatBox()  # 채팅 박스
        host = Host()  # 호스트
        # 참여자들 담고있는 리스트, 참여자 4명으로 초기화
        participants = [Participant(), Participant(),
                        Participant(), Participant()]
        myUI = self  # 자기 자신 (initUI)
        problems = []  # 문제들을 담고있는 리스트, 문제 등록 화면에서 문제가 추가됩니다.
        problem_num = 1  # 문제 번호 초기화 , 문제 등록 화면에서 1씩 증가
        init = True  # 처음 창을 열었다면 True , (문제 등록창에서의 라벨이 중복 등록되지 않도록 하기 위함)
        mode = None  # 등록, 수정, 미리보기를 구별하기 위한 모드
        checkedP = None  # 체크된 문제를 저장하는 변수

        participants[0].participation = 30  # 참여자 참여도 초기화
        participants[1].participation = 80
        participants[2].participation = 60
        participants[3].participation = 90

        host.name = "호스트"  # 호스트 이름 초기화
        participants[0].name = "민수"  # 참여자 이름 초기화
        participants[1].name = "빌제리안"
        participants[2].name = "첸"
        participants[3].name = "마유"

        problem_button = QPushButton('문제제공', self)  # 문제제공 버튼
        problem_button.resize(100, 100)  # 크기조정
        problem_button.move(40, 600)  # 위치 조정
        problem_button.clicked.connect(self.problem_win)  # 버튼을 함수와 연결

        participation_button = QPushButton('참여도부여', self)  # 참여도 부여 버튼
        participation_button.resize(100, 100)
        participation_button.move(140, 600)
        participation_button.clicked.connect(self.participation_win)

        exit_button = QPushButton('자리비움\n(호스트용)', self)  # 자리비움 버튼
        exit_button.resize(100, 100)
        exit_button.move(240, 600)
        global exit_host
        exit_host = QLabel('호스트) 자리비움 비활성화 상태', self)  # 자리비움 상황
        exit_host.resize(400, 30)
        exit_host.move(500, 650)
        exit_button.move(240, 600)
        exit_button.clicked.connect(self.exit_set)  # 버튼을 함수와 연결

        graph_button = QPushButton('통계 그래프', self)  # 참여도 부여 버튼
        graph_button.resize(100, 100)
        graph_button.move(340, 600)
        graph_button.clicked.connect(self.graph_win)

        global coordinate_info
        coordinate_info = QLabel('실시간 시선 감지',
                                 self)
        coordinate_info.move(500, 600)
        coordinate_info.resize(300, 40)

# -------------------------------------------------------------
# 채팅창을 위한 부분 (스크롤)

        chatting_scroll = QScrollArea(self)
        chatting_scroll.resize(525, 400)
        chatting_scroll.move(650, 20)
        chatBoxLabel = QLabel(chatBox.chatbox)
        chatBoxLabel.resize(525, 400)
        chatting_scroll.setWidget(chatBoxLabel)
# --------------------------------------------------------------
        chatting_input = QTextEdit(self)  # 채팅 입력 받는 부분
        chatting_input.resize(425, 80)
        chatting_input.move(650, 420)

        chatting_button = QPushButton('채팅 입력', self)  # 채팅 입력 후 누르는 버튼
        chatting_button.resize(100, 80)
        chatting_button.move(1075, 420)

        def addChat(self):  # 채팅 내용을 채팅박스에 넣는 함수
            newChat = Chat()
            newChat.comment = chatting_input.toPlainText()
            chatting_input.setText("")  # 채팅 입력창 초기화
            newChat.name = host.name
            chatBox.chatbox = chatBox.chatbox + \
                (newChat.name+") :"+newChat.comment+"\n")
            chatBoxLabel = QLabel(chatBox.chatbox)
            chatting_scroll.setWidget(chatBoxLabel)
            bar = chatting_scroll.verticalScrollBar()
            # 내용이 많아 스크롤 아래에도 존재할 경우 스크롤 자동 내림
            bar.rangeChanged.connect(lambda x, y: bar.setValue(y))

        chatting_button.clicked.connect(addChat)  # 채팅 버튼과 채팅 함수의 연결

        self.move(400, 100)
        self.resize(1200, 800)
        self.setWindowTitle('종합설계')  # 윈도우 이름
        self.show()

    def problem_win(self):  # 문제 관련 창 열기
        self.window = problem_main()

    def participation_win(self):  # 참여도 부여 관련 창 열기
        self.window = participation_give()

    def graph_win(self):  # 그래프 관련 창 열기
        self.window = graph()

    isExit = False  # 호스트의 자리를 비운 상태 초기화

    def exit_set(self):  # 자리비움 설정
        global exit_host
        if myUI.isExit:
            myUI.isExit = False
            exit_host.setText("호스트) 자리비움 비활성화 상태 -> 전체 학생 자리비움 해제")

            for participant in participants:
                participant.exit = False
        else:
            myUI.isExit = True
            exit_host.setText("호스트) 자리비움 활성화 상태 -> 전체 학생 자리비움 ")

            for participant in participants:
                participant.exit = True


if __name__ == '__main__':
    app = QApplication(sys.argv)

    thread = QThread()  # 스레드
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)  # 웹캠은 스레드로 따로 관리
    image_viewer1 = ImageViewer()

    vid.VideoSignal1.connect(image_viewer1.setImage)

    push_button1 = QPushButton('Start')  # 스타트 버튼 누르면 웹캠 연결
    push_button1.clicked.connect(vid.startVideo)

    vertical_layout = QVBoxLayout()
    horizontal_layout = QHBoxLayout()

    horizontal_layout.setAlignment(Qt.AlignTop)
    horizontal_layout.addStretch(0)
    horizontal_layout.addWidget(image_viewer1)
    horizontal_layout.addStretch(1)

    vertical_layout.addLayout(horizontal_layout)
    vertical_layout.addWidget(push_button1)

    layout_widget = MyApp()  # 메인 화면 열림

    layout_widget.setLayout(vertical_layout)

    sys.exit(app.exec_())
