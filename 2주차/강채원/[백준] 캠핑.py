i=0
while True:
  i+=1
  l,p,v = map(int,input().split())
  
  if l ==0 and p==0 and v==0:
    break

  max = v//p
  plus = v % p

  if plus > l: # 남은 일수가 l 보다 큰 경우는 l만큼 이용 가능
    plus = l
  days = max*l + plus
  
  print("Case %d: %d" %(i,days))