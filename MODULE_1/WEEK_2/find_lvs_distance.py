'''
    Find minimum edit distance Levenshtein from given 2 words.
'''
import numpy as np

def find_lvs_distance(source, target):
    n = len(source)
    m = len(target)
    
    distance_matrix = np.zeros((n + 1, m + 1))
    
    for i in range(1, n + 1):
        distance_matrix[i, 0] = i
    for j in range(1, m + 1):
        distance_matrix[0, j] = j
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if source[i - 1] == target[j - 1] else 1
            distance_matrix[i, j] = min(
                distance_matrix[i - 1, j] + 1,
                distance_matrix[i, j - 1] + 1,
                distance_matrix[i - 1, j - 1] + cost
            )
    
    return distance_matrix[n, m]

def main():
    source = 'honda'
    target = 'london'
    result_distance = find_lvs_distance(source, target)
    print(result_distance)


if __name__ == "__main__":
    main()