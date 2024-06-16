'''
    Return the sliding window max of a list.
'''

def max_kernel(num_list, k):
    result = []
    for i in range(len(num_list) - k + 1):
        window_max = max(num_list[i:i + k])
        result.append(window_max)
    return result

def main():
    print(max_kernel([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1], 3))

if __name__ == "__main__":
    main()