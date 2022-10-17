#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Participant():  # 참여자
    PARTICIPATION_MAX = 100
    PARTICIPATION_MIN = 0

    participation = PARTICIPATION_MIN
    name = "Anonymous"
    exit = False  # 자리비움 여부
    clicked = False  # 지정여부
    id = "undecided"  # undecided는 나중에  그 값이 정해졌는지 안정해졌는지 함수에서 판단할때 사용
    pwd = "undecided"
    email = "undecided"
    radio = None
    problems = []

    def set_name(name):  # 이름 String 대입
        self.name = name

    def set_exit(exit):  # true 혹은 false를 대입
        self.exit = exit

    def set_clicked(clicked):  # true 혹은 false를 대입
        self.clicked = clicked

    def set_id(id):  # 아이디 String 대입
        self.id = id

    def set_pwd(pwd):  # 비밀번호 String 대입
        self.pwd = pwd

    def set_email(email):  # 이메일 String 대입
        self.email = email
# ----------------------------------------------------------

    def use_chat(chatBox, comment):
        chat = Chat()
        chat.name = name
        # chat.comment = 컨트롤러와 연결 필요, ChatInput에서 값을 가져옴
        chatBox.chatbox.append(chat)

