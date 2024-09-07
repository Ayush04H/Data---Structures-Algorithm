def boolean_parenthesization(expr, i, j, is_true):
    n=len(expr)
    t = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]

    if i > j:
            return 0
    if i == j:
        if is_true:
            return 1 if expr[i] == 'T' else 0
        else:
            return 1 if expr[i] == 'F' else 0
        
    # Check if value is already memoized
    if t[i][j][is_true] != -1:
        return t[i][j][is_true]

        # Initialize ways to 0
    ways = 0

        # Loop through the expression, considering only operators (i.e., skip operands)
    for k in range(i + 1, j, 2):
        operator = expr[k]

            # Recursively count the ways for each partition
        left_true = boolean_parenthesization(expr, i, k - 1, True)
        left_false = boolean_parenthesization(expr, i, k - 1, False)
        right_true = boolean_parenthesization(expr, k + 1, j, True)
        right_false = boolean_parenthesization(expr, k + 1, j, False)

            # Combine the results based on the operator
        if operator == '&':
            if is_true:
                ways += left_true * right_true
            else:
                ways += left_false * right_true + left_true * right_false + left_false * right_false

        elif operator == '|':
            if is_true:
                ways += left_true * right_true + left_true * right_false + left_false * right_true
            else:
                ways += left_false * right_false

        elif operator == '^':
            if is_true:
                ways += left_true * right_false + left_false * right_true
            else:
                ways += left_true * right_true + left_false * right_false
    
    t[i][j][is_true] = ways
    return ways


expr = "T|F&T^T"
n=len(expr)
result = boolean_parenthesization(expr, 0, n - 1, True)
print(f"Number of ways to parenthesize the expression '{expr}' to evaluate to True is {result}")
