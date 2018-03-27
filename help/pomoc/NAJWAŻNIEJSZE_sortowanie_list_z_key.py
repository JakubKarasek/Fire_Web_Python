"""xs = ['dddd','a','bb','ccc']
xs.sort(key = len)
xs.reverse()
print(xs)"""


"""xs = [
    ('dddd'),
    ('a'),
    ('asd')
]

xs.sort(key = len)
print(xs)"""

my_list = [
  ["Jarosław", 19],
  ["Euzebiusz", 25],
  ["Zuzanna", 20],
  ["Ala", 13],  
  ["Marek", 23]
]

"""#to działa:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
my_list.sort(key=lambda x: x[0])
print(my_list)"""

"""#toteż ale do pojedynczej listy!!!!!!!!!!!!!!!!
sorted(my_list, key=lambda x: len(x))
print(my_list)
"""

def str_len(x):
    return len(x[0])
my_list.sort(key=str_len)
print(my_list)


#a.sort(key = len)

"""print(my_list
my_list.sort(key = len)
my_list.reverse()
print(my_list)
"""



