
# flow control test

while True:
    print()
    print()
    print()
    print('***WELCOME TO SUPER ADVENTURE QUEST***')
    print()
    print('type "start" to start.') # start
    while input() != 'start':
        print('fuck you, type "start"')
    print('hello! traveler, would you like to go on an adventure?')

    if input() == 'yes': # adventure intro
        print('you have been asked by the king to help slay a pesky draygen,')
        print('in return you will be rewarded with one gold shekel.')
        print('do you accept?')
    else:
        print('ok you boring piece of shit, go back to living in squaller with your old stinky balls')
        print('***GAME OVER***') 
            
    if input() == 'yes': # lets go
        print('you inform the king that you are up for the challenge and accept the task.')
        print('you go home to get a good nights rest before setting off on your adventure.')
        print('unfortunately, you die in your sleep.')
        print('RIP adventurer')
        print('***GAME OVER***')
    else:
        print('ok you boring piece of shit, go back to living in squaller with your old stinky balls')
        print('***GAME OVER***')

