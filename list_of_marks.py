list_of_marks=(12,18,25,24,2,5,18,20,20,21)
def merge_sort(list_of_marks):
    if len(list_of_marks) <= 1:
        return list_of_marks
    mid = len(list_of_marks)//2
    right = list_of_marks[mid:]
    left = list_of_marks[:mid]
    right = merge_sort(right)
    left = merge_sort(left)
    return list(merge(right, left))
    
def merge(right, left):
    res = []
    while len(right) != 0 and len(left) != 0 :
        if right[0] > left[0]:
            res.append(left[0])
            left.remove(left[0])
        else :
            res.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        res = res + right
    else:
        res = res + left
    return res
mylist=list(list_of_marks)
def find_more_than_average():
    sum_num = 0
    length = 0
    for mark in list_of_marks:
        sum_num += mark
        length += 1
    avg = sum_num/length
    count = 0
    for i in range(length):
        if list_of_marks[i] > avg:
            count += 1
    return ((count/length)*100)

    for i in range(len(mylist)):
        if(mylist[i]<=25):
            if(mylist[i]>12):
               print(mylist[i])
               a=mylist.count(i)
               print(a)
               print((a/length)*100)
print(find_more_than_average())            
            

def generate_frequency():
    l= []
    list_of_mark = list(list_of_marks)
    for mark in range(26):
        count = 0
        for marks in list_of_mark:
            if marks == mark:
                count += 1
        l.append(count)
    return (l)

print(generate_frequency())    
mylist=[12,18,25,24,2,5,18,20,20,21]

def sort_marks():
    global list_of_marks
    list_of_mark = list(list_of_marks)       
    return(merge_sort(list_of_mark))
print(sort_marks())
