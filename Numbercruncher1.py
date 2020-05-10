def Addition(numList):
    number_of_entries=len(numList)
    Addition=0
    for x in numList:
        Addition=float(Addition)+float(x)
    return(Addition)

def Subtraction(numList):
    number_of_entries=len(numList)
    Subtraction=numList[0]
    del numList[0]
    for x in numList:
        Subtraction=float(Subtraction)-float(x)
    return(Subtraction)

def Multiplication(numList):
    number_of_entries=len(numList)
    Multiplication=numList[0]
    del numList[0]
    for x in numList:
        Multiplication=float(Multiplication)*float(x)
    return(Multiplication)

def Division(numList):
    number_of_entries=len(numList)
    Division=numList[0]
    del numList[0]
    for x in numList:
        Division=float(Division)/float(x)
    return(Division)
    

print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

User_choice=input("Select your choise: ")

n = int(input("Enter how many numbers that you want to calculate : "))
numList = list(float(num) for num in input("Enter the list numbers separated by space: ").strip().split())[:n]

if User_choice=='1':
    answer = Addition(numList)
    print("The answer is: ",answer)

elif User_choice=='2':
    answer = Subtraction(numList)
    print("The answer is: ",answer)

elif User_choice=='3':
    answer = Multiplication(numList)
    print("The answer is: ",answer)

elif User_choice=='4':
    answer = Division(numList)
    print("The answer is: ",answer)



    
