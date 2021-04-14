#
# for i in iter(int, 1):
#     print("dsdsd")

# s = [1,2,4,5,1,2,5]
# c = [1,2,4,5,1,2,5]
# z = len(s)
# v = len(c)
# if z == v:
#      for i in range(z) :
#         if s[i] != c[i]:
#             print("не равны")
#             break
# else:
#     print("не равны")

с = "five thirteen two eleven seventeen two one thirteen ten four eight five nineteen"
c = с.split(" ")

# dic = {"five": 5, "thirteen": 13, "two": 2, "eleven": 11, 'seventeen': 17, 'one': 1,
#        "ten": 10, "four": 4,"eight":8, "nineteen": 19}

f = []
for i in list(range(len(c))):
    f.append({"five": 5, "thirteen": 13, "two": 2, "eleven": 11, 'seventeen': 17, 'one': 1,"ten": 10, "four": 4,"eight":8, "nineteen": 19}[c[i]])
print(f)

li = list(set(f))
print(li)

for i in range(len(li)):
    if i == int(len(li)-1): break
    if li[i] % 2 != 0: print("ggg", li[i] + li[i + 1])
    if li[i] % 2 == 0: print("ggg", li[i] * li[i + 1])

sum = 0
for i in range(len(li)):
    if li[i] % 2 != 0:
        sum = sum + li[i]

print("Сумма нечетных", sum)
