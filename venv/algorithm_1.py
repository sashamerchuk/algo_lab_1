import time

def selection_sort(list_restaurants):
    print("===========")
    print("Selection Sort")
    start_time = time.time()
    comparison_counter=0
    swap_counter=0
    arr=[]
    for o in range(len(list_restaurants)):
        arr.append(list_restaurants[o].num_of_tables)
    for i in range(len(arr)):
        min_index = i
        comparison_counter+=1
        swap_counter+=1
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    print("Time of execution: %f s" % (time.time() - start_time))
    print("Comparison was made %d times" % comparison_counter)
    print("Swap was made %d times" % swap_counter)
    print(arr)


def mergeSort(list_restaurants):
    start_time = time.time()
    comparison_counter=0
    swap_counter=0
    if len(list_restaurants)>1:
        mid=len(list_restaurants)//2
        left=list_restaurants[:mid]
        right=list_restaurants[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0;
        while i < len(left) and j < len(right):
            if left[i].num_of_dishes<=right[j].num_of_dishes:
                list_restaurants[k]=left[i]
                i +=1
                comparison_counter += 1
                swap_counter += 1
            else:
                list_restaurants[k]=right[j]
                j+=1
            k+=1
        while i <len(left):
            list_restaurants[k]=left[i]
            i+=1
            k+=1
            comparison_counter += 1
            swap_counter += 1
        while j < len(right):
            list_restaurants[k]=right[j]
            j+=1
            k+=1
            comparison_counter += 1
            swap_counter += 1
    print("Merge Sort")
    print("Time of execution: %f s" % (time.time() - start_time))
    print("Comparison was made %d times" % comparison_counter)
    print("Swap was made %d times" % swap_counter)
    for i in range(len(list_restaurants)):
        arr = [list_restaurants[i].num_of_dishes]
        print(arr)


