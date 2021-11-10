num = int(input())
a_list = [int(x) for x in input().split()]
lst = sorted(a_list, reverse=True)
print(lst[0] * lst[1])
