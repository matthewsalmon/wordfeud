# split the player list from the wloh email so that it can be pasted into a spreadsheet (column)
def player_list(lst):
    chunks = lst.split(',')
#   print(chunks)
    for x in range(len(chunks)):
        print(chunks[x].strip())


# split the player list from the wloh email so that it can be pasted into a spreadsheet (column)
def player_list_set(lst):

    chunks = lst.split(',')
    mylist = []

    for x in range(len(chunks)):
        name = chunks[x].strip()
        mylist.append(name)

    return mylist
