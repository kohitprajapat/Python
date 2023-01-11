food = input("Enter food name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
distance = float(input("Enter distance in KM: "))
distanceamount = distance*5
withoutgst = (price*quantity)+distanceamount
gst = withoutgst*0.2
totalamount = gst + withoutgst

print("Your Order of",price,"/",food,"Total amount is",totalamount)
