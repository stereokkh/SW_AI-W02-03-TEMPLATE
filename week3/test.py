prerequisites = [[1,0],[0,1],[2, 1],[2,0],[2,2],[2,0]]
dict = {i :[] for i in range(len(prerequisites))}
for i, j in prerequisites:
    dict[i].append(j)
print(dict)