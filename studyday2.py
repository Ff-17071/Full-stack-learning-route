name = "Fcs love you "  #字符串
print("大写的字母是",name.upper())
print("小写的字母是",name.lower())
print("需要学习的语言有：\t\nPython\nrust\t\nnodejs\t\npostgreSQL")
print(name.strip())  #去除字符串前后的空格，lstrip()去除左边，rstrip()去除右边

prompt = input("Hi boys, please iput you socre")
user_input = float(prompt) #.strip().lower()  #去除用户输入的前后空格,并且输入的字母转换成小写
if user_input < 60:
    print("you are failrd")
elif 60 <= user_input < 90:
    print("you are success")
else:
    print("you are good")

email = 163
print("my email is fengcs7@" + str(email) + ".com") #字符串拼接，str()函数将数字转换成字符串
