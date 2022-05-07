# Function to return the largest number
def max(a,b,c):

    if (a>b and a>c):

        return a

    elif(b>c):

        return b

    else:

        return c

a=int(input('Enter first number:'))

b=int(input('Enter second number:'))

c=int(input('Enter third number:'))

ans=max(a,b,c)

print('largest of three numbers=', ans)
