import random

random_words = ['hello','python','world']
hangman = 'hangman'
hangman_count = 7

selected_word = random.choice(random_words)
blanks = list(len(selected_word)*('_'))
blanks_count = len(selected_word)

print("Guess the word")
print(blanks)

while blanks_count > 0 and hangman_count > 0:
    user_char = input("Enter the char")
    inStr = False
    for i in range(len(selected_word)):
        if user_char == selected_word[i]:
            inStr = True
            blanks[i] = user_char
            blanks_count -= 1
    print(blanks)
    if inStr == False:
        hangman_count -= 1
        print(f"you got {hangman_count} chances")
        print(blanks)
        
if blanks_count > 0:
    print("HANGMAN")
if hangman_count > 0:
    print("YOU WIN")
<<<<<<< HEAD
        
=======
        
>>>>>>> 80598e4354e6f32a0fc2efdcf99f7bd931419f9c
