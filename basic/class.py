
#           [class 2]
#vari able, output,datatype,arithmatic



# print("the name of the product is")
# print(10)

# product_name = "sugar"
# print(product_name)  # suga



# product_name = "sugar"
# print("the name of the product is",product_name)     #the name of the product is sugar


#         (datatype)

#1 string 2 integer 3 floot 4 list 5 dictionary 6 taple


# product_name = "suger"
# print(type(product_name))  #'str'


# product_price = 150
# print(type(product_price))  #'int'

# product_price = 150.5
# print(type(product_price))   #'float'




#       (mathematics) 

# product_name1 = "sugar"
# product_name2 = "egg"

# quantity1 = 3
# quantity2 = 4

# price1 =  150
# price2 = 50
# total_price1 = quantity1 * price1
# total_price2 = quantity2 * price2

# print(total_price1 + total_price2) #  '650'


 #        (discount) 

# product_name1 = "sugar"
# product_name2 = "egg"

# quantity1 = 3
# quantity2 = 4

# price1 =  150
# price2 = 50

# discount = 5

# total_price1 = quantity1 * price1
# total_price2 = quantity2 * price2

# total = total_price1 + total_price2

# total_after_discoumt = (total -(total*discount)/100)
# print(total)    # 650
# print(total_after_discoumt)    # 617.5




                #class 3

            # conditional statement
            # if ()                 true = 1\   false = 0
            # else                  
            # /
            # if():
            #     elif():
            #         else
#comparison operasion

# a = 10
# b = 10

# if(a==b):
#     print("a is equal to b")
# else:
#     print("something went wrong")



# a = 10
# b = 10
# if(a==b):
#     print("a is equal to b")
# else:
#     print("something went wrong")


# total_price = 501
# discount = 5


# if(total_price>500):
#     total_price = total_price - ((total_price*discount)/100)
#     print(total_price)
# else:
#     print(total_price)

# age = 17 
# if(age<=18):
#     print("you are not able to ragister for NID")
# else:
#     print("you are eligible")


         # bilding function = len()  diye value ber kore
# name = "mamun"
# size_name = len(name)
# print(size_name)

#     # empty cek korte
# name = "mamun"
# size_name = len(name)
# if(size_name==0):
#     print("the field can not be empty")
# else:
#     print("success")

                # class 4
# name = "mamun"
# phone = "0"
# gmail = "s"
# if(len(name)==0) or len(phone)==0 or len(gmail)==0:
#     print("failed")
# else:
#     if(len(name)<2 or len(name)>):
#         print("the name length must be betweeen 2 and 6")
#     elif(len(phone)!=11):
#         print("the phone number size must be equal to 11")
#     else:
#         print("success")



#################class 6
    #string, #loop , #string slicing   
        #string


# s = "this is a string."
# print(s.split())  #p ['this', 'is', 'a', 'string.'] 

# s = "this is a string."
# words = s.split()
# for w in words:
#     print(w)
# print(' '.join(words))

# list = ['this', 'is', 'a', 'string'] 
# print(' '.join(list))

# s = "this is a string"
# print(s.upper())  #p THIS IS A STRING

# s = "This is a String"
# print (s.lower())   #p this is a string

#যেটা বড় হাতের রয়েছে তা ছোট হাতের, যেটা ছোট হাতের তাকে বড় হাতের করার জন্যঃ
# s = "This is a String"
# print (s.swapcase())   #p tHIS IS A sTRING

#আমরা চাইলে স্ট্রিং এর যে কোন শব্দ অন্য কিছু দিয়ে রিপ্লেস করে দিতে পারি। যেমনঃ
# s = "This is a String"
# new = s .replace("This" , "That")
# print (new) #That is a String

# #কোন স্ট্রিং এ একটা সাব স্ট্রিং বা একটা লেটার কতবার আছে, তা বের করতে count() মেথড ব্যবহার করা হয়। যেমনঃ
# str = "This is a string!"
# print (str.count( 's'))  #p 3

# #কোন স্ট্রিং এ কোন একটা সাবস্ট্রিং খুঁজতে find() মেথড ব্যবহার করা হয়। যেমনঃ
# s = "This is a String"
# if s.find('is' ):
#     print ( 'we found "is" in the string')

# #স্ট্রিং এর লেন্থ বা কয়টা ক্যারেক্টার রয়েছে, তা বের করার জন্য len() মেথড ব্যবহার করা হয়। খেয়াল রাখতে হবে স্পেস ও একটা কারেক্টার।
# str = "This is a string"
# print(len(str))


# name = "mamun"
# size = len(name)
# print(size)  #p 5

# #string slicing
# name = "mamun"
# print(name[0:])  #p mamun
# print(name[0:2])  #p ma

#প্রথম অক্ষর বড় হাতের করতে .capitalize() ফাংশন বেবহার করতে হয়।
# name = "my name is mamun"
# print(name.capitalize())

# name = "Mamun"
# print(name[0].isupper())



# txt = "i love apples apple,apple are my favorite fruit"
# x = txt.count("apple")
# print(x)


# স্ট্রিংটি একটি বিরাম চিহ্ন (.) দিয়ে শেষ হয় কিনা তা পরীক্ষা করুন
# txt = "Hello, welcome to my world."
# x = txt.endswith(".")
# print(x)

#প্রতিটি শব্দের বড় হাতের প্রথম অক্ষর তৈরি করুন
# txt = "Welcome to my world"
# x = txt.title()
# print(x)        #p Welcome To My World



#loop 
# for i in range(6):
#     print(i)

# for i in range(1,6,2):
#     print(i)

# name = "mamun"
# for i in range(len(name)):
#     print(name[i])



########################class 7

# name = "mamun"
# sum = 0
# for i in range(len(name)):
#     asc = ord(name[i])
#     sum = sum + asc
# print(sum)



#########   list # 


# list_1 = [1,2,3,4,5]
# print(len(list_1))

# list_1 = [1,2,3,4,5]
# print(list_1[3])

# list_1 = [1,2,3,4,5]
# for i in range(len(list_1)):
#     print(list_1[i])

        #  0r     0r
# list_1 = [1,2,3,4,5]
# for i in list_1:
#     print(i)

# list_1 = [1,2,3,4,5]
# sum = 0
# for i in list_1:
#     sum = sum + i
#     print(i)





#################### class 11
