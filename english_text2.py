
# دریافت متن انگلیسی از کاربر
text = input("Enter your text: ")

# دریافت حرف انگلیسی از کاربر
letter = input("Enter a letter: ")

# شمارش تعداد حروف مورد نظر در متن 
count = 0
for char in text:
    if char.lower() == letter.lower():
        count += 1
    
    
# نمایش تعداد حروف
print(f"{letter}={count}")

