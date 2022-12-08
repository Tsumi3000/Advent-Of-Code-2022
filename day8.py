
file = open('input.txt').readlines()
treeVisible = 0
bestSpot = {}
for ligne in range(len(file)):
    for tree in range(len(file[ligne])-1):
        add = {}
        directions = {"up":0,"down":0,"left":0,"right":0}

        for upTree in range(ligne):
            if "up" not in add: directions["up"]+=1
            if file[ligne-1-upTree][tree] >= file[ligne][tree]: add["up"] = True

        for downTree in range(ligne+1, len(file)):
            if "down" not in add: directions["down"]+=1
            if file[downTree][tree] >= file[ligne][tree]: add["down"] = True

        for leftTree in range(tree):
            if "left" not in add: directions["left"]+=1
            if file[ligne][tree-1-leftTree] >= file[ligne][tree]: add["left"] = True

        for rightTree in range(tree+1, len(file[ligne])-1):
            if "right" not in add: directions["right"]+=1
            if file[ligne][rightTree] >= file[ligne][tree]: add["right"] = True
            
        if not ("up" in add and "down" in add and "left" in add and "right" in add): treeVisible+=1
        bestSpot[str(ligne)+str(tree)] = 1
        for i in directions: bestSpot[str(ligne)+str(tree)]*=directions[i]

print(sorted(bestSpot.values())[-1])
print(treeVisible)