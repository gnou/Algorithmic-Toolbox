# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dynamic_sequence(n):
    all_possible_numbers = [0, 0]
    for i in range(2, n+1):
        min_count = all_possible_numbers[i-1] + 1
        if i % 3 == 0:
            min_count_3 = all_possible_numbers[i//3] + 1
            if min_count_3 < min_count:
                min_count = min_count_3
        if i % 2 == 0:
            min_count_2 = all_possible_numbers[i//2] + 1
            if min_count_2 < min_count:
                min_count = min_count_2
        all_possible_numbers.append(min_count)

    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0 and all_possible_numbers[n//3] == all_possible_numbers[n] - 1:
            n = n//3
        elif n % 2 == 0 and all_possible_numbers[n//2] == all_possible_numbers[n] - 1:
            n = n//2
        else :
            n = n - 1

    return reversed(sequence)




input = sys.stdin.read()
n = int(input)
# sequence = list(optimal_sequence(n))
sequence = list(dynamic_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
