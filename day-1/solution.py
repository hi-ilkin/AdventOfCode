l = list(map(int, open('input.txt', 'r')))

prev_sum = None
counter = 0

for i in range(3, len(l) + 1):
    cur_sum = sum(l[i-3:i])
    print(l[i-3:i], prev_sum, cur_sum)

    if prev_sum is not None and cur_sum > prev_sum:
        counter += 1
    prev_sum = cur_sum

print(counter)
