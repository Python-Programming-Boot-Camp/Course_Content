grade = ["freshman","sophomore","junior","senior"]
print(list(enumerate(grade)))
print(dict(enumerate(grade)))
from enum import Enum, auto
class grade2(Enum):
    freshman = 1
    sophomore = 2
    junior = 3
    senior = auto()
print(grade2.freshman.name)
print(grade2.freshman.value)
print(grade2.senior.value)