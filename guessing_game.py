import random
number = random.randint(0,100)
guessed_numbers = [0]

while True:
    guessed_number = int(input('Guess a number between 1 and 100: '))
    
    if guessed_number == number:
        guessed_numbers.append(guessed_number)
        print(f"You've guessed correctly in {len(guessed_numbers) - 1} tries!")
        break
        
    elif len(guessed_numbers) == 1 and abs(guessed_number - number) <= 10:
        guessed_numbers.append(guessed_number)
        print('WARM!')
        continue
        
    elif len(guessed_numbers) == 1 and abs(guessed_number - number) > 10:
        guessed_numbers.append(guessed_number)
        print('COLD!')
        continue
        
    elif abs(guessed_number - number) < abs(guessed_numbers[-1] - number):
        guessed_numbers.append(guessed_number)
        print('WARMER!')
        continue
        
    elif abs(guessed_number - number) > abs(guessed_numbers[-1] - number):
        guessed_numbers.append(guessed_number)
        print('COLDER!')
        continue
        
    elif guessed_number < 1 or guessed_number > 100:
        guessed_numbers.append(guessed_number)
        print('OUT OF BOUNDS')
        continue