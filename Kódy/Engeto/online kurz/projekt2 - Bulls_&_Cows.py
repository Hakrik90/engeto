import random

oddelovac = '-' * 60
nl = '\n'
hadane_cislo = str(random.randint(1000, 9999))
pokusy = 0


def zadavani_cisla():
    while True:
        print('-' * 60)
        print('Enter a 4-digit number between 1000 and 9999:')
        cislo = input()
        if cislo == 'exit':
            break
        elif cislo.isdigit() is False:
            print("You have to enter numeric characters. Once again. To exit, type 'exit")
        elif cislo[0] == '0':
            print("The number must not start with zero. Once again. To exit, enter 'exit'")
        elif len(cislo) != 4:
            print("The number must be within the interval. Once again. To exit, type 'exit'")
        else:
            break
    return cislo if cislo != 'exit' else print('You quit the game!')


def bull_fnc(tip, hadane_cislo):
    bull = 0
    for i, n in enumerate(hadane_cislo):
        if tip[i] == hadane_cislo[i]:
            bull += 1
    return bull


def crow_fnc(tip, hadane_cislo):
    crow = 0
    for i, n in enumerate(hadane_cislo):
        if n in tip and tip[i] != hadane_cislo[i]:
            crow += 1
    return crow


print('Hello!')
print(oddelovac)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")

while True:
    pokusy += 1
    tip = zadavani_cisla()
    crow = crow_fnc(tip, hadane_cislo)
    bull = bull_fnc(tip, hadane_cislo)
    if bull == 1 and crow == 1:
        print(f"{bull} bull, {crow} crow")
    elif bull == 1:
        print(f"{bull} bull, {crow} crows")
    elif crow == 1:
        print(f"{bull} bulls, {crow} crow")
    elif bull == 4:
        if pokusy == 1:
            print(f"{oddelovac}{nl}Correct, you 've guessed the right number {tip} in {pokusy} guess!!!")
            break
        else:
            print(f"{oddelovac}{nl}Correct, you 've guessed the right number {tip} in {pokusy} guesses!!!")
            break
    else:
        print(f"{bull} bulls, {crow} crows")


if pokusy <= 3:
    print("That was unreal. You're probably telepathic!")
elif 3 < pokusy <= 10:
    print("That was excellent. Good job.")
elif 10 < pokusy <= 20:
    print("Nothing to be ashamed of.Good job.")
elif 20 < pokusy <= 30:
    print("There's room for improvement, but you did it.")
else:
    print("Well, as long as we're all over it.")
