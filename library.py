#دریافت سن از کاربر
age=int(input("enter your age pleas:"))
#تعیین گروه سنی
if age<7:
    groh="A"
elif 7<=age<9:
    groh="B"
elif 9<=age<12:
    groh="C"
elif 12<=age<15:
    groh="D"
else:
    groh="E" 
#نمایش خروجی
print(f"Suitable for the age group:{groh}")