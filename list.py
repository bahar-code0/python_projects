# ایجاد یک لیست خالی
numbers = []
count=0
# گرفتن شش عدد صحیح از کاربر
while count<6:
    num = int(input("inter a integer number: "))
    numbers.append(num)
    count=count+1
    
#چاپ لیست نامرتب    
print(numbers)
# مرتب‌سازی لیست به ترتیب صعودی
numbers.sort()

# چاپ لیست مرتب شده
print(numbers)

# چاپ بزرگترین عضو لیست
print("The largest member of the list:", numbers[-1])
