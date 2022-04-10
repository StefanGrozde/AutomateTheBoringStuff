tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(table):
    colWidth = [0] * len(tableData)
    for f in range(len(table)):
        for g in range(len(table)):
            if len(table[f][g]) > colWidth[f]:
                colWidth[f] = len(table[f][g])

    for i in range(len(table)):
        for y in range(len(table[i])):
            print(table[i][y].rjust(colWidth[i]) + ' ' + table[i + 1][y].rjust(colWidth[i + 1]) + ' ' + table[i + 2][y].rjust(colWidth[i + 2]))
        break
printTable(tableData)
    
