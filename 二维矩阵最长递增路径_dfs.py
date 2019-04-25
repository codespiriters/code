# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:57:53 2019
@author: Haiyun Hong
"""
'''
输入：
3
3
7 8 7
6 4 3
1 5 8
输出：
4
'''
def get_matrix():
    rows=int(input())
    cols=int(input())
    matrix=[]
    for i in range(rows):
        arr=list(map(int,input().split()))
        matrix.append(arr)
    return matrix,rows,cols
def dfs(matrix,record,rows,cols,i,j):
    if record[i][j]!=0:
        return record[i][j]
    position=[(0,1),(0,-1),(-1,0),(1,0)]
    res=1
    for pos in position:
        x,y=i+pos[0],j+pos[1]
        print(x,y)
        if x<0 or x>=rows or y<0 or y>=cols or matrix[x][y]<=matrix[i][j]:
            continue
        path=1+dfs(matrix,record,rows,cols,x,y)
        res=max(path,res)
    record[i][j]=res
    return res
def main(matrix,rows,cols):
    max_path=0
    record=[]
    for _ in range (rows):
        record.append([0]*cols)
    for i in range (rows):
        for j in range (cols):
            path=dfs(matrix,record,rows,cols,i,j)
            max_path=max(max_path,path)
            
    return max_path
matrix,rows,cols=get_matrix()
print(main(matrix,rows,cols))