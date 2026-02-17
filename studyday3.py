#根据要求写一个单独的年龄分类判断
#初步判断，0=<少年<12 12=<青少年<18 18=<青年<40 40=<中年<60 60=<老年<100

userold_input = int(input("请输入你的年龄: ").rstrip())

if userold_input < 12:
    print("您属于少年")
elif 12 <= userold_input < 18:
    print("您属于青少年")
elif 18 <= userold_input < 40:
    print("您属于青年")
elif 40 <= userold_input < 60:
    print("您属于中年")
else:
    print("您属于老年") 