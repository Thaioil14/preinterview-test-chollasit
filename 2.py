x,y,z = list(map(int, input("Input Number : ").split()))

for i in range(1,x+1):
    if i%y == 0 and i%z == 0 :
        print(i,"Ping Pong")
    elif i%y == 0 :
        print(i,"Ping")
    elif i%z == 0 :
        print(i,"Pong")

