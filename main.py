# functions--------------------------------------------------
import random            # for the random choose of phrase
import time               # for the use of epoch time to see how much time game lasted


def win_check(args):      # check if player guessed all the words
    for e in args:
        for y in e:           # loop to go over all the letters
            if y == '_':
                return False    # if there are still blank spots return false
    return True                 # if there are no blank spots return True


def print_board(args):  # showing the current board of the game
    for q in args:
        print(q, end=' ')  # print all the words with spaces between them
    print('\n')
    return None


def insert_letter(guess_map, phrase, letter):   # function for replacing '_' in the game map with the typed letter
    index = 0        # help index for reloading the help_guess_map with every one word at a time
    for q in phrase:    # for to go over all the words in the phrase
        help_str = ''     # reset the help_str for start new string for later
        help_guess_map = guess_map[index]
        if letter in q:    # check if the letter inserted by the player is in the word checked
            for t in range(len(q)):  # if yes then construct the help_str  revealing the letter inserted
                if q[t] == letter:
                    help_str += letter
                else:
                    help_str += help_guess_map[t]
            guess_map[index] = help_str       # after constructing the string, return it to the guess_map
        index += 1                # index up by 1 to go over the next word
    return guess_map               # at the end return the guess_map with the letter revealed


# main code---------------------------------------------------
Words = [['act', 'as', 'if'], ['act', 'without', 'expectation'], ['always', 'be', 'honest'],
         ['always', 'be', 'yourself'], ['ask', 'powerful', 'questions'], ['audit', 'your', 'mistakes'],
         ['be', 'constantly', 'curious'], ['be', 'here', 'now'], ['believe', 'in', 'yourself'],
         ['believe', 'you', 'can'], ['build', 'quality', 'relationships'], ['build', 'strategic', 'partnerships'],
         ['celebrate', 'all', 'success'], ['change', 'is', 'good'], ['commit', 'or', 'quit'], ['do', 'your', 'best'],
         ['dreams', 'come', 'true'], ['embrace', 'constant', 'change'], ['energy', 'draws', 'attention'],
         ['focus', 'and', 'win'], ['friends', 'are', 'treasures'], ['Happiness', 'is', 'Choice'],
         ['Life', 'is', 'awesome']]
Word = ''

Saved_old_games = []   # for saving the old phrases used so they will not choose again
Letter = ''            # the input of the player
All_english_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    Phrase = []       # list to insert the Phrase that randomly choose
    Guess_map = []    # guess map to show the phrase hidden
    Points = 0        # resting the points of the player
    guessed_letters = []   # resting and save the letters guessed by the player
    print('welcome to guess the phrase game :)\n'
          'you need to guess the phrase \n'
          'every correct guess increase your score with 5 points\n'
          'every wrong guess lowers your score with 1 point\n'
          'if you guess the phrase before 30 seconds you will get a bonus of 100 points!!!\n')
    while True:           # while for randomly choose phrase from the words bank
        Index = random.randrange(0, len(Words))    # randomly create index from  0 to max index of the words list.
        if Index not in Saved_old_games:     # check with index if not already used this phrase
            Saved_old_games.append(Index)     # if not add this index to the list of used indexes
            Phrase = Words[Index]           # if not used before load the phrase from the words index chose
            break

    for i in range(len(Phrase)):
        Word = ''
        for k in range(len(Phrase[i])):
            Word += '_'
        Guess_map.append(Word)

    print('Game starts!!! timer starts now...\n')
    time_start = time.time()
    print_board(Guess_map)

    while True:
        while True:
            Letter = str(input('please insert one letter : '))
            Letter = Letter.lower()
            if Letter not in All_english_letters:
                print('try again please insert one english letter')
            else:
                if Letter in guessed_letters:
                    print('already guessed this letter, please try again')
                    print_board(Guess_map)
                else:
                    guessed_letters.append(Letter)
                    break

        Guess_map = (insert_letter(Guess_map, Phrase, Letter))
        print_board(Guess_map)

        words_counter = 0  # for resting the words counter
        for m in Phrase:    # for and if all words checked if contain the letter inserted by the player
            if Letter in m:           # if yes add 5 points
                print('good guess !! added 5 points!')
                Points += 5
                break
            elif words_counter == (len(Phrase)-1):      # if no decrease 1 point
                print('wrong guess -1 points')
                Points -= 1

            words_counter += 1

        if win_check(Guess_map):
            time_won = time.time()
            if (time_won - time_start) < 30:
                Points += 100
                print('greate you finished fast and won a bonus of 100 points!!')
            print('yeah you won!!!!!!!')
            print(f'you have {Points} points!')
            break

    while True:  # while for input if players want replay
        replay = input('wanna replay? y/n : ')
        if replay in ['y', 'n']:
            break
        else:
            print('Type y or n')
        continue
    if replay == 'n':
        break
    elif replay == 'y':
        continue
