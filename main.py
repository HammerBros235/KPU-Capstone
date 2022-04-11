import cv2
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from Chat import *
from ChatBox import *
from Host import *
from Problem import *


class problem_resister(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 200, 900, 700)
        global problem_info
        global init
        global mode

        if mode == "register":

            problem_register_final = QPushButton('최종 등록 버튼', self)
            problem_register_final.resize(325, 80)

            self.setWindowTitle('문제 만들기')

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

            problem_title_edit = QLineEdit(self)
            problem_importance_edit = QLineEdit(self)
            problem_right_edit = QLineEdit(self)
            problem_photo_edit = QPushButton('내부 저장소에서 가져오기', self)
            problem_contents_edit = QTextEdit(self)

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

            def addP(self):
                global problem_info
                global problem_num
                global myUI
                global problems
                global pMain

                problem = Problem()
                if problem_title_edit.text() == '':
                    problem_info.setText("제목을 입력해주세요")

                elif problem_importance_edit.text() == '':
                    problem_info.setText("중요도를 입력해주세요")

                elif problem_right_edit.text() == '':
                    problem_info.setText("문제의 정답을 입력해주세요")

                elif problem_contents_edit.toPlainText() == '':
                    problem_info.setText("문제의 내용을 입력해주세요")

                else:
                    problem.title = problem_title_edit.text()
                    problem.num = problem_num
                    problem_num += 1
                    problem.importance = problem_importance_edit.text()
                    problem.right = problem_right_edit.text()
                    problem.contents = problem_contents_edit.toPlainText()
                    problems.append(problem)
                    problem_info.setText("문제를 성공적으로 만들었습니다")

                    myUI.window = problem_main()

            problem_register_final.clicked.connect(addP)

        elif mode == "edit":
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

        elif mode == "preview":


            self.setWindowTitle('문제 미리보기')

            problem_title = QLabel('문제 제목 : ', self)
            problem_importance = QLabel('중요도(%) : ', self)
            problem_right = QLabel('문제의 정답 : ', self)
            problem_contents = QLabel('문제 내용 : ', self)

            problem_title_edit = QLabel(checkedP.title, self)
            problem_importance_edit = QLabel(checkedP.importance, self)
            problem_right_edit = QLabel(checkedP.right+"  /  (실제 화면에서는 정답이 보이지 않고 정답 적는 칸이 있습니다)", self)
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

        self.show()


class problem_main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 200, 700, 600)
        global init
        global pMain
        global problems

        pMain = self

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

        problem_register = QPushButton('문제 등록', self)
        problem_delete = QPushButton('문제 삭제', self)
        problem_edit = QPushButton('문제 수정', self)
        problem_question = QPushButton('문제 출제', self)
        problem_preview = QPushButton('문제 미리보기', self)
        problem_autoSet = QPushButton('자동 설정', self)

        problem_register.resize(100, 100)
        problem_delete.resize(100, 100)
        problem_edit.resize(100, 100)
        problem_question.resize(100, 100)
        problem_preview.resize(100, 100)
        problem_autoSet.resize(100, 100)

        problem_register.move(800, 0)
        problem_delete.move(800, 100)
        problem_edit.move(800, 200)
        problem_question.move(800, 300)
        problem_preview.move(800, 400)
        problem_autoSet.move(800, 500)

        def problem_register_layout(self):
            global mode

            mode = "register"
            myUI.window = problem_resister()

        def problem_delete_layout(self):
            for problem in problems:
                if problem.radio.isChecked():
                    problem.radio.setParent(None)
                    index = problems.index(problem)
                    problems.remove(problem)

        def problem_edit_layout(self):
            global mode
            global checkedP

            for problem in problems:
                if problem.radio.isChecked():
                    mode = "edit"
                    checkedP = problem
                    myUI.window = problem_resister()
                    break

        def problem_question_layout(self):
            print("not implemented")

        def problem_preview_layout(self):
            global mode
            global checkedP

            for problem in problems:
                if problem.radio.isChecked():
                    mode = "preview"
                    checkedP = problem
                    myUI.window = problem_resister()
                    break

        def problem_autoSet_layout(self):
            print("not implemented")

        problem_register.clicked.connect(problem_register_layout)
        problem_delete.clicked.connect(problem_delete_layout)
        problem_edit.clicked.connect(problem_edit_layout)
        problem_question.clicked.connect(problem_question_layout)
        problem_preview.clicked.connect(problem_preview_layout)
        problem_autoSet.clicked.connect(problem_autoSet_layout)

        self.setWindowTitle('문제제공')
        self.resize(900, 600)
        self.show()

# --------------------------------------------------------


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
        global image

        run_video = True
        while run_video:
            ret, image = self.camera.read()
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            qt_image1 = QtGui.QImage(color_swapped_image.data,
                                     self.width,
                                     self.height,
                                     color_swapped_image.strides[0],
                                     QtGui.QImage.Format_RGB888)
            self.VideoSignal1.emit(qt_image1)
            push_button1.hide()
            image_viewer1.move(5, 20)

            loop = QEventLoop()
            QTimer.singleShot(25, loop.quit)  # 25 ms
            loop.exec_()

    @pyqtSlot()
    def canny(self):
        self.flag = 1 - self.flag


class ImageViewer(QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(Qt.WA_OpaquePaintEvent)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
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


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.buttons = []
        self.initUI()
        self.dialog_delete = QDialog()

    def initUI(self):
        global chatBox
        chatBox = ChatBox()

        global host
        host = Host()

        global myUI
        myUI = self

        global problems
        problems = []

        global problem_num
        problem_num = 1

        global init
        init = True

        global mode
        mode = None

        global checkedP
        checkedP = None

        problem_button = QPushButton('문제제공', self)
        problem_button.resize(100, 100)
        problem_button.move(40, 600)
        problem_button.clicked.connect(self.problem_win)

        participation_button = QPushButton('참여도부여', self)
        participation_button.resize(100, 100)
        participation_button.move(140, 600)

        exit_button = QPushButton('자리비움', self)
        exit_button.resize(100, 100)
        exit_button.move(240, 600)

        chatting_scroll = QScrollArea(self)
        chatting_scroll.resize(525, 400)
        chatting_scroll.move(650, 20)
        chatBoxLabel = QLabel(chatBox.chatbox)
        chatBoxLabel.resize(525, 400)
        chatting_scroll.setWidget(chatBoxLabel)

        chatting_input = QTextEdit(self)
        chatting_input.resize(425, 80)
        chatting_input.move(650, 420)

        chatting_button = QPushButton('채팅 입력', self)
        chatting_button.resize(100, 80)
        chatting_button.move(1075, 420)

        def addChat(self):
            newChat = Chat()
            newChat.comment = chatting_input.toPlainText()
            chatting_input.setText("")
            newChat.name = host.name
            chatBox.chatbox = chatBox.chatbox + \
                (newChat.name+") :"+newChat.comment+"\n")
            chatBoxLabel = QLabel(chatBox.chatbox)
            chatting_scroll.setWidget(chatBoxLabel)
            bar = chatting_scroll.verticalScrollBar()
            bar.rangeChanged.connect(lambda x, y: bar.setValue(y))

        chatting_button.clicked.connect(addChat)

        self.move(400, 100)
        self.resize(1200, 800)
        self.setWindowTitle('종합설계')
        self.show()

    def problem_win(self):
        self.window = problem_main()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    thread = QThread()
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)

    image_viewer1 = ImageViewer()

    vid.VideoSignal1.connect(image_viewer1.setImage)

    push_button1 = QPushButton('Start')
    push_button1.clicked.connect(vid.startVideo)

    vertical_layout = QVBoxLayout()
    horizontal_layout = QHBoxLayout()
    horizontal_layout.addWidget(image_viewer1)
    vertical_layout.addLayout(horizontal_layout)
    vertical_layout.addWidget(push_button1)

    layout_widget = MyApp()

    layout_widget.setLayout(vertical_layout)

    sys.exit(app.exec_())