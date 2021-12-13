# Problem 48

limit = 1000
times = 1
total = 0
for i in range(1, limit+1):
    for r in range(1, i+1):
        times =  times * i
    # print(times, end='')
    # print('')
    total += times
    times = 1
digit = len(str(total))
last_ten_digits = (str(total)[digit-10]) +  (str(total)[digit-9]) + (str(total)[digit-8]) + (str(total)[digit-7]) + (str(total)[digit-6]) + (str(total)[digit-5]) + (str(total)[digit-4]) + (str(total)[digit-3]) + (str(total)[digit-2]) + (str(total)[digit-1])
print(last_ten_digits)