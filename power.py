num = int(input("Enter a number: "))

power_num = int(input("Enter the power of the number: "))

res = 1

for i in range(power_num):
    res = res*num
print("The %d power of given number is: %d" %(power_num, res))