product = input("Enter product name : ")
price = int(input("Enter Price: "))
discount = int(input("Enter discount in % : "))

print("Your",product ,"price after discount is ",float(price-(price*discount/100)) )