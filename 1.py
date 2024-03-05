x = int(input("Input Number : "))
for i in range(1,x+1):
    if i%3 == 0 and i%5 == 0 :
        print(i,"Ping Pong")
    elif i%3 == 0 :
        print(i,"Ping")
    elif i%5 == 0 :
        print(i,"Pong")
