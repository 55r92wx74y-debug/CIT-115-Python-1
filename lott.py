#this displays property tax

TAX_FACTOR = 0.0065

print('Put in the lot number for house ')
lot = int(input('Lot Number '))

while lot != 0:
    value = float(input('Value of house '))
#calculate property rax
    tax = value * TAX_FACTOR

#display tax
    print(f'Property tax $ {tax:,.2f}')

    print('Enter the next lot number ')

    print('Enter the next lot number or press 0 to end program')

    lot = int(input('Lot number '))
