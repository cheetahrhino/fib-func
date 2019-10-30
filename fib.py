# A Fibonacci sequence is a  sequence of numbers where each successive number is the sum of the previous two.
# The classic Fibonacci sequence begins 1, 1, 2, 3, 5, 8, 13,....
# Write a program that computes the nth Fibonacci number where the n is a value input by the user

def fibCalc(num):

    a,b = 1,1

    num_int = int(num-2)
    
    for i in range(num_int):
        nth = a + b
        a = b
        b = nth
    return b

def main():
    print("This is a program that computes the nth Fibonacci number where the n is a value input by the user\n")

    num = int(input("Please input what Fibonacci number you want to be calculated: "))

    print("The {0}th Fibonacci number is {1}.".format(num,fibCalc(num)))

main()