import random

def main():
    while 1:
        menu = input('0.Exit 1.Calculator 2.BMI 3.Grade 5.주사위 7.랜덤 이름 뽑기'+'\n'
                     '8.가위 바위 보 9.소수 구하기 10.윤년 알아보기 11.골프게임  '
                     '12.로또 13.은행 14. 구구단')
        if menu == '0':
            break

        elif menu == '1':
            q1 = Quiz01Calculator(int(input('첫번째 수')), input('연산자'), int(input('두번째 수')))
            print(f'{q1.num1} {q1.opcode} {q1.num2} = {q1.res()}')

        elif menu == '2':
            q2 = Quiz02Bmi(input('이름'), int(input('몸무게(kg)')), int(input('키(cm)')))
            print(f'{q2.name}님의 BMI는 {q2.bmiCheak()}, {q2.res()}입니다.')

        elif menu == '3':
            q3 = Quiz03Grade(input('이름'), int(input('국어점수')), int(input('영어점수')), int(input('수학점수')))
            print(f'이름: {q3.name}\n'
                  f'국어: {q3.kor}점 \n'
                  f'영어: {q3.eng}점 \n'
                  f'수학: {q3.math}점 \n'
                  f'총점: {q3.sum()}점 \n'
                  f'평균: {q3.avg()}점 \n'
                  f'합격여부: {q3.chkPass()}\n')

        elif menu == '5':
            print(Quiz05Dice.dice())

        elif menu == '6':
            q6 =None

        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(q7.randomMember())

        elif menu == '8':
            q8 = Quiz08Rps(int(input('1.가위 2.바위 3,보')))
            print(f'플레이어: {q8.playerResult}, 컴퓨터: {q8.comResult}, 결과: {q8.rpsRes()}')

        elif menu =='9':
            q9 = Quiz09GetPrime(int(input('100이하의 숫자 입력')))
            print(q9.getPrime())

        elif menu == '10':
            q10 = Quiz10LeapYear(int(input('년도입력')))
            print(q10.leapYear())

        elif menu == '11':
            q11 = Quiz11NumberGolf(int(input('1~100 사이 숫자 입력')))
            print(q11.golf())

        elif menu == '12':
            print(Quiz12Lotto.lotto())

        elif menu == '13':
            q13 = Quiz13Bank

        elif menu == '14':
            q14 = Quiz14Gugudan
        else:
            print('잘못 입력하셨습니다.')

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
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def bmiCheak(self):
        return self.weight * 10000 / self.height / self.height

    def res(self):
        if Quiz02Bmi.bmiCheak() >= 35:
            return '고도비반'
        elif Quiz02Bmi.bmiCheak() >= 30:
            return '중도 비만 (2단계 비만)'
        elif Quiz02Bmi.bmiCheak() >= 25:
            return '경도 비만 (1단계 비만)'
        elif Quiz02Bmi.bmiCheak() >= 23:
            return '과체중'
        elif Quiz02Bmi.bmiCheak() >= 18.5:
            return '정상'
        else:
            return '저체중'

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

class Quiz13Bank:
    def __init__(self, account):
        self.account = account

    def bank(self):
        if self.account > 0:
            res = ''

class Quiz14Gugudan:
    def __init__(self):
        pass


if __name__ == '__main__':
    main()