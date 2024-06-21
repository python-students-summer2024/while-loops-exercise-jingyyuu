def get_starting_number():
    is_entered_number_valid = False
    while not is_entered_number_valid:
        starting_number = input("Enter How bottles of beer on the wall?").strip()
        if starting_number.isdigit() and int(starting_number) >= 1:
            is_entered_number_valid = True
    return int(starting_number)

def sing(starting_number_of_beer):
    lyrics = ""
    current_number = starting_number_of_beer
    is_current_number_greater_than_1 = current_number > 1
    while is_current_number_greater_than_1:
        if current_number > 2:
            lyrics += f"{current_number} bottles of beer on the wall, {current_number} bottles of beer.\nTake one down, pass it around, {current_number-1} bottles of beer on the wall.\n\n"
        else:
            lyrics += f"{current_number} bottles of beer on the wall, {current_number} bottles of beer.\nTake one down, pass it around, {current_number-1} bottle of beer on the wall.\n\n"
        current_number = current_number -1
        is_current_number_greater_than_1 = current_number > 1
        
    lyrics = lyrics +"""1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!"""
    print(lyrics) 