list_1= ["abc","def","ghi", "zkl"]
list_2 = []
sum = 0
for row in list_1:
    for colm in row:
        asc = ord(colm)
        sum = sum + asc
    list_2.append(sum)
print(list_2)
