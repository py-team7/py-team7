#quizapp.py
from quizans import *
from graphics import *
from button import Button

class Question:
    def __init__(self, win):
        self.questions = [
                        {"question":"AXELL", "answer":"A", "comment":"AXELL is an idol group of five people."},
                        {"question":"asfi", "answer":"A", "comment":"asfi is an idol group in Shibuya."},
                        {"question":"Ada", "answer":"B", "comment":"Ada is a programming language.\n" + " \n" + "It derives from the name of Ada Lovelace, the world's first programmer."},
                        {"question":"Curl", "answer":"B", "comment":"Curl is a programming language."},
                        {"question":"IDL", "answer":"B", "comment":"IDL is a programming language.\n" + " \n" +"IDL stands for Interactive Data Language"},
                        {"question":"P.IDL", "answer":"A", "comment":"P.IDL is a female idol group"},
                        {"question":"Cupitron", "answer":"A", "comment":"Cupitron is a trio techno pop idol."},
                        {"question":"Clojure", "answer":"B", "comment":"Clojure is a programming language."},
                        {"question":"GEM", "answer":"A", "comment":"GEM is a female idol group"},
                        {"question":"Ook!", "answer":"B", "comment":"Ook! is a programming language made for orangutans by joke.\n" + " \n" + "Programming can be done just by listening to the orangutan 's bark."}
                        ]
        self.win = win
        self.num = 0
        self.redraw(0)

    def redraw(self, num):
        if  num == 1:
            self.message_quiz.undraw()

        if  num == 2:
            self.message_ans.undraw()
        
        if  num == 3:
            self.message_right.undraw()

        if  num == 4:
            self.message_ans.undraw()
            self.message_right.undraw()

    def quizlen(self):
        length = len(self.questions)
        return length

    def getquiz(self, num):
        self.num = num
        self.question = self.questions[self.num]["question"]
        return self.question

    def getanswer(self):
        self.answer = self.questions[self.num]["answer"]
        return self.answer
    
    def lookquiz(self):
        if self.num != 0:
            self.redraw(1)
        self.message_quiz = Text(Point(40, 140), self.questions[self.num]["question"])
        self.message_quiz.setSize(24)
        self.message_quiz.draw(self.win)

    def lookans(self):
        if self.num!= 0:
            self.redraw(2)
        self.message_ans = Text(Point(100, 30), self.questions[self.num]["comment"])
        self.message_ans.draw(self.win)

    def lookright(self, ans):
        if self.num!= 0:
            self.redraw(3)
        if(self.answer == ans):
            self.message_right = Text(Point(100, 85), "Yeah! Got it!")
            self.message_right.setFill("blue")
        else:
            self.message_right = Text(Point(100, 85), "Wrong!")
            self.message_right.setFill("red")
        self.message_right.setSize(36)
        self.message_right.draw(self.win)

    def result(self, point):
        if point >= 8:
            good = Image(Point(100, 75), "congratulation.png")
            good.draw(self.win)
        else:
            white = bad = Image(Point(100, 75), "white.gif")
            white.draw(self.win)
            bad = Image(Point(100, 75), "mission_failed.png")
            bad.draw(self.win)

        message_point = Text(Point(100, 40), str(point) + " / 10")
        message_point.setSize(36)
        
        message_point.draw(self.win)


class Launch:
    def __init__(self):
        self.win = GraphWin("Idol or Program Quiz", 800, 600)
        self.win.setCoords(0, 0, 200, 150)
        self.win.setBackground("white")

        rect1 = Rectangle(Point(26, 45), Point(86, 130))
        rect1.setFill("lightgray")
        rect1.draw(self.win)

        rect2 = Rectangle(Point(114, 45), Point(174, 130))
        rect2.setFill("lightgray")
        rect2.draw(self.win)

        pink = Image(Point(56, 100), "pink.png")
        pink.draw(self.win)

        blue = Image(Point(144, 100), "blue.png")
        blue.draw(self.win)
        
        
        self.button = Quizans(self.win)

        self.quiz = Question(self.win)
        self.count = 0

    def run(self):
        len = self.quiz.quizlen()

        for index in range(len):
            self.quiz.getquiz(index)
            topic_answer = self.quiz.getanswer()
            self.quiz.lookquiz()

            player_answer = self.button.answer()
            self.quiz.lookright(player_answer)
            self.quiz.lookans()
            if player_answer == topic_answer:
                self.count = self.count + 1

            next = False
            while(next == False):
                next = self.button.next()
            
            self.quiz.redraw(4)
        
        self.quiz.result(self.count)
            
        while True:
    
            key = self.win.checkKey()
            if key in ["q", "Q"]:
                break
        self.win.close()
                    
                                                                                                                                                                                                                                                                                                                                                                                                                                             

if __name__ == "__main__":
    Launch().run()
