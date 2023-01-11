kohit = 0.2
sachin = 0.25
akhil = 0.19
kuldeep = 0.05
pratham = 0.15
deekshu = 1

product = input("Enter your product: ") 
price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))
amount = price*quantity
promo = input("Enter promo code: ")
print("")
if promo == "kohit" :
    print("Congrats you got 20% discount:",amount*0.2)
    print("")
    print("Your have to pay",amount-(amount*0.2))
    
elif promo == "sachin" :
    print("Congrats you got 25% discount:",amount*0.25)
    print("")
    print("Your have to pay",amount-(amount*0.25)) 
    
elif promo == "akhil" :
    print("Congrats you got 19% discount:",amount*0.19)
    print("")
    print("Your have to pay",amount-(amount*0.19))
    
elif promo == "kuldeep" :
    print("Congrats you got 5% discount:",amount*0.05)
    print("")
    print("Your have to pay",amount-(amount*0.05))  
    
elif promo == "pratham" :
    print("Congrats you got 15% discount:",amount*0.15)
    print("")
    print("Your have to pay",amount-(amount*0.15))   
    
elif promo == "deekshu" :
    print("Congrats you got 100% discount:",amount*1)
    print("")
    print("Your have to pay",amount-(amount*1))    
    
elif promo == "" :
    print("You have to pay",amount)    
    
else : 
    print("You entered wrong value")       
