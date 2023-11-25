# car = {"model":"ml","color":"red","price":100}
# print(car['model'])

# car = {"model":"ml","color":"red","price":100}
# print(car.keys())

# car = {"model":"ml","color":"red","price":100}
# print(car.values())

# car = {"model":"ml","color":"red","price":100}
# for i in car:
#     print(i)


# car = {"model":"ml","color":"red","price":100}
# for i in car.values():
#     print(i)

# car = {"model":"ml","color":"red","price":100}
# for i,j in car.items():
#     print(i,j)


cars = {"car1":
        {"model":'m1',"price":100},
        "car2":
        {"model":'m2',"price":1000}}
for i,j in cars.items():
    for k in j.items():
        print(i,k)


