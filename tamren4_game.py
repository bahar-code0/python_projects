#توضیحات برای بازیکن ها
print("In this game, we need two players, the first player")
# دریافت اعداد از نفر اول
a = int(input("enter first number:"))
b = int(input("enter second number: "))

# دریافت عدد از نفر دوم
num = int(input("now second player enter your offer:"))

# محاسبه مربع عدد پیشنهادی
sq = num * num

# بررسی اینکه آیا مربع عدد پیشنهادی بین دو عدد a و b قرار دارد یا خیر
if a < sq < b or a>sq>b:
    print(True)
else:
    print(False)


