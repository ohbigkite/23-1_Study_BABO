### 3-1. 거스름돈

### 문제풀이 핵심아이디어 또는 새롭게 알게된 내용: 
    coin list 를 만들어 놓고 나누기로 나눠주는 횟수를 구한 후 나머지 값을 업데이트!
            
### 코드의 시간복잡도와 그 이유:    
    O(M)    
    > 반복문이 coin 종류 수만큼만 돌기 때문
   
    
    
### 주석이 가득 담긴 코드:
```python

#N : 상품 가격, M : 고객이 낸 돈
def change(N,M):
    cnt = 0
    money = [500,100,50,10]
    
    n = M-N # 거슬러줘야 하는 돈
    
    for m in money: #O(m) 동전 종류의 수
        cnt += (n//m) # 나눠주는 횟수
        n %= m
    
    return cnt 

## 총 시간복잡도 : O(M)

```

### 3-2. 큰 수의 법칙

### 문제풀이 핵심아이디어 또는 새롭게 알게된 내용: 
    가장 큰 수를 만드는 것이므로 첫번째로 큰 수와 두번째로 큰 수만 번갈아 가면서 더하면 됨
            
### 코드의 시간복잡도와 그 이유:    
    O(M X K)   
    > 반복문이 두 번인데 M만큼, K만큼 돌아서
   
    
    
### 주석이 가득 담긴 코드:
```python

n,m,k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True: # O(m)
    for i in range(k): #O(k)
        if m == 0:
            break
        result += first
        m-=1
        
    if m == 0:
        break
    
    result += second
    m-=1
    
print(result)

## 총 시간복잡도 : O(M X K)

```

### 3-3. 숫자 카드 게임

### 문제풀이 핵심아이디어 또는 새롭게 알게된 내용: 
    N,M을 입력받고 data 를 한 줄씩 입력받아 오는 걸 처음에 이해 못 했었는데 
    한 줄씩 입력 받아 바로바로 min 값, result 값을 업데이트함!
            
### 코드의 시간복잡도와 그 이유:    
    3-1 : O(N)
    > 반복문이 N만큼 돌기 때문
    3-2 : O(N X M)
    > 이중 반복문이며 각각 N,M 번 돌기 때문
   
    
    
### 주석이 가득 담긴 코드:
```python
#3-1
n,m = map(int,input().split())
# data = map(int, input().split())

result = 0

for i in range(n): # O(n)
    data = map(int, input().split()) # 한 줄씩 입력받아 바로 처리
    min_value = min(data)
    
    result = max(result,min_value)

print(result)

## 총 시간복잡도 : O(N)

```

```python
# 3-2
n,m = map(int,input().split())

result = 0

for i in range(n): # O(n)
    data = map(int, input().split()) 
    min_value = 10001
    
    for d in data: # O(m)
        min_value = min(min_value,d)
    
    result = max(result,min_value)
    
print(result)

##총 시간복잡도 : O(N X M)

```

### 3-4. 1이 될 때까

### 문제풀이 핵심아이디어 또는 새롭게 알게된 내용: 
    coin list 를 만들어 놓고 나누기로 나눠주는 횟수를 구한 후 나머지 값을 업데이트!
            
### 코드의 시간복잡도와 그 이유:    
    4-1. O(logN) ??
    > 반복문이 N만큼 돌진 않고, K로 나눠가면서 돌아가기 때문 (확실치 않아요....ㅎㅎ)
    
    4-2. O(1) ??
    > 반복문 없이 target과 result에 미리 값을 다 넣어두고 while문 내에서 n//k 만큼 반복되는데 
    이는 상수에 해당하기 
   
    
    
### 주석이 가득 담긴 코드:
```python
# 4-1)
def to_one(N,K):
    cnt = 0
    while N > 1:
        if N % K == 0: 
            N %= K
            cnt += 1
        else :
            N -= 1
            cnt += 1

    return cnt

## 총 시간복잡도 : O(logN) ??

```

```python
# 4-2) 참고 코드
n,k = map(int, input().split())

result = 0

while True:
    target = (n//k)*k # k로 나누어 떨어지는 수를 구해둠
    result += (n-target) # 1을 빼야하는 만큼을 result에 저장
    n = target
    
    if n < k:
        break
    
    #k로 나눔
    result += 1
    n //= k

#나눈 후 1씩 빼는 연산 더해줌
result += (n-1)
print(result)

## 총 시간복잡도 : O(1)??

```
