# split the player list from the wloh email so that it can be pasted into a spreadsheet (column)
def player_list(lst):
    chunks = lst.split(',')
#   print(chunks)
    for x in range(len(chunks)):
        print(chunks[x].strip())


