#amicable numbers:Two numbers are said to be amicable
#if the sum of proper divisors  of one number  plus  1,  is equal to the other number.
#All divisors  of a number other than 1 and itself,   are called proper divisors.
#For example, the numbers 220 and 284 are amicable as the
#sum of proper divisors of 220 (i.e.) 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110 is equal to 284
#and sum of proper divisors of 284 (i.e.) 1, 2, 4, 71 and 142 is 220.
def isAmicable(n1,n2):
    sum1=0;
    sum2=0;
    for i in range(1,n1):
        if n1%i == 0:
            sum1 = sum1+i
    for i in range(1,n2):
        if n2%i == 0:
            sum2 = sum2+i
    if sum1 == n2 and sum2 == n1:
        print("amicable number")
    else :
        print("not amicable number")

n1=int(input("Enter number1"))
n2=int(input("enter number2"))
isAmicable(n1,n2)
