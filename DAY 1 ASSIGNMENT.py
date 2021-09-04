"""#DAY 1 ASSIGNMENT

###1. add two number
"""

print("ENTER FIRST NUMBER:")
a = int(input())
print("ENTER SECOND NUMBER")
b=int(input())
c = a+b
print("BY ADDING TWO NUMBERS =",c)

"""###2. Try to add integer with string and see the output"""

a = 'python'
b=5
c=a+str(b)
print("adding string and integer = ",c)

"""###3. Print variable and strings in one line with the help of f string"""

print(f"27abc\n")
name = "abc"
code = "x!$"
age = 27
print("Hello, {2}. Your code is  {1}  and you are {0} years old\n".format(age,code, name))

"""###4. How to add space and new line in the print statement"""

print("hello world 1 \n")
print("hello world 2 \n")
print(f"Hello\nWorld!\n")
a ="hi"
b = "there !"
print(a,"  ",b)
