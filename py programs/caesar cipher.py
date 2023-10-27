alphabets = list('abcdefghijklmnopqrstuvwxyz')

def caeser(user_input,steps,direction):
    output = ""
    direction.lower()
    if direction == 'd':
        steps *= -1
    for char in user_input:
        if char in alphabets:
            position = alphabets.index(char) + steps
            position %= 26
            output += alphabets[position]
    print(output)

isTrue = True
while isTrue:
    user_input = input("Enter the string ")
    steps = int(input("Enter the number of steps "))
    steps = steps % 26
    direction = input("What do you want to do? (e - encrypt | d - decrypt) ")
    caeser(user_input,steps,direction)

    user_choice = input("Do you want to continue? y - yes | n - no ")
    user_choice.lower()
    if user_choice == 'n':
        isTrue = False





