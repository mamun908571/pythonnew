print("Output 1 ")
print("")

list_1= [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
output1 = []
for i in list_1[:2]:
    output1.append(i)

output1.insert(2,[9,0,1,2])
output1.insert(3,[3,4,5,6])



for j in output1:
    print(j)


odd_and_even =[]
for k in list_1:
    for l in k:
        if(l%2)==0:
            odd_and_even.append("even")
        else:
            odd_and_even.append("odd")
print("")
print("Output 2 ")
print("")

odd_and_even1=[]
odd_and_even1.append(odd_and_even[:4])
odd_and_even1.append(odd_and_even[4:8])
odd_and_even1.append(odd_and_even[8:12])
odd_and_even1.append(odd_and_even[12:17])

for lists in odd_and_even1:
    print(lists)



print("")
print("Output 3 ")
print("")

output3 = [list_1[1][0]*2,list_1[3][0]*2,list_1[1][1]*2,list_1[2][0]*2]

print(output3)

print("")
print("Output 4 ")
print("")

even =[]
for even1 in output3:
        if (even1 % 2)== 0:
            even.append("even")
        else:
            even.append("odd")
print(even)