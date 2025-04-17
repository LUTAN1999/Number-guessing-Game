from random import randint
lower_number=1
higher_number=10
random_numbers:int=randint(lower_number,higher_number)
print(f'Guess the number in the range{lower_number} to {higher_number}')

while True:
        try:
            user_guess: int=int(input('guess : '))
        except ValueError as error:
              print('enter a valid number not a word :) please')
              continue
        if user_guess >random_numbers:
              print('THE NUMBER IS LOWER :( TRY ONE MORE TIME PLEASE!')
        elif user_guess < random_numbers:
              print('the number is a grater number :(')
        else:
              print('Yeahhhhhhhhhhhhh you are correct.')
              break
      
