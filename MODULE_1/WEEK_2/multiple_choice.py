'''
    Answers to multiple choice questions.
'''
from count_chars import count_chars
from find_lvs_distance import find_lvs_distance
from max_kernel import max_kernel
from return_word_count import return_word_count

# Question 5
def check_the_number(num):
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        list_of_numbers.append(i)
    if num in list_of_numbers:
        results = "True"
    if num not in list_of_numbers:
        results = "False"
    return results    

# Question 6
def find_min_max(data, max, min):
    results = []
    for i in data:
        if i < min:
            results.append(min)
        elif i > max:
            results.append(max)
        else:
            results.append(i)
    return results

def extend_list(x, y):
    x.extend(y)
    return x

def find_min_list(arr):
    min_item = arr[0]
    for item in arr:
        if item < min_item :
            min_item  = item
    return min_item 

def find_max_list(arr):
    max_item = arr[0]
    for item in arr:
        if item > max_item:
            max_item = item
    return max_item

def compare_number(integers, number):
    results = []
    for item in integers:
        if item == number:
            results.append(True)
        else:
            results.append(False)
    return results

def find_average(list_nums = [0, 1, 2]):
    var = 0
    for item in list_nums:
        var += item
    return var / len(list_nums)

def check_if_factor_of_3(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var

def find_factorial(y):
    var = 1
    while(y > 1):
        var *= y
        y -= 1
    return var

def reverse_string(x):
    return x[::-1]

def function_helper(x):
    if x > 0:
        return "T"
    else:
        return "N"
    
def check_state(data):
    res = [function_helper(x) for x in data]
    return res

def is_duplicate(x, data):
    for i in data:
        if x == i:
            return 0
    return 1

def remove_duplicates(data):
    res = []
    for i in data:
        if is_duplicate(i, res):
            res.append(i)
    return res

def main():
    print('Question 1:') # A
    assert max_kernel([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
    num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
    k = 3
    print(max_kernel(num_list , k))
    
    print('Question 2:') # A
    assert count_chars("Baby") == {'B': 1 , 'a': 1 , 'b': 1 , 'y': 1}
    print(count_chars('smiles'))

    print('Question 3:') # C
    file_path = r'MODULE_1\WEEK_2\P1_data.txt' 
    result = return_word_count(file_path)
    assert result['who'] == 3
    print(result['man'])
    
    print('Question 4:') # C
    assert find_lvs_distance("hi", "hello") == 4
    print(find_lvs_distance("hola", "hello"))

    print('Question 5:') # A
    N = 7
    assert check_the_number(N) == "False"
    N = 2
    results = check_the_number(N)
    print(results)

    print('Question 6:') # C
    my_list = [5, 2, 5, 0, 1]
    max_val = 1
    min_val = 0
    assert find_min_max(max=max_val, min=min_val, data=my_list) == [1, 1, 1, 0, 1]
    my_list = [10, 2, 5, 0, 1]
    max_val = 2
    min_val = 1
    print(find_min_max(max=max_val, min=min_val, data=my_list))

    print('Question 7:') # A
    list_num1 = ['a', 2, 5]
    list_num2 = [1, 1]
    list_num3 = [0, 0]
    assert extend_list(list_num1, extend_list(list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]
    list_num1 = [1, 2]
    list_num2 = [3, 4]
    list_num3 = [0, 0]
    print(extend_list(list_num1, extend_list(list_num2, list_num3)))

    print('Question 8:') # C
    my_list = [1, 22, 93, -100]
    assert find_min_list(my_list) == -100
    my_list = [1, 2, 3, -1]
    print(find_min_list(my_list))

    print('Question 9:') # D
    my_list = [1001, 9, 100, 0]
    assert find_max_list(my_list) == 1001
    my_list = [1, 9, 9, 0]
    print(find_max_list(my_list))

    print('Question 10:') # D
    my_list = [1, 2, 3, 4]
    print(compare_number(my_list, 2))
    
    print('Question 11:') # A
    assert find_average([4, 6, 8]) == 6
    print(find_average())
    
    print('Question 12:') # A
    assert check_if_factor_of_3([3 , 9 , 4 , 5]) == [3 , 9]
    print(check_if_factor_of_3([1 , 2 , 3 , 5 , 6]))
    
    print('Question 13:') # C
    assert find_factorial(8) == 40320
    print(find_factorial(4))
    
    print('Question 14:') # B
    x = 'I can do it'
    assert reverse_string(x) == "ti od nac I"
    x = 'apricot'
    print(reverse_string(x))
    
    print('Question 15:') # C
    data = [10 , 0 , -10 , -1]
    assert check_state( data ) == ['T', 'N', 'N', 'N']
    data = [2 , 3 , 5 , -1]
    print(check_state(data))
    
    print('Question 16:') # A
    lst = [10, 10, 9, 7, 7]
    assert remove_duplicates(lst) == [10, 9, 7]
    lst = [9, 9, 8, 1, 1]
    print(remove_duplicates(lst))
        
if __name__ == "__main__":
    main()

