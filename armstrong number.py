'''
Armstrong means if the value is 153 we need to find out  1*1*1 + 5*5*5 + 3*3*3 =153
if the answer is same after multiply and add then it is an armstrong number
'''
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum +digit ** 3
    temp = temp // 10
if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")


#output - 153 is an armstrong number