def calculate_discount(price, discount_percent):
     
    if discount_percent >=20:
     discount_amount = price*(20/100)
     final_price = price -discount_amount
     return final_price
    else: 
       return price

price= (1000)
discount_percentage= (20)
final_price= calculate_discount (price, discount_percentage)
print(f"final price is:{final_price}")





  
  

  


   
