#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
last modified: 2018.02.09
"""

# python3 filename.py


# comment

"""
comment
"""

print("Hello" + " Python")
print("Hi, " * 3)

print("Hello %s world" % "Python")
print("Hello %s %d world" % ("Python", 2018))
"""
%s        string
%c        character
%d        integer
%f        floating-point
%o        Octal(8)
%x        Hexadecimal(16)
%%        %
"""

print("Hello%10s" % "Python")
"""output:
Hello    Python
"""

print("Hello {0} world".format("Python"))
print("Hello {0} {1} world".format("Python", 2018))
print("Hello {name} {year} world".format(name="Python", year=2018))

print("{0:=<10}".format("Hello"))
print("{0:=>10}".format("Hello"))
print("{0:=^10}".format("Hello"))
"""output:
Hello=====
=====Hello
==Hello===
"""

print("Hello{0:>10}".format("Python"))
print("{0:<10}Python".format("Hello"))
print("{0:^10}".format("Hello"))
"""output:
Hello    Python
Hello     Python
  Hello
"""

print("{{ s }}".format())
"""output:
{ s }
"""

print(type(2), type("a"), type([]), type(()), type({}))
"""output:
<class 'int'> <class 'str'> <class 'list'> <class 'tuple'> <class 'dict'>
"""

import sys
i = 2
print(sys.getrefcount(2))
j = 2
print(sys.getrefcount(2))
k = 2
print(sys.getrefcount(2))
"""output
115
116
117
"""