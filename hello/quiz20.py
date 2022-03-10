import random
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])

        list2 = ['math', 'english']
        print(list2[0])
        print(list2[0][1])

        list3 = [1, '2', [1, 2, 3]]
        print(list3)

        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)
        list4.append(list5)
        print(list4)
        list4[-2:] = []
        print(list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print(c[0][1])
        c[0][1] = 10
        print(c)

        d = range(10)
        print(d)
        print(sum(d))

        e = [2, 10, 0, -2]
        print(sorted(e))
        print(b.index(0), len(b))
        return None

    def quiz21tuple(self) -> str:
        a = (1, 2)
        b = (0, (1, 4))
        print(a, type(a), a[0], a + b)
        return None

    def quiz22dict(self) -> str:
        a = {'class': ['deep learning', 'machine learning'], 'num_students': [40, 20]}
        print(a)
        print(type(a))
        print(a['class'])
        a['grade'] = ['a', 'b', 'c']
        print(a)
        print(list(a.keys()))
        print(list(a.items()))
        print(a.get('class'))
        print('class' in a)
        return None

    def quiz23listcom(self) -> str:
        print('----- legacy ------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('----- comprehension ------')
        a2 = [i for i in range(5)]
        print(a2)
        print([i*10 for i in range(5)])
        print([i for i in range(5) if i % 2 == 0])
        print([i for i in range(5) if i % 2 == 0 if i % 4 == 0])
        print([i if i % 2 == 0 else 'odd' for i in range(5)])
        print([(i, j) for i in range(2) for j in range(3)])


        return None

    def quiz24zip(self) -> {}:
        # url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        # html_doc = urlopen(url)
        # soup = BeautifulSoup(html_doc, 'lxml') # html.parser vs lxml

        # print(self.crawling(url, 'artist'))
        # self.find_rank(url)

        # cls_names = ['artist', 'title']
        # a = [self.crawling(url, cls_names)]

        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        ls1 = self.crawling(url, 'title')
        ls2 = self.crawling(url, 'artist')
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    def find_rank(self, url) -> None:
        for i in ['title', 'artist']:
            print('\n'.join(f'{i+1}위: {j}' for i, j in enumerate(self.crawling(url, i))))

    @staticmethod
    def crawling(url, cls_nm) -> []:
        soup = BeautifulSoup(urlopen(url), 'lxml')
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text()[1:-1] for i in ls]


    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0 '}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')

        songs = soup.find_all('div', {'class': 'ellipsis rank01'})
        songs = [i.get_text() for i in songs]
        # print(songs)
        songs = [i[1:-1] for i in songs]
        # print(songs)
        songs = songs[:5]

        artists = soup.find_all('span', {'class': 'checkEllipsis'})
        # print(artists)
        artists = [i.get_text() for i in artists]
        # print(artists)
        artists = [i for i in artists]
        artists = artists[:5]

        melon = zip(songs, artists)
        print(list(melon))

        return None

    def quiz28dataframe(self) -> None:

        # dict = self.quiz24zip()
        # df = pd.DataFrame.from_dict(dict, orient='index')
        # print(df)
        # df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')



    def quiz29(self) -> str: return None



