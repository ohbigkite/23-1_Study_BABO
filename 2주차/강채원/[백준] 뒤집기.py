seq = str(input())

if len(set(seq))==1:
  result = 0
  print(result)
else:
  to1=0
  to0=0
  if seq[0] == '0':
    to1 = 1
  else : to0 = 1

  for i in range(len(seq)-1):
    if seq[i] != seq[i+1]:
      if seq[i+1]=='0':
        to1 += 1
      else: to0 +=1

  print(min(to0,to1))