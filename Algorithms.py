# from main import *

def bubble_sort(list,Rectangle):

    for i in  range(0,len(list)-1):
        Sorted = False
        for j in  range(0,len(list)-1-i):
            if list[j] > list[j+1]:
                store=list[j+1]
                list[j+1]=list[j]
                list[j]=store
                Sorted = True
                
                Rectangle(list )






def merge_sort(list,Rectangle):

    if len(list) > 1:
        left = list[:len(list) // 2]
        right = list[len(list)//2:]
        merge_sort(left,Rectangle)
        merge_sort(right,Rectangle)
        

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i=i+1
                k=k+1
            else:
                list[k]=right[j]
                j=j+1
                k=k+1
        

        while i < len(left) :
            list[k] = left[i]
            k=k+1
            i=i+1
        while j < len(right) :
            list[k] = right[j]
            k=k+1
            j=j+1

        Rectangle(list )





def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(list, start, end,Rectangle):
    if start < end:
        pi = partition(list, start, end)
        quick_sort(list, start, pi-1,Rectangle)
        quick_sort(list, pi+1, end,Rectangle)
        Rectangle(list )

def partition(list, start, end):
    pivot_index = start
    pivot = list[pivot_index]

    while start < end:
        while start < len(list) and list[start] <= pivot:
            start+=1

        while list[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, list)

    swap(pivot_index, end, list)

    return end
