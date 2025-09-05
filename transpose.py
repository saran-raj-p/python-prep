m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
m3 =[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(m1)):
    for j in range(i+1,len(m1[0])):
        temp = m1[i][j]
        m1[i][j] = m1[j][i]
        m1[j][i] = temp


print(m1)
