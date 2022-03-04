from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz05Dice, Quiz07RandomChoice, Quiz08Rps, \
    Quiz09GetPrime, Quiz10LeapYear, Quiz11NumberGolf, Quiz12Lotto, Quiz13Bank, Quiz14Gugudan

if __name__ == '__main__':
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
            member = Member()
            q2 = Quiz02Bmi()
            member.name = input('이름: ')
            member.weight = float(input('몸무게(kg): '))
            member.height = float(input('키(cm): '))
            getBmi = q2.getBmi(member)
            res = q2.res(member)
            print(f'{member.name}님의 BMI는 {getBmi:.2f}, {res}입니다.')

        elif menu == '3':
            q3 = Quiz03Grade(input('이름'), int(input('국어점수')), int(input('영어점수')), int(input('수학점수')))
            print(f'이름: {q3.name}\n'
                  f'국어: {q3.kor}점 \n'
                  f'영어: {q3.eng}점 \n'
                  f'수학: {q3.math}점 \n'
                  f'총점: {q3.sum()}점 \n'
                  f'평균: {q3.avg():.2f}점 \n'
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
            q13 = Quiz13Bank(input('이름: '), int(input('초기 금액: ')))
            while 1 :
                choice = input('0.종료 1.잔액 조회 2.입금 3.출금')
                if choice == '0':
                    break
                elif choice == '1':
                    print(q13.account)
                elif choice == '2':
                    print(q13.deposit(int(input('입금 금액: '))))
                elif choice == '3':
                    print(q13.withdraw(int(input('출금 금액: '))))
                else:
                    print('잘못된 입력입니다.')

        elif menu == '14':
            print(Quiz14Gugudan.gugudan())
        else:
            print('잘못 입력하셨습니다.')