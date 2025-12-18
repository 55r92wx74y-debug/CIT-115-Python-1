#grade analyzer

name = input("What is your name?: ")
#Asking for the input of the scores
score1 = int(input("Test1: "))
score2 = int(input("Test2: "))
score3 = int(input("Test3: "))
score4 = int(input("Test4: "))


if score1 < 0:
    print("Test scores must be greater than 0.")
    exit()
if score2 < 0:
    print("Test scores must be greater than 0.")
    exit()
if score3 < 0:
    print("Test scores must be greater than 0.")
    exit()
if score4 < 0:
    print("Test scores must be greater than 0.")
    exit()

drop_lowest = input("would you like to drop the lowest grade (Y/N): ")
#checking for the lowest score

lowest = score1

if score2 < lowest:
    lowest = score2
if score3 < lowest:
    lowest = score3
if score4 < lowest:
    lowest = score4


if drop_lowest.upper() == "Y":
    total = score1 + score2 + score3 + score4 - lowest
    average = total/3
elif drop_lowest.upper() == "N":
    print("keeping all scores")
    total = score1 + score2 + score3 + score4
    average = total/4
else:
    print("error you must print Y or N")

#assigning a grade to the letter

if average >= 97:
    letter_grade = "A+"
elif average <= 96.9:
    letter_grade = "A"
elif average <= 93.9:
    letter_grade = "A-"
elif average <= 89.9:
    letter_grade = "B+"
elif average <= 86.9:
    letter_grade = "B"
elif average <= 83.9:
    letter_grade = "B-"
elif average <= 79.9:
    letter_grade = "C+"
elif average <= 76.9:
    letter_grade = "C"
elif average <= 73.9:
    letter_grade = "C-"
elif average <= 69.9:
    letter_grade = "D+"
elif average <= 66.9:
    letter_grade = "D"
elif average <= 63.9:
    letter_grade = "D-"
else:
    letter_grade = "F"


print(f"{name}'s test average is : {average: .1f}")
print(f"letter grade for the test is: {letter_grade}")




    
