class Problem():  # 문제
    title = "undecided"
    importance = "undecided"
    right = "undecided"
    content = "undecided"
    num = "undecided"
    time = "undecided"
    photo = "undecided"
    radio = None

    def set_problem(self, title, importance, right, content, num, time, photo):  # 문제 만들기 및 수정
        self.title = title
        self.importance = importance
        self.right = right
        self.content = content
        self.num = num
        self.time = time
        self.photo = photo

    def get_problem(self):  # 문제 가져오기
        return [self.title, self.importance, self.right, self.content, self.num, self.time, self.photo]

    def show(self):
        temp = 1
        # 문제 보여주기 (미구현)

# 나머지 기능들은 추후에


prob = Problem()
prob.set_problem("problemMath", 10, 24, "3X8", "1", 120, "D:/workspace")
prob.get_problem()