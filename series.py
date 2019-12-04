def sum_series(n, a = 0 , b = 1):
    if n == 0:
        return a
    if n == 1:
        return b   
    current_num = b
    previous_num = a

    for i in range(2 , n):
        i = i
        new_num = current_num + previous_num
        previous_num = current_num
        current_num = new_num
    return current_num + previous_num
print(sum_series(4,4,3))

def fibonacci(n):
    if n < 2:
        return n
    
    current_num = 0
    previous_num = 0
    for i in range(n):
        if i < 2:
            current_num = i
        else:
            new_num = current_num + previous_num
            previous_num = current_num
            current_num = new_num
    return current_num + previous_num        
fibonacci(12)

def lucas(n):
    if n < 2:
        return 2 - n
    
    current_num = 1
    previous_num = 2

    for i in range(n):
        if i < 2:
            current_num = 2 - i
        else:
            new_num = current_num + previous_num
            previous_num = current_num
            current_num = new_num
    return current_num + previous_num
print(lucas(0))