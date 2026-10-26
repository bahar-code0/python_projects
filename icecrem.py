# دریافت قیمت چهار بستنی
price1 = float(input("Enter the price of the first ice cream: "))
price2 = float(input("Enter the price of the second ice cream: "))
price3 = float(input("Enter the price of the third ice cream: "))
price4 = float(input("Enter the price of the fourth ice cream: "))

# محاسبه بستنی خفن (بیشترین قیمت)
max_price = price1
if price2 > max_price:
    max_price = price2
if price3 > max_price:
    max_price = price3
if price4 > max_price:
    max_price = price4
    
# محاسبه بستنی معمولی (میانگین قیمت‌ها)
average_price = (price1 + price2 + price3 + price4) / 4

# نمایش نتایج
print(f"The price of Khafen ice cream: {max_price}")
print(f"The price of regular ice cream: {average_price}")
