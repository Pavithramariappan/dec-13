def factorial(number):
    if(number == 0 or number == 1): 
        fact = 1
    else: 
        fact = number * factorial(number - 1) 
    return fact 
  

def find_strong_numbers(list):
    new_list =[] 
  
    for x in list: 
        temp = x 
        sum = 0
        while(temp): 
            rem = temp % 10
            sum += factorial(rem) 
            temp = temp // 10
        if(sum == x): 
            new_list.append(x) 
        else: 
            pass  
              
    return new_list 


val_list=[145, 375, 100, 2, 10, 40585, 0]
strong_num_list=find_strong_numbers(val_list)
print(strong_num_list)
