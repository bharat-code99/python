
def display_list(game_list):
    print("Current Game List:")
    print(game_list)

def position_choice():
    choice = ''
    while choice not in ['0', '1', '2']:
        choice = input("Choose a position (0, 1 or 2): ")
        if choice not in ['0', '1', '2']:
            print("Please choose a valid position")
    return int(choice)

def replacement_choice(game_list, position):
    user_replacement = input("Enter a value to replace at that position: ")
    game_list[position] = user_replacement
    return game_list

def gameon_choice():
    choice = ''
    while choice not in ['Y', 'N']:
        choice = input("Do you want to continue the game (Y / N): ")
    return True if choice == 'Y' else False

if __name__ == '__main__':
    my_list = [0, 1, 2]
    game_on = True
    while game_on:
        display_list(my_list)
        position = position_choice()
        replacement_choice(my_list, position)
        display_list(my_list)
        game_on = gameon_choice()