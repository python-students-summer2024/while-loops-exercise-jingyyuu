def get_starting_number():
    is_entered_number_valid = False
    while not is_entered_number_valid:
        starting_number = input("Enter How bottles of beer on the wall?").strip()
        if starting_number.isdigit() and int(starting_number) >= 1:
            is_entered_number_valid = True
    return int(starting_number)

def sing(starting_number_of_beer):
    lyrics = ""
    for i in range(starting_number_of_beer,1,-1):
        if i > 2:
            lyrics = lyrics +f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down, pass it around, {i-1} bottles of beer on the wall.\n\n"
        else:
            lyrics = lyrics +f"{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down, pass it around, {i-1} bottle of beer on the wall.\n\n"

    lyrics = lyrics +"""1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!"""
    print(lyrics) 
    