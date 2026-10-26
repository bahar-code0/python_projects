# ایجاد دو مجموعه خالی
x1=set()
x2=set()
# گرفتن پنج عدد صحیح از کاربر و اضافه کردن به مجموعه اول
print("inter 5 integer numbers for first group")
count=0
while count<5:
    num = int(input("number: "))
    x1.add(num)
    count+=1

# گرفتن پنج عدد صحیح دیگر از کاربر و اضافه کردن به مجموعه دوم
print("inter 5 integer numbers for second group")
count=0
while count<5:
    num = int(input("number: "))
    x2.add(num)
    count+=1 

# نمایش دو مجموعه     
print(f"first set:{x1}")
print(f"second set:{x2}")
# محاسبه و نمایش اشتراک دو مجموعه
print("insersection set:",x1.intersection(x2))
# محاسبه و نمایش اجتماع دو مجموعه
print("union set:",x1.union(x2))
