
# ارتفاع مربع را از کاربر دریافت می کنیم 
n = int(input("Enter moraba size:"))
#رسم مربع
for i in range( n ):
    print("*" * n)



# ارتفاع لوزی را از کاربر دریافت می کنیم 
diamond_height = int(input("enter lize size:"))

# تضمین کردن ارتفاع به عدد فرد
if diamond_height % 2 == 0:
   diamond_height += 1

# رسم لوزی
for i in range(1, diamond_height + 1, 2):
   spaces = " " * ((diamond_height - i) // 2)
   stars = "*" * i
   print(spaces + stars)

for i in range(diamond_height - 2, 0, -2):
    spaces = " " * ((diamond_height - i) // 2)
    stars = "*" * i
    print(spaces + stars)



    
