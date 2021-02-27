from collections import namedtuple
color = namedtuple('color',('red','green','blue'))
first_color = color(232,34,95)
second_color = color(red=22,blue=23,green=233)
print(first_color[0])
print(first_color.blue)
print(first_color)
print(second_color)