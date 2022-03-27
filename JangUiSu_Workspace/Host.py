#!/usr/bin/env python
# coding: utf-8

# In[15]:


import Participant
import Problem


class host():  # 호스트
    name = "Anonymous"
    exit = False  # 자리비움 여부
    clicked = False  # 지정여부
    id = "undecided"  # undecided는 나중에  그 값이 정해졌는지 안정해졌는지 함수에서 판단할때 사용
    pwd = "undecided"
    email = "undecided"
    problems = []

    participants = []  # 참여자들 집합
    clicked_participants = []  # 지정된 참여자들 집합 (참여도를 부여시 사용)
    Problems = []  # 호스트가 등록한 전체 문제들
# -------------------------------------------------------------------------------

    def add_edit_problem(self, title, importance, right,  # 문제 등록 및 수정
                         content, num, time, photo):
        problem = Problem()
        problem.set_problem(title, importance, right,
                            content, num, time, photo)
        self.problems.append(problem)

    def del_problem(self, problem):  # 문제 삭제
        Problems.remove(problem)

    def give_participation(self, participant, participation):  # 참여도 부여
        participants[participants.index(
            participant)].participation += participation
# -------------------------------------------------------------------------------

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
# -------------------------------------------------------------------------------

    def make_problem(self, title, importance, right, content, num, time, photo):  # 문제 만들기 및 수정
        problem = Problem()
        problem.title = title
        problem.importance = importance
        problem.right = right
        problem.content = content
        problem.num = num
        problem.time = time
        problem.photo = photo
        return problem
        
    def add_problem(problem):  # 참여자들이 풀 문제 추가하기
        for participant in participants:
            participant.problems.append(problem)

    def get_problems():  # 문제를 하나씩 띄워주는 기능 (미구현)
        for problem in self.problems:
            problem.show()
            # 구현해야할 부분


# In[ ]:




