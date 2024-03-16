import random
import hangman_art
import hangman_words

#Logo for the game
print(hangman_art.logo)


#Step 1 generating the words
list_base = hangman_words.word_list
string_random = random.choice(list_base)
print(string_random)
list_result = list(string_random)
print(f'Pssst, the solution is {string_random}.')


#second generate the blanks as many of the word length is 
blank_string = ""
for n in range(0, len(list_result)):
    blank_string += "_"
print(blank_string)
list_blank = list(blank_string)

#third step lets ask the user to guess the letter
end_of_game = False
end_of_lives = False
num_lives = 6
while not end_of_game:
    
    string_user = input("Give us the letter\n").lower()
    
    for words in list_blank:
        if words == string_user:
            print(f"you have already guessed the letter {string_user}.")

    for l in range(len(list_result)):
       # print(f"Current position: {l}\n Current letter: {list_result[l]}\n Guessed letter: {string_user}")
        if(list_result[l] == string_user):
            list_blank[l] = string_user

    if string_user not in string_random:
        print(f"You have choosed the wrong letter {string_user} so you lose on life")
        num_lives -= 1
        if num_lives == 0:
            end_of_lives = True
            print("Game over you are dead")
    
    print(list_blank)
   
    
    if "_" not in list_blank:
        end_of_game = True
        print("You win")

     
    print(hangman_art.stages[num_lives])
