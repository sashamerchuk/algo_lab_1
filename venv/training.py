import random
a=[1,2,68,2,3,5]
b=[21,23,68,24,31,5]
c=[121,233,648,254,311,54]
q = [32,48,356,54,67,76]
z=[983,234,765,4321,342,23,12]
import time
def bubble_sort(arr):
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(a)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped=True
bubble_sort(a)
print("bubble sort",a)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j]> arr[min_index]:
                min_index=j
        arr[i],arr[min_index], = arr[min_index],arr[i]
selection_sort(a)
print("selection sort",a)

def insertion_sort(arr):
    for i in range(1,len(arr)):
        item_to_insert=arr[i]
        j=i-1

        while j>=0 and arr[j]<item_to_insert:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=item_to_insert
insertion_sort(b)
print("insertion sort",b)

def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0;
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i <len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j <len(right):
            arr[k]=right[j]
            j+=1
            k+=1
merge_sort(c)
print("merge sort",c)

def partition(arr,low,high):
    pivot = arr[(low+high)//2]
    i=low-1
    j=high+1
    while True:
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]
def quick_sort(arr):
    def _quick_sort(items,low,high):
        if low<high:
            split_index=partition(items,low,high)
            _quick_sort(items,low,split_index)
            _quick_sort(items,split_index+1,high)
    _quick_sort(arr,0,len(arr)-1)
quick_sort(q)
print("quick sort",q)

def heapify(nums,heap_size,root_index):
    # Предположим, что индекс самого большого элемента является корневым индексом

    largest=root_index
    left_child=(2*root_index)+1
    right_child=(2*root_index)+2

    # Если левый потомок корня является допустимым индексом, а элемент больше
    # чем текущий самый большой элемент, то обновляем самый большой элемент
    if left_child < heap_size and nums[left_child]>nums[largest]:
        largest=left_child
    if right_child<heap_size and nums[right_child]>nums[largest]:
        largest=right_child
    # Если самый большой элемент больше не является корневым элементом, меняем их местами
    if largest !=root_index:
        nums[root_index],nums[largest]=nums[largest],nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums,heap_size,largest)
def heap_sort(nums):
    n = len(nums)
    # Создаем Max Heap из списка
    # Второй аргумент означает, что мы останавливаемся на элементе перед -1, то есть на первом элементе списка.
    # Третий аргумент означает, что мы повторяем в обратном направлении, уменьшая количество i на 1
    for i in range(n,-1,-1):
        heapify(nums,n,i)
    # Перемещаем корень max hea в конец
    for i in range(n-1,0,-1):
        nums[i],nums[0]= nums[0],nums[i]
        heapify(nums,i,0)
heap_sort(z)
print("heap sort",z)


def partition(arr,low,high):
    pivot = arr[(low+high)//2]
    i=low-1
    j=high+1
    while True:
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]
def quick_sort(arr):
    def _quick_sort(items,low,high):
        if low<high:
            split_index=partition(items,low,high)
            _quick_sort(items,low,split_index)
            _quick_sort(items,split_index+1,high)
    _quick_sort(arr,0,len(arr)-1)
quick_sort(q)
print("quick sort",q)

def selection_sort1(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
selection_sort1(z)
print(z)
