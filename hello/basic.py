class Quiz30:
    def __init__(self):
        pass

    def quiz20list(self):
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
        print(2*list4)
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

    def quiz21tuple(self):
        a = (1, 2)
        b = (0, (1, 4))
        print(a, type(a), a[0], a + b)

    def quiz22dict(self):
        a = {'class': ['deep learning', 'machine learning'], 'num_students':[40, 20]}
        print(a)
        print(type(a))
        print(a['class'])
        a['grade'] = ['a', 'b', 'c']
        print(a)
        print(list(a.keys()))
        print(list(a.items()))
        print(a.get('class'))
        print('class' in a)

if __name__ == '__main__':
    quiz = Quiz30()
    quiz.quiz22dict()