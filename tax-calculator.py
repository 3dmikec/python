from decimal import *

tax_rates = {
        'AL':0.04,
        'AK':0.0,
        'AZ':0.056,
        'AR':0.065,
        'CA':0.0725,
        'CO':0.029,
        'CT':0.0635,
        'DE':0.0,
        'DC':0.06,
        'FL':0.06,
        'GA':0.04,
        'HI':0.04,
        'ID':0.06,
        'IL':0.0625,
        'IN':0.07,
        'IA':0.06,
        'KS':0.065,
        'KY':0.06,
        'LA':0.0445,
        'ME':0.055,
        'MD':0.06,
        'MA':0.0625,
        'MI':0.06,
        'MN':0.06875,
        'MS':0.07,
        'MO':0.04225,
        'MT':0.055,
        'NE':0.0685,
        'NV':0.0685,
        'NH':0.0,
        'NJ':0.06625,
        'NM':0.05125,
        'NY':0.04,
        'NC':0.0475,
        'ND':0.05,
        'OH':0.0575,
        'OK':0.045,
        'OR':0.0,
        'PA':0.06,
        'PR':0.115,
        'RI':0.07,
        'SC':0.06,
        'SD':0.045,
        'TN':0.07,
        'TX':0.0625,
        'UT':0.0485,
        'VT':0.06,
        'VA':0.043,
        'WA':0.065,
        'WV':0.06,
        'WI':0.05,
        'WY':0.04
}

def tax_calc():
    
    print('1: Enter two-letter state abbreviation')
    print('2: Enter custom tax rate as a percentage')
    
    while True:
        try:
            choice = int(input('Please select 1 or 2 to continue: '))
            if choice > 2:
                print('Choices are 1 or 2')
                continue
            else:
                break
            break
        except:
            print('Input must be a number')
            continue
    
    while True:
        try:
            cost = float(input('Enter the cost in dollars: '))
            break
        except:
            print('Input must be a number')
            continue
            
    if choice == 1:
        while True:
            tax = str(input('Enter two-letter state abbreviation: '))
            if tax.upper() in tax_rates:
                break
            else:
                print(f'{tax.upper()} was not recognized. Please try again')
                continue
        result_tax = Decimal(cost * tax_rates[tax.upper()])
        result_total = result_tax + Decimal(cost)
        print(f"\nTax rate for {tax.upper()} is {tax_rates[tax.upper()]*100}%")
        print(f"Taxes: ${Decimal(result_tax.quantize(Decimal('.00'), rounding=ROUND_HALF_UP))}")
        print(f"Total Cost: ${Decimal(result_total.quantize(Decimal('.00'), rounding=ROUND_HALF_UP))}")
    
    elif choice == 2:
        while True:
            try:
                tax = float(input('Enter your custom tax rate as a percentage: '))
                tax /= 100
                break
            except:
                print('Input must be a number')
                continue
        result_tax = Decimal(cost * tax)
        result_total = result_tax + Decimal(cost)
        print(f"\nTaxes: ${Decimal(result_tax.quantize(Decimal('.00'), rounding=ROUND_HALF_UP))}")
        print(f"Total Cost: ${Decimal(result_total.quantize(Decimal('.00'), rounding=ROUND_HALF_UP))}")
              
tax_calc()

input('Press ENTER to exit')