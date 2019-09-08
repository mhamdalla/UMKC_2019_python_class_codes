# # employee class code in Python
#initializing the variables
# x =0
# sum_s = 0
# # class definition
# class Employees:
#      def increment(self): #counter for number of employees
#          global x #use the global values so that i can use as many employees as i need
#          x += 1
#      def avg_sal(self):  # function to return the average i can avoid it because i am changing the global variables
#          return sum_s / x
#      def __init__(self, name="", family="", salary="", department=""):
#          global sum_s
#          self.increment()
#          self.name = name
#          self.family = family
#          self.salary = salary
#          self.department = department
#          sum_s += self.salary
#          self. avg_sal()
# class FulltimeEmployee(Employees):
#     def __init__(self, name="", family="", salary="", department=""):
#          Employees.__init__(self, name, family, salary, department)
#
# #main script
# a=Employees("MOhamed", "Hamdalla", 1300, "ECE")
# b=FulltimeEmployee("Khadimul", "Islam", 1000, "ECE")
# print(a.avg_sal())


#numby
# import numpy as np
# x= np.random.randint(1, 20, size=(1,15))
# y= x.reshape((3,5))
# print(y)
# y1=np.max(y, axis=1,keepdims=True)
# print(np.where(y == y1, 0, y))


# import requests
# from bs4 import BeautifulSoup
# html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
# soup = BeautifulSoup(html.content, "html.parser")
# print(soup.title)
# for link in soup.find_all('a'):
#     print(link.get('href'))