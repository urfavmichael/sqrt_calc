def closest_perfect_square_num(n):
    # closest_square = None
    closest_num = None
    min_diff = float('inf')

    i = 0
    while i * i <= n:
        i += 1

    for j in range(i - 1, i + 2):
        perfect_square = j * j
        diff = abs(perfect_square - n)

        if diff < min_diff:
            min_diff = diff
            # closest_square = perfect_square
            closest_num = j

    return closest_num

def square_root(n, k):
    closest_perfect_square = closest_perfect_square_num(n)
    answer = closest_perfect_square + (n - closest_perfect_square ** 2) / (closest_perfect_square * 2)
    for i in range(1, k):
        answer = answer + (n - answer ** 2) / (answer * 2)
    return answer
