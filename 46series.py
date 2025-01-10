#Write a program to calculate the sum of the following series till the nth term
#1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
#n will be provided by the user
def fact(n):
    if n==0: return 1
    else: return (n)*fact(n-1)

a= int(input("give me a number: "))
sum=0.0
for i in range (1,a):
    sum = sum + i/fact(i)
print(sum)