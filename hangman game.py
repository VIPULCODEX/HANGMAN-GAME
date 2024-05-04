import random
from time import sleep

name = "HANGMAN"
by = "VIPUL SHARMA AND CO."
so = "-" * 50
sp = "" * 5
rules = """ YOU HAVE ONLY 5 CHANCES TO GUESS THE WORD AND IF YOU FAIL U WILL LOSE THE GAME.
          YOU WILL GET 50 POINT TO GUESS A CORRECT CHARACTER AND U WILL LOSE 25 POINTS TO GUESS A WRONG CHARACTER.
          SO BE VERY CAREFUL ABOUT YOUR GUESS.
          ............................................ALL THE BEST..........................................."""
print(so + name + so, "\n", so + by + so, "\n", so, "\n")
print("RULES:\n")
print(rules)
print(sp, so)

words = ["ability", "about", "above", "absolute", "accessible", "accommodation",
         "accounting", "beautiful", "bookstore", "calculator", "clever", "engaged",
         "engineer", "enough", "handsome", "refrigerator", "opposite", "socks",
         "interested", "strawberry", "backgammon", "anniversary", "confused",
         "dangerous", "entertainment", "exhausted", "impossible", "overweight",
         "temperature", "vacation", "scissors", "appointment", "decrease",
         "development", "earthquake", "environment", "brand", "necessary", "luggage",
         "impossible", "circumstances", "congratulate", "frequent"]
fword = random.choice(words)
tablov = []
tablov.append("-" * len(fword))
tablo = []
for i in tablov:
    for h in i:
        tablo.append(h)
print("our words has{}letters.".format(len(fword)), ''.join(tablo))
print("" * 7)
c = """_______
 |
 |"""
c1 = "\n  O"
c2 = "\n \|/"
c3 = "\n  |"
c4 = "\n / \."
cson = ""
depo = ""
depo1 = ""
a = len(depo)
can = 5
score = 0
wrongwords = "+/1234567890*-_?.,"
while True:
    if '-' not in tablo:
        print("YOU WON! Word: {} Your Score: {}".format(fword, score))
        print("Please press enter to quit.......")
        break
    if can == 0:
        print("\nYou lose......")
        sleep(0.9)
        print("Your score {}".format(score))
        sleep(0.9)
        print("THE WORD U COULDN'T ANSWER IS: {}".format(fword))
        sleep(0.9)
        print("Please press enter to quit.........")
        break
    x = input("\nPlease enter a letter").lower()
    if len(x) != 1 or x in wrongwords:
        print("\nPlease enter a valid single letter....")
        continue
    if x in depo:
        print("You used this letter before")
        continue
    if x in fword:
        score += 50 * fword.count(x)
        print("Letter {} is counted {} times".format(x, fword.count(x)))
        sleep(0.7)
        for index, i in enumerate(fword):
            if x == i:
                tablo[index] = x
        print("\nWord:", ''.join(tablo))
        sleep(0.7)
    else:
        depo1 += x
        can -= 1
        score -= 25
        print("\nLetter {} not in our word. {} chances left".format(x, can))
        sleep(0.7)
        print("\nWord:", ''.join(tablo))
        sleep(0.7)
        if can == 4:
            cson += str(c)
            print(cson)
        if can == 3:
            cson += str(c1)
            print(cson)
        if can == 2:
            cson += str(c2)
            print(cson)
        if can == 1:
            cson += str(c3)
            print(cson)
        if can == 0:
            cson += str(c4)
            print(cson)

input("Press enter to exit")
