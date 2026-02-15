# if else statement to check odd or even number 
#if n is odd, print weird
#if n is even and in the inclusive range of 2 to 5, print not weird
#n is even and in the inclusive range of 6 to 20, print weird
#n is even and greater than 20, print not weird

n= int(input("Enter a number")) # Remove spaces at the beginning and at the end of the string: 
#The strip() method removes any leading, and trailing whitespaces.

if n%2 !=0:
    print("Weird")

elif n %2==0 and n in range(2,6):
    print("Not Weird")

elif n%2==0 and n in range(6,21):
    print("Weird")

elif n%2==0 and n>20: 
    print("Not Weird")







# # if else statement to check odd or even number 

# n = int(input("Enter a number"))

# if n%2 ==0:
#     print("Even")
# else:
#     print("Odd")

