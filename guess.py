import random

fk,best=True,20
while fk:
    n = random.randrange(1, 101)
    while True:
        nd = input("请选择难度：1.简单(1-10次)2.中等(1-5次)3.困难(1-3次)\”\n")
        if nd in ["1","2","3"]:
            break
        print("请输入1、2或3进行选择！")
    if nd == "1":
        max_attempts = 10
    elif nd == "2":
        max_attempts = 5
    else:
        max_attempts = 3
    a = int(input("请在1到100中猜一个数\n"))
    low, high = 1, 100
    cs = 1
    while a != n and cs < max_attempts:
        if a < low or a > high:
            a = int(input("不符合游戏规则！请重输\n"))
        elif a < n:
            low = a + 1
            print(f"太小了！\n请在{low}到{high}中猜一个数")
            a = int(input())
            cs += 1
        else:
            high = a - 1
            print(f"太大了！\n请在{low}到{high}中猜一个数")
            a = int(input())
            cs += 1
    if a != n:
        print("挑战失败")
    elif a == n and cs < max_attempts:
        print(f"猜对了！共用了{cs}次")
        if cs < best:
            best = cs
            print(f"最佳成绩：{best}")
    else:
        print(f"猜对了！共用了{cs + 1}次")
        if cs < best:
            best = cs+1
            print(f"最佳成绩：{best}")
    while True:
        t=input("是否继续？\"是\\否\"\n")
        if t in ["是","否"]:
            break
    if t == "否" :
        fk=False
        print("游戏结束，再见")
