import sys
sys.stdin = open('in.txt','r')
sys.stdout = open('out.txt','w')

with open('in.txt', 'r+') as f:
    data = f.readlines()
    og = data
    # print(data)
    answer = []
    for card in data:
        winner = []
        full = []
        card = card[5:]
        # print(card)
        card = card.split()
        gamenum = ""
        for i,num in enumerate(card):
            if ":" in num:
                gamenum = int(num[0:-1]) - 1
            if num == "|":
                winner = card[1:i]
                full = card[i+1:]
        print(gamenum,"GAMENUM")
        #         print(winner)
        #         print(full)
        # print(card)
        count = -1
        for num in full:
            if num in winner:
                count += 1
        print(count,"COUNT")
        if count >= 0:
            answer.append(2 ** count)
            for dupe in range(1,count+2):
                print(gamenum+dupe,"NEW CARD")
                if gamenum + dupe <= 215:
                    print(og[gamenum+dupe])
                    data.append(og[gamenum+dupe])
        else: 
            answer.append(0)
    #     print(count)
    # print(sum(answer))
    print(len(data))
            
sys.stdin = sys.__stdin__
sys.stdout = sys.__stdout__