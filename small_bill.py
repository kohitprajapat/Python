food = input("Enter food name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
distance = float(input("Enter distance in KM: "))
distanceamount = distance*5
withoutgst = (price*quantity)+distanceamount
gst = withoutgst*0.2
totalamount = gst + withoutgst
print("")
print("Bill: ",withoutgst)
print("Gst: ", gst)
print("Delivery Charges: ",distanceamount)
print("")
print("You have to pay",totalamount,"for this order")
