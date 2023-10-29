# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:48:08 2023

@author: USER
"""

#Q1 it have O(n)
def matrecies(num_column):
    List1=[int(input('Enter element of the first row:')) for _ in range(num_column)]
    List2=[int(input('Enter element of the second row:')) for _ in range(num_column)]
    return [List1,List2,[List1[col]+List2[col] for col in range(num_column)]]
#This solution have O(n^2)
def matrex(row,column):
    rows=[[int(input(f'Enter element for row{r}:')) for _ in range(column)] for r in range((row))]
    ############
    def sum_List(index):
        Matrix_for_index=[row[index] for row in rows]
        return sum(Matrix_for_index,start=0)
    ##############
    sumation_list=[sum_List( index) for index in range(column)]
    rows.append(sumation_list)
    return rows
print(matrex(2,3))
#Q2 O(n^3) because the max methode have O(n)
def rotateList(rows):
    rotated_list=[[row[index] for row in rows if index<len(row)] for index in range(len(max(rows)))]
    return rotated_list
rows=[[x for x in range(i,i+3)] for i in range(0,12,3)]
print('->',rows,max(rows))
print('->>',rotateList(rows))
#Q3 O(n)
def invertToDict(rows):
    return {f'Class{x}': rows[x] for x in range(len(rows))}
print(invertToDict(rows))
#Q4 O(n^2)
def MatrixToDict():
    task=['firstname','lastname','ID','jobtitle','company']
    employees=[[input(f'{task[i]}{x+1}')if i!=2 else f'{task[i]}{x}' for i in range(len(task))]for x in range(int(input('Enter the rows number:')))]
    return {employee[2]:[employee[x] for x in range(len(employee)) if x !=2] for employee in employees}
print(MatrixToDict())
def palendrom(s)-> bool:
    if len(s)==0:
     return True
    if s[0]==s[len(s)-1]:
        return palendrom(s[1:len(s)-1])
    return False
print(palendrom('racecar'))
def merge(Array,left,right):
    left_size=len(left)
    right_size=len(right)
    i,l,r=0,0,0
    while r<right_size and l<left_size:
        if left[l]<right[r]:
            Array[i]=left[l]
            l+=1 
        else:
            Array[i]=right[r]
            r+=1
        i+=1
    while l<left_size:
        Array[i]=left[l]
        l+=1 
        i+=1
    while r<right_size:
        Array[i]=right[r]
        r+=1
        i+=1
def mergeSort(Array):
    size=len(Array)
    if size<=1:
        return 
    left=Array[:size//2]
    right=Array[len(left):]
    mergeSort(left)
    mergeSort(right)
    merge(Array, left, right)
Array=[3,5,7,8,1,2,3]
mergeSort(Array)
print(Array)
    
    