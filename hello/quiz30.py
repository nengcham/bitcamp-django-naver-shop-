import random
import string

import pandas as pd
from icecream import ic

from domains import myRandom

'''
ic| df:     A   B   C
        1   1   2   3
        2   4   5   6
        3   7   8   9
        4  10  11  12
'''
class Quiz30:
    def quiz30_df_4_by_3(self) -> str:
        ls = [[j+i for j in range(3)] for i in range(1, 12, 3)]
        col = list(string.ascii_uppercase)[:3]
        df = pd.DataFrame(ls, index=range(1, 5), columns=col)
        # ic(df)
        return None

    '''
    데이터프레임 문제 Q03.
    두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
    ic| df:     0   1   2
            0  97  57  52
            1  56  83  80
    '''
    def quiz31_rand_2_by_3(self) -> str:
        ls = [[myRandom(10, 99) for i in range(3)] for i in range(2)]
        idx = [str(i) for i in range(2)]
        col = [str(i) for i in range(3)]
        df = pd.DataFrame(ls, index=idx, columns=col)
        ic(df)
        return None

    '''
                데이터프레임 문제 Q04.
                국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
                 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

                  ic| df4:        국어  영어  수학  사회
                            lDZid  57  90  55  24
                            Rnvtg  12  66  43  11
                            ljfJt  80  33  89  10
                            ZJaje  31  28  37  34
                            OnhcI  15  28  89  19
                            claDN  69  41  66  74
                            LYawb  65  16  13  20
                            QDBCw  44  32   8  29
                            PZOTP  94  78  79  96
                            GOJKU  62  17  75  49
        '''
    def quiz32_df_grade(self) -> str:
        idx = [''.join(random.choice(string.ascii_letters) for i in range(5)) for i in range(10)]
        ls = [[myRandom(0, 100) for i in range(4)] for i in range(10)]
        col = ['국어', '영어', '수학', '사회']
        df = pd.DataFrame(ls, index=idx, columns=col)
        ic(df)
        return None

    def quiz33(self) -> str: return None

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
