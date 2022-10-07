playerA = ''
playerB = ''

def player(suffix):
    while True:
        name = input("Enter Name, player "+ suffix +" : ")
        res = isinstance(name, str)
        if name:
            break
    return name

playerA = player("A")
playerB = player("B")

movesA = []
movesB = []

move = ''

# Start a loop that will run until the user enters 'quit'.
while move != 'quit':
    move = input("Enter move for " + playerA + " , or 'quit': ")

    if move != 'quit':
        movesA.append(move)
    else:
        break

    move = input("Enter move for " + playerB + " , or 'quit': ")

    if move != 'quit':
        movesB.append(move)

print(movesA)
print(movesB)

# class to encapsulate a single move (word,rack,board position,score)
class Move:
    def __init__(self, word, score):
        self.word = word
        self.score = score

m1 = Move("hex", 26)

print(m1.word)
print(m1.score)
MovesC = []
MovesC.append(m1)

m2 = Move("chalazal", 74)

MovesC.append(m2)

for x in MovesC:
    print(x.word,x.score)
