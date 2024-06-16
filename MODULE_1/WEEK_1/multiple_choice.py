'''
    Run functions for the multiple choice exercises.
'''

from q1_calculate_metrics import metrics
from q2_activate_functions import activation_function
from q3_calculate_loss import calculate_loss
from q4_approx_functions import cos_approx, sin_approx, sinh_approx, cosh_approx
from q5_calculate_MD_nRE import md_nre_single_sample

# Define extra functions
def calc_ae(y, y_hat):
    return abs(y - y_hat)

def calc_se(y, y_hat):
    return (y - y_hat) ** 2

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
    
# Q1
print(f"Q1, {round(metrics(2, 4, 5), 2)}")

# Q2
print(f"Q2, is_number(1): {is_number(1)}")
print(f"Q2, is_number('n'): {is_number('n')}")

# Q4
print(f"Q4, {round(activation_function(2, 'sigmoid'), 2)}")

# Q5
print(f"Q5, {round(activation_function(-1, 'elu'), 2)}")

# Q6
print(f"Q6, {round(activation_function(3, 'sigmoid'), 2)}")

# Q7
print('Q7 ',calc_ae(2 , 9))

# Q8
print('Q8 ', calc_se(2 , 1))

# Q9
print('Q9', round(cos_approx( x =3.14 , n =10) , 4))

# Q10
print('Q10', round(sin_approx( x =3.14 , n =10) , 4))

# Q11
print('Q11', round(sinh_approx( x =3.14 , n =10) , 2))

# Q12
print('Q12', round(cosh_approx( x =3.14 , n =10) , 2))