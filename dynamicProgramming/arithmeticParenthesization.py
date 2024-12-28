def arithmetic_max_value_recursive(numbers, operators, memo, start, end):
    # Base case: 단일 숫자
    if start == end:
        return numbers[start], numbers[start]
    
    # Check memoization
    if (start, end) in memo:
        return memo[(start, end)]
    
    max_val = float('-inf')
    min_val = float('inf')
    
    # Try all possible splits
    for k in range(start, end):
        # Recursively solve left and right subexpressions
        left_max, left_min = arithmetic_max_value_recursive(numbers, operators, memo, start, k)
        right_max, right_min = arithmetic_max_value_recursive(numbers, operators, memo, k + 1, end)
        
        # Calculate all possible combinations based on the operator
        if operators[k] == '+':
            max_val = max(max_val, left_max + right_max)
            min_val = min(min_val, left_min + right_min)
        elif operators[k] == '*':
            vals = [left_max * right_max,
                   left_max * right_min,
                   left_min * right_max,
                   left_min * right_min]
            max_val = max(max_val, max(vals))
            min_val = min(min_val, min(vals))
    
    # Store in memo and return
    memo[(start, end)] = (max_val, min_val)
    return max_val, min_val

def solve_arithmetic(numbers, operators):
    memo = {}
    max_val, _ = arithmetic_max_value_recursive(numbers, operators, memo, 0, len(numbers) - 1)
    return max_val

# Example usage
numbers = [7, 4, 3, 5]
operators = ['+', '*', '+']
print("Maximum possible value:", solve_arithmetic(numbers, operators))
