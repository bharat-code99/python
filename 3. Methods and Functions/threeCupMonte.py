from random import shuffle

def shuffle_list(mylist):
    print(f"Before Shuffling: {mylist}")
    print("Shuffling...")
    shuffle(mylist)

def user_guess():
    input_guess = ''
    while input_guess not in ['0', '1', '2']:
        input_guess = input("Pick a guess 0, 1 or 2: ")
    return int(input_guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("You Win!")
    else:
        print("Wrong Guess!")
        print(mylist)

my_list = [' ', 'O', ' ']
shuffle_list(my_list)
guess = user_guess()
check_guess(my_list, guess)