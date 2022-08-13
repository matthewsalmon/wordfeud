def player_list(lst):
    chunks = lst.split(',')
#   print(chunks)
    for x in range(len(chunks)):
        print(chunks[x].strip())


