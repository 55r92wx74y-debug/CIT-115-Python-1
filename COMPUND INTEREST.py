#kaeliah mighty
#10/12/25
#compund intrerest

#principal investment
PV = float(input("Enter the starting principal: "))
#Interest rate
R = float(input("Enter the annual interest rate: "))
#Number of periods
T = float(input("For how many years will the account earn interest?: "))
#compounding
M = int(input("How many times per year is the interest compunded?: ")) 

#formula

RP = R/100
FV = PV*(1+(RP/M))**(M*T)

print(f"At the end of {T} years you will have $ {FV}")






















              
