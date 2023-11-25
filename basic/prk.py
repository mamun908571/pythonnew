












# print("subject name            Marks           grade      Grade point")    
# print("bangla1 :                70             A-           3.5")
# print("bangla2 :                60             A-           3.5")
# print("english1 :               80             A+           5")
# print("english2 :               80             A+           5")
# print("general_math :           70             A            4.00")
# print("highermath1              50             B            3.00")
# print("highermath2 :            5              B            3.00 ")
# print("biology1 :               60             A+           5")
# print("biology2 :               20             A+           5")
# print("physics1 :               80             A+           5")
# print("chemistry2:              20             A+           5")
# print("islamic_religion:        70             A            4.00")
# print("social_science:          80             A+           5")
# print("ict :                    80             A+           5")
# ict= 80

# if((ict)<=100 and (ict)>=80):
#     ict1 = 5
#     print("ict:",ict,ict1,"A+")



name = input("enter your name:")
sum = 0 
for i in range(len(name)):
    asc = ord(name[i])
    
    print(asc)
    sum = sum + asc
print(sum)
