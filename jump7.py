i=0
while i<100:
    i+=1
    if i%7==0 or (i-7)%10==0 or 0<i-70<10:
        continue
    print(i)
