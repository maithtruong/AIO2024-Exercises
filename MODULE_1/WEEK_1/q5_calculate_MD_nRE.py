'''
    5. Calculate Mean Difference of n.
'''

import math

def md_nre_single_sample(y, y_hat, n, p):
    if y < 0 or y_hat < 0:
        raise ValueError("y and y_hat must be non-negative.")
    if n <= 0 or p <= 0:
        raise ValueError("n and p must be positive.")

    term_y = y ** (1/n)
    term_y_hat = y_hat ** (1/n)
    md_nre = abs(term_y - term_y_hat) ** p

    return md_nre

def main():
    # Example
    examples = [
        (100, 99.5, 2, 1, 0.025031328369998107),
        (50, 49.5, 2, 1, 0.03544417213033135),
        (20, 19.5, 2, 1, 0.05625552183565574),
        (5.5, 5.0, 2, 1, 0.11029411764705888),
        (1.0, 0.5, 2, 1, 0.29289321881345254),
        (0.6, 0.1, 2, 1, 0.4571067811865475),
    ]
    
    for y, y_hat, n, p, expected in examples:
        result = md_nre_single_sample(y, y_hat, n, p)
        print(f"md_nre_single_sample(y={y}, y_hat={y_hat}, n={n}, p={p}) = {result} (expected: {expected})")

if __name__ == "__main__":
    main()