
#user input 
user_input = input("give me a number: ")
num=int(user_input)
input_rev = int(input("give the inverser: "))
#Digits 
#if the number is 4321
a=int(num%10)
num =num//10

b=int(num%10)
num = num//10

c=int(num%10)
num = num//10

d = int(num%10)
num = num//10
rev = 1000*a+100*b+c*10+d
print(rev)
#check 
if rev ==input_rev:
    print("True")
else: print("False")