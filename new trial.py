name = input("What is your name?")
print("hello")
print(name)
first_name="brian"
second_name="kipyegon"
print(first_name)
print(second_name)
#print(first_name+second_name)
#capitalizing the first letter and uppercasing all
print(first_name.capitalize() +" "+ second_name.upper())
#using in to show that something is part of something
if "s" in "geeks":
    print("s part of geeks")
else:print("not part of geeks")
#declaring an array of variables
fruits=["banana","mango","orange"]
x,y,z=fruits
print(x)
print(y)
print(z)
a="awesome"
def myfunc():
    print("python is"+a)
    myfunc()