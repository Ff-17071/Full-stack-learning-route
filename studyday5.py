#用于联系深入的联系for和while循环和其他一些概念
#补充一个简单登录验证程序，后续的网页会遇到
user_information = {'fcs7': '2026'}
input_username = input("请输入用户名：").strip()
input_password = input("请输入密码：")
user_input_information = {'input_username': input_username, 'input_password': input_password}#是否可以改善此处代码？
print(user_input_information)
for user_input_information in user_information:
    if user_input_information == user_information:
        print("登录成功!")
    else:
        print("登录失败!")
#初步的验证已经可以实施，后续可以进行完善，比如增加输入次数限制，增加验证码等功能
#user_information后续需要考虑用那种类型的数据结构存储，本次因为只是一个简单的校验，多个用户账号和密码的话，用什么进行验证
#for循环还是if语句？