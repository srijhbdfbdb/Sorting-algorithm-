import random as r
def slection_sort(array):
    for i in range(len(array)):
        min = i 
        for k in range(i+1, len(array)):
            if array[k] < array[min]:
                min = k
        array[i], array[min] = array[min], array[i]
    return array    
def h():
    with open('heloworld', 'r') as f:
        a = f.readlines()
        return a

print(h())   

def quick_sort(array):
    if len(array) <= 1:
        return array
    greater_thanb_pivot = []
    lesser_than_pivot = []
    pivot = array[0]
    for item in array[1:]:
        if item > pivot:
            greater_thanb_pivot.append(item)
        else:
            lesser_than_pivot.append(item)
    return quick_sort(lesser_than_pivot) + [pivot] + quick_sort(greater_thanb_pivot)

""" h= quick_sort([-1,-3,1,100,50])
print(h) """

def binary_search(target, array):
    first = 0
    last = len(array) - 1
    while target !=  array and first < last:
        mid = len(array)//2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            array=array[:mid+1]
            first += 1
        else:
            array = array[mid+1:]
            first += 1
    return False

list1 = [r.randint(10,1000) for i in range(1000)]
sort_list1 = slection_sort(list1)
a = binary_search(100, list1)
print(a)
    
