#1
def chat():
    print("예권 : 안녕? 너는 몇살이니?")
    print("인호 : 나? 21살이지!")
    
chat()


#2
def chat(name1, name2, name3):
    print("%s: 안녕? 넌 몇살이니?" % name1)
    print("%s: 나? 나는 25" % name2)
    print("%s: 그렇구나!" % name3)

chat("알렉스", "윤하", "철수") 


#3
def chat(name1, name2, age):
    print("%s: 안녕? 넌 몇살이니?" % name1)
    print("%s: 나? 나는 %d" % (name2, age))


chat("알렉스", "윤하", 10)
chat("철수", "영희", 11)

#4

def chat(name1, name2, age):
    print("%s: 안녕? 넌 몇살이니?" % name1)
    print("%s: 나? 나는 %d살" % (name2, age))


chat("알렉스", "윤하", 10)
chat("철수", "영희", 11)


#5

def dsum(a, b):
    result = a + b
    return result

d = dsum(1,2)
print(d)


#6

def sayhello(name,age):
    if age < 10:
        print("안녕, "+ name)
    elif age <=20 and age >= 10:
        print("안녕하세요, "+ name)
    else:
        print("안녕하십니까,"+ name)

sayhello("주혁", 9)
sayhello("인호", 10)
sayhello("예권", 20)
sayhello("동석", 40)

