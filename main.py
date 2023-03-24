# functions--------------------------------------------------
import random


def print_board(args):  # showing the current board of the game
    for q in args:
        print(q, end=' ')
    print('\n')
    return None


def insert_choosed_letter(guess_map, phrase, letter):
    index = 0
    help_guess_map=''
    for q in phrase:
        help_str = ''
        help_guess_map = guess_map[index]
        if letter in q:
            for t in range(len(q)):
                if q[t] == letter:
                    help_str += letter
                else:
                    help_str += help_guess_map[t]
            guess_map[index] = help_str
        index += 1

    return guess_map


# main code---------------------------------------------------
Words = [['act', 'as', 'if'], ['act', 'without', 'expectation'], ['always', 'be', 'honest'],
         ['always', 'be', 'yourself'], ['ask', 'powerful', 'questions'], ['audit', 'your', 'mistakes'],
         ['be', 'constantly', 'curious'], ['be', 'here', 'now'], ['believe', 'in', 'yourself'],
         ['believe', 'you', 'can'], ['build', 'quality', 'relationships'], ['build', 'strategic', 'partnerships'],
         ['celebrate', 'all', 'success'], ['change', 'is', 'good'], ['commit', 'or', 'quit'], ['do your best'],
         ['dreams', 'come', 'true'], ['embrace', 'constant', 'change'], ['energy', 'draws', 'attention'],
         ['focus', 'and', 'win'], ['Friends', 'are', 'treasures'], ['Happiness', 'is', 'Choice'],
         ['Life', 'is', 'awesome']]
Word = ''
Phrase = []
Guess_map = []
Points = 0
Saved_old_games = []
Letter = ''
All_english_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
words_counter = 0

while True:
    Phrase = []
    Guess_map = []
    Points = 0
    guessed_letters = []
    print('welcome to guess the phrase game :)\n'
          'you need to guess the phrase \n'
          'every correct guess increase your score with 5 points\n'
          'every wrong guess lowers your score with 1 point\n'
          'if you guess the phrase before 30 seconds you will get a bonus of 100 points!!!\n')
    while True:
        Index = random.randrange(0, len(Words))
        if Index not in Saved_old_games:
            Saved_old_games.append(Index)
            Phrase = Words[Index]
            print(Saved_old_games)
            print(Phrase)
            break

    for i in range(len(Phrase)):
        Word = ''
        for k in range(len(Phrase[i])):
            Word += '_'
        Guess_map.append(Word)

    print('Game starts!!! timer starts now...\n')
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
                else:
                    guessed_letters.append(Letter)
                    break

        Guess_map = (insert_choosed_letter(Guess_map, Phrase, Letter))
        print_board(Guess_map)

        words_counter = 0
        for m in Phrase:
            if Letter in m:
                print('yea !! added 5 points!')
                Points += 5
                break
            elif words_counter == (len(Phrase)-1):
                print('wrong guess -1 points')
                Points -= 1

            words_counter += 1
        print(f'you have {Points} points')






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
