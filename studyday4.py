#本章用于循环的学习（while/for）和模块函数
#将内置的函数重新设置之后，需要重新设置回去，需输入del len

#第一个例子：计算 1 到 100 的和
new_number = 1
sum_number = 0
while new_number <= 100:
    sum_number += new_number
    new_number += 1
print(sum_number)

#第二个例子：输出 0–100 内所有偶数
#从0赋值还是从2开始赋值需要值得思考
even_number = 2
while even_number <= 100:
    print(even_number)
    even_number += 2
print("0-100内的偶数输出完成")

#第三个例子：简易的猜数游戏
counter_input = 0
fixed_number = 44
guess_number = int(input("清楚如你猜测的数据：").strip())
if guess_number == fixed_number:
    counter_input += 1
    print("bingo! 你猜对了,你一共猜了%d次" % counter_input)
else:
    if guess_number > fixed_number:
        counter_input += 1
        print("你猜的数字比正确数字大")
    elif guess_number < fixed_number:
        counter_input += 1
        print("你猜的数字比正确数字小")
    else:
        counter_input += 1
        print("你猜对了,你一共猜了%d次" % counter_input)
