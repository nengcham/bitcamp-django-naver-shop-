import random

from hello.domains import my100, myRandom


class Quiz10:

    def quiz10bubble(self) -> str: return None

    def quiz11insertion(self) -> str: return None

    def quiz12selection(self) -> str: return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str:
        ran_num = myRandom(2, 11)
        res = [[0]*ran_num for i in range(ran_num)]
        count = 1


        return None

    def quiz17prime(self) -> str:
        num = my100()
        res = ""
        for i in range(2, num):
            count = 0
            for j in range(2, i + 1):
                if i % j == 0:
                    count += 1
            if count == 1:
                res += str(i) + "\t"
        print(f'랜덤 숫자: {num}\n숫자 이하의 소수: {res}')
        return None

    def quiz18golf(self) -> str:
        count = 1
        res = ''
        com = my100()
        player = 50
        upNum = 100
        downNum = 0

        while 1:
            if player < com:
                res += str(player)+'\t'
                downNum = player
                player = int((player + upNum) / 2)

                count += 1

            elif player > com:
                res += str(player)+'\t'
                upNum = player
                player = int((player + downNum) / 2)
                count += 1

            elif player == com:
                res += str(player) + '\t'
                print(f'랜덤 숫자: {com}, 도전 숫자: {res}, {count}회 만에 맞췄어요!')
                break

        return None

    def quiz19booking(self) -> str: return None