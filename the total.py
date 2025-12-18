#calculate the sun of a series

MAX = 5 #Max number of inputs

#intitialize an acommulator variable

total= 0.0

#explain the program
print(f'This program calculates the sun of {MAX} numbers ')

for counter in range(MAX):
    number = int(input('Enter a number '))
    total += number

print(f'The totl=al is {total} ')
