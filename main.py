# functions--------------------------------------------------
import random


def print_board(args):  # showind the current board of the game
    for q in args:
        print(q, end=' ')
    print('\n')
    return None


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
All_english_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    Phrase = []
    Guess_map = []
    Points = 0
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

    print_board(Guess_map)

    while True:
        while True:
            Letter = str(input('please insert one letter : '))
            if Letter not in All_english_letters:
                print('try again please insert one english letter')
            elif Letter in Guess_map:
                print('already guessed this word, please try again')


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
