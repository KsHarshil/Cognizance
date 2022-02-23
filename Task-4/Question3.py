lists=[]

lists.append(['No.  Name  Marks'])
lists.append([1 , 'Harshil' , 90])
lists.append([2 , 'Harsha '  ,92])
lists.append([3 , 'Sujith '  ,89])
lists.append([4 , 'Jai    '  ,89])


for i in range(len(lists)):
    for j in range(len(lists[i])):
        print(lists[i][j],end="    ")
    print("")
print("")


for n in range(len(lists[2])):
    print(lists[2][n],end="    ")
print("\n")