def factorial_sum( n ):
    total_sum = 0
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
        total_sum += factorial

    return total_sum


n = int(input("请输入一个数："))  # 你可以替换n为你想要计算的上限值
result = factorial_sum(n)
print(f"从1到{n}的阶乘之和为：{result}")


a = int(input("输入一个输作为"))