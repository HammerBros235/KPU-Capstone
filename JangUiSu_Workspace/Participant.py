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

    def add_problem(problem):  # 참여자들이 풀 문제 추가하기
        self.problems.append(problem)

    def get_problems():  # 문제를 하나씩 띄워주는 기능 (미구현)
        for problem in self.problems:
            problem.show()
            # 구현해야할 부분

