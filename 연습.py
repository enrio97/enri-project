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
