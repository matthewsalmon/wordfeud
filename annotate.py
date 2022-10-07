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
