# Bilbo's Wholesale Eggs store has different wholesale prices for the eggs
# based on the number purchased

number = int(input("Enter the number of eggs: "))
dozen = int(number // 12)
cost = float((dozen*0.4)+(number-(dozen*12))/12*0.4)
price = float(cost/number)

if number >= 132 :
   print("Your cost is $0.35 per dozen or", round(price,3), "per egg." )
   print("Your bill comes to ${:.2f}.".format(cost))
   
elif number >= 72 :
   print("Your cost is $0.40 per dozen or", round(price,3), "per egg." )
   print("Your bill comes to ${:.2f}.".format(cost))

elif number >= 48 :
   print("Your cost is $0.45 per dozen or", round(price,3), "per egg." )
   print("Your bill comes to ${:.2f}.".format(cost))

else :
   print("Your cost is $0.50 per dozen or", round(price,3), "per egg." )
   print("Your bill comes to ${:.2f}.".format(cost))
