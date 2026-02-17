name = "Fcs love you "  #字符串
print("大写的字母是",name.upper())
print("小写的字母是",name.lower())
print("需要学习的语言有：\t\nPython\nrust\t\nnodejs\t\npostgreSQL")
print(name.strip())  #去除字符串前后的空格，lstrip()去除左边，rstrip()去除右边

prompt = input("Hi boys, please input you score :")
user_input = float(prompt.strip()) #.strip()去除用户输入的字符串前后空格,.lower()并且输入的字母转换成小写
if user_input < 60:
    print("you failed")
elif 60 <= user_input < 90:
    print("you passed")
else:
    print("you are good")

email = "fengcs7@163.com"
print("my email is ",email) #字符串拼接，str()函数将数字转换成字符串
