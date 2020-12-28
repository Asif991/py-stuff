word = 'secret'

guesses = ''

turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print('-')
            failed+=1
    if failed == 0:
        print('You win')
        print('The word is: ', word)
        break

    guess = input("guess a character:")

    guesses += guess 
     
    if guess not in word:
         
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more attempts...')
         
        if turns == 0:
            print("You Loose")