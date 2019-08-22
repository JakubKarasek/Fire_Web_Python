def digit_sum(n):
  sum_list = []
  if n > 0:
    n = str(n)
    for x in map(int,n):
        sum_list.append(x)
    total = 0
    for y in range(0,len(sum_list)):
        total += sum_list[y]
    return total


print(digit_sum(1234))
