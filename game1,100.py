import random
javab=random.randint(1,1000)

count=0

while True:
    hads=int(input('what is your hads between(1:1000)?'))
    count+=1

    
    if hads<=0:
        break
    elif  hads>javab:
        print("min is smaller")
    elif hads<javab:
        print("min is larger")
    else:
        print(f"wooooooooow!!! its true!!!you can say that after {count} min")        
       
  
