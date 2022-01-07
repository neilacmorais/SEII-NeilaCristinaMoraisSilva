li = [2, 1, 3, 4, 5, 6, 7, 9, 8]
s_li = sorted(li)

print(s_li)
print(li)

li.sort()
print(li)

s_li = sorted(li, reverse =True)
print(s_li)



tup = (2, 1, 3, 4, 5, 6, 7, 9, 8)
s_tup = sorted(tup)
print(s_tup)

li = [5, -1, -2, -3, 0]
s_li = sorted(li)
print(s_li)

s_li = sorted(li, key=abs)
print(s_li)
