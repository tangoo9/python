print("Hello World!")

# variable
a = 20
bB = 30
c = a+bB
print(c)

# String & Number
my_name = "tang"
age = 32
print("Hello my name is", my_name, "!")
print(age, "years old")

# parameters
user_name = "Tang"
def say_hello(user_name):
    print(user_name, "Hi! how are you?")

def say_bye():
    print("Bye!")

say_hello(user_name)

# default parameters
def say_hello2(user_name2="익명"):
    print(user_name2, "Hi ㅎㅎ! how are you?")

say_hello2()

# 산술 연산자 : +, - , * , / 
#  ** 는 제곱연산
def power(a=0, b=1):
    print(a ** b)

power(100, 2)