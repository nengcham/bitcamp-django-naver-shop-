import random

from hello.domains import my100, Member, myRandom, memberlist, myMember


class Quiz00:

    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        o = ['+', '-', '*', '/', '%']
        ran_o = o[myRandom(0, 5)]
        if ran_o == '+': res = a + b
        elif ran_o == '-': res = a - b
        elif ran_o == '*': res = a * b
        elif ran_o == '/': res = a / b
        elif ran_o == '%': res = a % b

        print(f'{a} {ran_o} {b} = {res}')

        return None

    def quiz01bmi(self):
        this = Member()
        this.weight = 78.8
        this.height = 178.8
        getBmi = this.weight * 10000 / this.height / this.height
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
        print(f'{myMember()}님의 BMI는 {getBmi:.2f}, {res}입니다.')
        return None

    def quiz02dice(self):
        print(myRandom(1, 6))
        return None

    def quiz03rps(self):
        p = myRandom(0, 2)
        c = myRandom(0, 2)
        rps = ['가위', '바위', '보']
        res = 'Lose' if (p + 1) % 3 == c else 'Draw' if p == c else 'Win'
        print(f'플레이어: {rps[p]}, 컴퓨터: {rps[c]}, 결과: {res}')
        return None

    def quiz04leap(self):
        y = myRandom(1, 2500)
        leap = '윤년 입니다.' if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else '평년 입니다.'
        print(f'{y}년은 {leap}')
        return None

    def quiz05grade(self):
        kor = myRandom(0, 100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        sum = kor + eng + math
        avg = sum / 3
        res = '합격' if avg >= 60 else '불합격'
        print(f'국어: {kor}, 영어: {eng}, 수학: {math}, 평균: {avg:.2f}, 결과: {res}')

    def quiz06memberChoice(self):
        print(myMember())
        return None

    def quiz07lotto(self):
        print(sorted(random.sample(range(1, 46), 6)))
        return None

    def quiz08bank(self):
        name = '최건일'
        account = myRandom(100, 30000)
        deposit = myRandom(100, 30000)
        withdraw = myRandom(100, 30000)

        print(f'{name}님의 잔액{account}원 입니다.')
        return None

    def quiz09gugudan(self):  # 책받침구구단
        res = ""
        for i in [2, 6]:
            for j in range(1, 10):
                for k in range(0, 4):
                    res += f'{i + k} * {j} = {(i + k) * j}\t'
                res += '\n'
            res += '\n'
        print(res)
        return None

