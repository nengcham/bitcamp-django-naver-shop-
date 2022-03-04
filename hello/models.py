import random

class Quiz01Calculator:
    def __init__(self, num1, opcode, num2, ):
        self.num1 = num1
        self.num2 = num2
        self.opcode = opcode

    def res(self):
        if self.opcode == '+':
            result = self.num1 + self.num2
        elif self.opcode == '-':
            result = self.num1 - self.num2
        elif self.opcode == '*':
            result = self.num1 * self.num2
        elif self.opcode == '/':
            result = self.num1 / self.num2
        return result

class Quiz02Bmi:
    @staticmethod
    def getBmi(member):
        this = member
        return this.weight * 10000 / this.height / this.height

    @staticmethod
    def res(member):
        this = member
        getBmi = Quiz02Bmi.getBmi(this)
        if getBmi >= 35:
            res = '고도 비반'
        elif getBmi >= 30:
            res = '중도 비만 (2단계 비만)'
        elif getBmi >= 25:
            res = '경도 비만 (1단계 비만)'
        elif getBmi >= 23:
            res = '과체중'
        elif getBmi >= 18.5:
            res = '정상'
        else:
            res = '저체중'
        return res

class Quiz03Grade:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def chkPass(self):
        return '합격' if Quiz03Grade.avg(self) >= 60 else '불합격'

class Quiz04GradeAuto:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def getGrade(self):
        pass

    def chkPass(self):
        return '합격' if Quiz04GradeAuto.avg(self) >= 60 else '불합격'

def myRandom(start, end):
    return random.randint(start, end)

class Quiz05Dice:
    @staticmethod
    def dice():
        return myRandom(1, 6)

class Quiz07RandomChoice:
    def __init__(self):
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                  '권혜민', '서성민', '조현국', '김한슬', '김진영',
                  '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                  '최민서', '한성수', '김윤섭', '김승현',
                  '강 민', '최건일', '유재혁', '김아름', '장원종'
                  ]
    def randomMember(self):
        return self.members[myRandom(0, len(self.members)-1)]

class Quiz08Rps:
    def __init__(self, playerRsp):
        self.rps = ['가위', '바위', '보']
        self.player = playerRsp - 1
        self.com = myRandom(0, 2)
        self.playerResult = self.rps[self.player]
        self.comResult = self.rps[self.com]

    def rpsRes(self):
        p = self.player
        c = self.com
        return 'Lose' if (p + 1) % 3 == c else 'Draw' if p == c else 'Win'

class Quiz09GetPrime:
    def __init__(self, num):
        self.num = num

    def getPrime(self):
        res = ""
        for i in range(2, self.num):
            count = 0
            for j in range(2, i+1):
                if i % j == 0:
                    count += 1
            if count == 1:
                res += str(i) + "\t"
        return res

class Quiz10LeapYear:
    def __init__(self, year):
        self.year = year

    def leapYear(self):
        y = self.year
        return '윤년 입니다.' if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else '평년 입니다.'

class Quiz11NumberGolf:
    def __init__(self, user):
        self.user = user

    def golf(self):
        count = 0
        num = myRandom(1, 100)
        numEnter = self.user
        while num != numEnter:
            if numEnter > 100:
                res = '잘못된 숫자 입니다.'
            elif numEnter < num:
                res = 'up'
                count += 1
            elif numEnter > num:
                res = 'down'
                count += 1
            numEnter = int(input(res))
        return f'정답입니다! {count}회 만에 맞췄어요!'

class Quiz12Lotto:
    @staticmethod
    def lotto():
        return random.sample(range(1,46),6)

class Quiz13Bank: # 이름, 입금, 출금만 구현
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def deposit(self, deposit):
        self.account = self.account + deposit
        return f'입금한 금액은{deposit}, 현재 잔액은 {self.account}입니다.'

    def withdraw(self, withdraw):
        self.account = self.account - withdraw
        return f'출금한 금액은{withdraw}, 현재 잔액은 {self.account}입니다.'

class Quiz14Gugudan: # 책받침구구단
    @staticmethod
    def gugudan():
        res = ""
        for i in [2, 6]:
            for j in range(1, 10):
                for k in range(0, 4):
                    res += f'{i + k} * {j} = {(i + k) * j}\t'
                res += '\n'
            res += '\n'
        return res
