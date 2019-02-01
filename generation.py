import random
special_number = random.randint(0, 100)
exit = False

while exit != True:
    user_input = 0
    try:
        user_input = int(input("Gib bitte eine Zahl ein: "))
    except:
        print("Bitte nur Zahlen eingeben!")
        break
    if user_input <= 100 and user_input >= 1:
        procent = (user_input/special_number)*100 # Prozent angabe vom Kuchen
        if procent <= 50:
            print("Du bist weit weg, rate viel höher")
        elif procent <= 75:
            print("Du bist in der näher, aber du musst höher raten")
        elif procent <= 85:
            print("Fast, aber du musst höher raten")
        elif procent <= 95:
            print("Du bist ganz nah dran")
        elif procent <= 98:
            print("Du bist so nah dran, dass es anfängt heiß zu werden, rate höher")
        elif procent == 100:
            print("Du hast die Zahl richtig erraten")
        elif procent <= 105:
            print("Fast geschaft, rate niedrieger")
        elif procent <= 120:
            print("Du bist in der näher, aber du musst tiefer raten")
        elif procent <= 150:
            print("Wow du bist so weit weg, rate niedrieger")
        # Hier schreibe ich die bedingungen
    else:
        print("Auf Wiedersehen")
        exit = True
