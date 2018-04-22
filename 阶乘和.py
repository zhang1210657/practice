#阶乘和
#题目：输入一整数x，请计算1!+2!+3!+...+x!（假设x>3）

x = int(input('请输入一个整数：'))
result = 0
for i in range(1,x+1):


    tp = 1
    for j in range(1,i+1):
        tp *= j


    result += tp


print(result)
