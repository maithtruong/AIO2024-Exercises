'''
    3. Function to choose regression method for loss.
'''
import random as r
import math as m

def calculate_loss(num_samples, loss_name):
    if not str(num_samples).isnumeric():
        print('Number of samples must be an integer number')
        return
    
    num_samples = int(num_samples)
    
    predict_values = [r.uniform(0, 10) for _ in range(num_samples)]
    target_values = [r.uniform(0, 10) for _ in range(num_samples)]
    
    if loss_name == 'MAE':
        loss = sum(abs(p - t) for p, t in zip(predict_values, target_values)) / num_samples
    elif loss_name == 'MSE':
        loss = sum((p - t) ** 2 for p, t in zip(predict_values, target_values)) / num_samples
    elif loss_name == 'RMSE':
        loss = m.sqrt(sum((p - t) ** 2 for p, t in zip(predict_values, target_values)) / num_samples)
    else:
        print('Not a valid loss name!')
        return
    
    print(f'Loss name: {loss_name}')
    for i in range(num_samples):
        print(f'Sample-{i}: Predict = {predict_values[i]:.4f}, Target = {target_values[i]:.4f}')
    print(f'Loss: {loss:.4f}')

def main():
    # Example
    print("Example 1:")
    calculate_loss(num_samples='5', loss_name='MAE')
    print("\nExample 2:")
    calculate_loss(num_samples='5', loss_name='MSE')
    print("\nExample 3:")
    calculate_loss(num_samples='5', loss_name='RMSE')

if __name__ == "__main__":
    main()