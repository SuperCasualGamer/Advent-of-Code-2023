import sys
sys.stdin = open('day1.txt','r')
sys.stdout = open('out.txt','w')

def forwards(line: str) -> str:
    line = line.replace("one","1")
    line = line.replace("two","2")
    line = line.replace("three","3")
    line = line.replace("four","4")
    line = line.replace("five","5")
    line = line.replace("six","6")
    line = line.replace("seven","7")
    line = line.replace("eight","8")
    line = line.replace("nine","9")
    line = line.replace("1ight","18")
    line = line.replace("tw1","21")
    line = line.replace("eigh2", "82")
    line = line.replace("eigh3", "83")
    line = line.replace("7ine","79")
    line = line.replace("nin8","98")
    print(line)
    return line

def backwards(line: str) -> str:
    line = line.replace("en2","12")
    line = line.replace("thgi3","83")
    line = line.replace("thgi5","85")
    line = line.replace("thgi9","89")
    print(line)
    return line

with open('day1.txt', 'r+') as f:
    data = f.readlines()
    answer = []
    for x in data:
        curr = ""
        print(x)
        x = forwards(x)
        x = backwards(x)
        for let in x:
            if let.isdigit() == True:
                curr = let
                let = ""
                print(curr)
                break
        for let in x[::-1]:
            if let.isdigit() == True:
                curr += let
                let = ""
                print(curr)
                break
        if curr == "":
            curr = 0
        print(curr)
        answer.append(int(curr))
    print(sum(answer))
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__