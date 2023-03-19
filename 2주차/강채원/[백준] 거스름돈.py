price = int(input()) # 여러 개 입력 받을 때만 map()쓰기^^
change = 1000-price

coin = [500,100,50,10,5,1]

cnt=0
for c in coin:
    if change == 0:
        break
    cnt+= change//c
    change %= c
print(cnt)
