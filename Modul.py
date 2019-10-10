
print("Hello, and welcome to Investment Co. where your money is in safe hands!")
startMoney = eval(input("Please enter your starting principal! \n"))
interest = eval(input("Now enter your annual percentage rate, ex. (3% = 0.03) \n"))
print("Great! your percentage rate is " + str(int((interest * 100))) + "%")
for num in range(10):
    startMoney = startMoney * (1+interest)
    print ("In " + str(round(num, 2)) + " years you'll have " + str(round(startMoney, 2)) + "$")