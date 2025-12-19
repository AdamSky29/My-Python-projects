import random

znaki = ["🍒", "🍋", "🔔", "🍀", "💎"]

while True:
    krecenie = int(input("Czy chcesz zakręcić? (1=tak, 2=nie): "))
    if krecenie == 1:
        los1 = random.randint(0, 4)
        los2 = random.randint(0, 4)
        los3 = random.randint(0, 4)
        print("********************")
        print(" |     KASYNO!    |   ")  
        print("********************")
        print(f"  {znaki[los1]}  |  {znaki[los2]}  |  {znaki[los3]}  ")
        print("********************")
        if los1 == los2 == los3:
            print("***** WYGRAŁEŚ! *****")
        else:
            print("*** PRZEGRAŁEŚ! ***")
        print("********************")
    elif krecenie == 2:
        print("Koniec gry.")
        break
    else:
        print("Nieznana opcja, spróbuj ponownie.")
