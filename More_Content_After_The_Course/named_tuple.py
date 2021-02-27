from collections import namedtuple
color = namedtuple('color',('red','blue','green'))
first_color = color(232,34,95)
second_color = color(red=22,green=23,blue=233)
print(first_color[0])
print(first_color.blue)
print(first_color)
print(second_color)