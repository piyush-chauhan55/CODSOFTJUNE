
# Enter Two Numbers:-

a=int(input("Enter First Number : a = "))
b=int(input("Enter Second Number : b = "))

# some operations:-

sum=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b
exp=a**b

#Enter an operator:-

operator = input(" Enter an operator: +,-,*,/,%,** := ")

if(operator=='+'):
    print("Sum is = " + str(sum))

elif(operator=='-'):
    print("Sub is = " + str(sub))

elif(operator=='*'):
    print("mul is = " + str(mul))

elif(operator=='/'):
    print("div is = "+ str(div))

elif(operator=='%'):
    print("mod is = " + str(mod))

elif(operator=='**'):
    print("exp is = " + str(exp))

else:
    print("Invalid operator")