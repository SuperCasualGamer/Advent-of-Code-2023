import sys
from collections import defaultdict
sys.stdin = open('in.txt','r')
sys.stdout = open('out.txt','w')
def power(current:dict, new:dict):
    #Sees if the difference in new set was greater than previous sets and adds it to current
    for key in current.keys():
        if new[key] > current[key]:
            current[key] = new[key]
    return current


with open('in.txt', 'r+') as f:
    data = f.readlines()
    answer = []
    for game in data:
        state = True
        gamenum = ""
        print(game,"NEW GAME")
        for i,x in enumerate(game):
            if x == ":":
                game = game[i:]
                game = game.strip("\n")
                break
            else:
                gamenum += x
        balls = {"b":0,"r":0,"g":0}
        most = {"b":0,"g":0,"r":0}
        curr = ""
        for i,let in enumerate(game):
            print(let)
            print(game)
            if let.isdigit() is True:
                curr += let
                print(curr,"val")
            elif let.isdigit() == False:
                if let == "b":
                    balls["b"] += int(curr)
                    curr = ""
                    most = power(most, balls)
                    print(most,"MOST")
                if let == "r":
                    balls["r"] += int(curr)
                    curr = ""
                    most = power(most, balls)
                    print(most,"MOST")
                if let == "g":
                    balls["g"] += int(curr)
                    curr = ""
                    most = power(most, balls)
                    print(most,"MOST")
                if let == ";":
                    most = power(most, balls)
                    print(most,"MOST")
                    balls = {"b":0,"r":0,"g":0}
                    game = game[i:]
        if state:
                curr = 1
                for key in most.keys():
                    if most[key] != 0:
                        print(most)
                        print(most[key],"VAL")
                        print(curr,"CURR")
                        curr = curr * most[key]
                        print(curr,"NEW")
                answer.append(curr)
                print(curr,"CURR")
    print(answer)
    print(sum(answer))


sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__