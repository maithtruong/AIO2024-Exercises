'''
    2. Functions that simulate 3 given activation functions.
'''

import math as m

def is_number(value):
    return isinstance(value, (int, float))

def activation_function(value, function):
    if not is_number(value):
        raise ValueError("Input value must be a number.")
    
    if function == 'sigmoid':
        output = 1 / (1 + m.exp(-value))
        
    elif function == 'relu':
        output = max(0, value)
        
    elif function == 'elu':
        alpha = float(input('Please enter alpha value: '))
        output = alpha * (m.exp(value) - 1) if value <= 0 else value

    else:
        raise ValueError(f'{function} is not supported!')
    
    print(f'{function}({value}): {output}')
    
    return output

def main():
    # Example
    print("Example 1:")
    activation_function(value=3, function='sigmoid')
    print("Example 2:")
    activation_function(value=-2, function='relu')
    print("Example 3:")
    activation_function(value=-1, function='elu')

if __name__ == "__main__":
    main()