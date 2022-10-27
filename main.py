import calendar
import datetime
import heapq
import math
import time
import random


def displayCount():
    print('display total employee %d' % Employee.empCount)


class Employee:
    empCount = 0

    def __init__(self, name, age, number, salary):
        self.salary = salary
        self.name = name
        self.age = age
        self.number = number

        Employee.empCount += 1

    def displayEmployee(self):
        print('name:', self.name, 'age: ', self.age, "number", self.number, 'salary:', self.salary, )


emp1 = Employee('sami', 23, 65656449, 20000)
emp2 = Employee('ahmad', 32, 34004396060, 30000)

emp1.displayEmployee()
emp2.displayEmployee()
print('display total employee %d' % Employee.empCount)

hasattr(emp1, 'age')
getattr(emp1, 'age')
setattr(emp1, 'age', 24)
# delattr(emp1, 'age')
emp1.displayEmployee()
print('Employee__doc__ :', Employee.__doc__)
print('Employee__bases :', Employee.__bases__)
print('Employee__name__ :', Employee.__name__)
print('Employee__module__: ', Employee.__module__)
print("Employee__dict__: ", Employee.__dict__)

print("points")


class Points:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, 'destroyed')


pt1 = Points()
pt2 = pt1
pt3 = pt2
print(id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3

localtime = time.asctime(time.localtime(time.time()))
print('localtime : ', localtime)

cal = calendar.month(1999, 1)
print(cal)

random_set = {'sami', 23, 3.14, 216, (True, False)}
print(random_set)
random_set = {'sami', 23, 216, (True, False)}
print(random_set)
print(len(random_set))
empty_set = set()
print(empty_set)

empty_set.add(1)
print(empty_set)

empty_set.update([2, 3, 4, 5])
print(empty_set)

empty_set.discard(5)
print(empty_set)

empty_set.remove(4)
print(empty_set)

random_set.remove((True, False))
print(random_set)

odd_list = [1, 3, 5, 7, 9, 11]
unorderd_set = {10, 11, 13, 15, 17, 19, 13, 23, 29}
print(unorderd_set)
for num in unorderd_set:
    if not num % 2 == 0:
        odd_list.append(num)

print(odd_list)
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

set_1 = {2, 5, 4, 6, 8, 10}
set_2 = {11, 15, 8, 6, 2}

print(set_1 & set_2)
print(set_1.intersection(set_2))
print(set_2.intersection(set_1))
print(set_1 - set_2)
print(set_A - set_B)

print(set_A.difference(set_B))
print(set_2.difference(set_1))

my_employee_set = {'yasir', 'Saleem', 'haider', 'shani'}
print(my_employee_set)
my_employee_dic = {1: 'yasir', 2: ' Saleem', 3: 'haider', 4: 'sami'}
print(my_employee_dic)
my_employee_tup = 'shani', 'yasir', 'sohaib', 'ahmad', 'ammar'
print(my_employee_tup)
my_employee_lis = ['sami', 'saif', 'ahsan', 'imran']
print(my_employee_lis)

my_employee_list = list(my_employee_tup)
print(my_employee_list)
my_employee_list = list(my_employee_dic.items())
print(my_employee_list)
my_employee_list = list(my_employee_set)
print(my_employee_list)
my_employee_tuple = tuple(my_employee_lis)
print(my_employee_tuple)
# my_employee_dict = dict(my_employee_lis)
# print(my_employee_dict)
my_employee_set1 = set(my_employee_list)
print(my_employee_set1)
my_employee_set1 = set(my_employee_dic)
print(my_employee_set1)
my_employee_tuple = tuple(my_employee_dic)
print(my_employee_tuple)

string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
result = []
for s in string_list:
    if len(s) < 5:
        result.append(len(s))
print(string_list)

date_today = datetime.date.today()
print(date_today)

time_today = datetime.datetime.now()
print(time_today.strftime('%H:%M:%S'))
datetoday = datetime.date.today()
print(datetoday)

fact_of_5 = math.factorial(5)
print(fact_of_5)

gcd = math.gcd(600, 180)
print(gcd)

log100 = math.log(100, 1000)
print(log100)

heap = []
heapq.heappush(heap, 11)
heapq.heappush(heap, 22)
heapq.heappush(heap, 14)
heapq.heappush(heap, 18)
heapq.heappush(heap, 28)
heapq.heappush(heap, 23)

minimum = heapq.heappop(heap)
print(minimum)

rand_num = random.random()
print(rand_num)

rand_num_in_range = random.uniform(20, 60)
print(rand_num_in_range)

random.shuffle(string_list)
print(string_list)

list2 = [1, 2, 23, 4]
print(sum(list2))

try:
    fh = open('testfile', 'w')
    try:
        fh.write('this is ny first exception handling!')
    finally:
        print('going to close this file')
        fh.close()
except IOError:
    print('error can not find file or read data')


class Parent:
    empty = 100

    def __init__(self):
        print('call parent constructor')

    def parentMethod(self):
        print('call parent method')

    def setAttar(self, attar):
        Parent.empty = attar

    def __getAttr__(self):
        print('Parent attribute:', Parent.empty)


class Child(Parent):
    def __init__(self):
        print('calling child constructor')

    def childMethod(self):
        print('call the child method')


c = Child()
c.childMethod()
c.setAttar(200)
c.__getAttr__()
c.parentMethod()


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector (%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(11, 20)
v2 = Vector(15, -9)
print(v1 + v2)
