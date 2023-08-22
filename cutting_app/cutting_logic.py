import itertools
from itertools import combinations_with_replacement

def generate_patterns(orders, stock_width):
    widths = [order[0] for order in orders]
    patterns = []

    # Generate all combinations of widths
    for r in range(1, len(widths) + 1):
        for combination in combinations_with_replacement(widths, r):
            if sum(combination) <= stock_width:
                patterns.append(combination)
    for pattern in patterns:
        print(pattern)
    return patterns





def cutting_stock(orders, stock_width):
    n = len(orders)
    demands = [order[1] for order in orders]
    #orders = [(int(pair.split('*')[0]), int(pair.split('*')[1])) for pair in orders_str.split(',')]
    print("Parsed Orders:", orders)

    # Generate all possible patterns
    patterns = generate_patterns(orders, stock_width)
    
    # Compute the number of rolls required for each pattern
    pattern_rolls = []
    for pattern in patterns:
        rolls = [0] * n
        for width in pattern:
            index = next(i for i, order in enumerate(orders) if order[0] == width)
            rolls[index] += 1
        pattern_rolls.append(rolls)
    
    # Dynamic programming to find the minimal number of stock lengths to satisfy the demands
    memo = {}
    def dp(remaining_demands):
        if tuple(remaining_demands) in memo:
            return memo[tuple(remaining_demands)]
        
        # Base case: all demands are satisfied
        if all(demand == 0 for demand in remaining_demands):
            return 0, []
        
        min_rolls = float('inf')
        best_pattern = None
        for i, pattern in enumerate(pattern_rolls):
            new_demands = [remaining_demands[j] - pattern[j] for j in range(n)]
            # Check if the pattern is feasible
            if all(new_demand >= 0 for new_demand in new_demands):
                rolls, chosen_patterns = dp(new_demands)
                rolls += 1
                if rolls < min_rolls and chosen_patterns is not None:
                    min_rolls = rolls
                    best_pattern = chosen_patterns + [pattern]

        
        memo[tuple(remaining_demands)] = (min_rolls, best_pattern)
        return min_rolls, best_pattern
    
    _, optimal_patterns = dp(demands)
    
    formatted_patterns = []
    total_waste = 0  # Initialize total waste to 0

    formatted_patterns_with_waste = []

    if optimal_patterns is not None:  # Check if optimal_patterns is not None
        for pattern in optimal_patterns:
            pattern_str = '-'.join([str(orders[i][0]) for i, qty in enumerate(pattern) for _ in range(qty)])
            waste_for_pattern = stock_width - sum(orders[i][0]*qty for i, qty in enumerate(pattern))
            formatted_patterns_with_waste.append((pattern_str, waste_for_pattern))
    for pattern in formatted_patterns_with_waste:
        print(pattern)
    return formatted_patterns_with_waste
