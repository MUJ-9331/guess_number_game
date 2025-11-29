import random

n = random.randrange(1, 101)
nd = input("请选择难度：\“简单(1-10次)\” \“中等(1-5次)\” \“困难(1-3次)\”\n")
if nd == "简单":
    max_attempts_attempts = 10
elif nd == "中等":
    max_attempts_attempts = 5
else:
    max_attempts_attempts = 3
a = int(input("请在1到100中猜一个数\n"))
low, high = 1, 100
cs = 1
while a != n and cs < max_attempts_attempts:
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
elif a == n and cs < max_attempts_attempts:
    print(f"猜对了！共用了{cs}次")
else:
    print(f"猜对了！共用了{cs + 1}次")
