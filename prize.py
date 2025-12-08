def max_prize_greedy(n, k, number_str):
    result_stack = []
    removals_left = k

    for digit in number_str:

        while removals_left > 0 and len(result_stack) > 0 and result_stack[-1] < digit:
            result_stack.pop()
            removals_left -= 1

        result_stack.append(digit)


    while removals_left > 0:
        result_stack.pop()
        removals_left -= 1
    final_prize = ''.join(result_stack)
    return int(final_prize)


n, k = input().split()
n = int(n)
k = int(k)
number_str = input()

print(max_prize_greedy(n, k, number_str))