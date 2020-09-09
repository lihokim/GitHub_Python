n=int(input())
s,k=map(int,input().split())
arr = list(map(int,input().split()))
cha=[]
num=[]

for i in range(0,n):
    cha.append(abs(s-arr[i]))
    num.append(i+1)
def quickSort(a,b, start, end):# 재귀함수용 함수 선언(리스트, 시작인덱스, 종료인덱스)
    if start < end: # 시작 인덱스 보다 끝 인덱스가 클 경우
        left = start # left 변수에 시작 인덱스 할당
        pivot = a[end] #  //pivot 값은 a리스트에 마지막 원소 값
        for i in range(start, end): # 시작인덱스부터 끝 원소까지 반복
            if a[i] < pivot: # 리스트 인덱스 값이 pivot 값보다 작을 경우라면
                a[i], a[left] = a[left], a[i] #  해당 인덱스와 left인덱스  swap
                b[i], b[left] = b[left], b[i]
                left += 1 # 인덱스 하나 증가 시켜주기(자리를 옮겨가며 비교해야 하기 때문에)
        a[left] , a[end] = a[end], a[left] # left인덱스와 끝 인덱스 swap
        b[left] , b[end] = b[end], b[left]
        quickSort(a,b, start, left-1) # 재귀 호출 (리스트, 시작 인덱스, left-1)
        quickSort(a,b, left+1, end) # 재귀 호출 (리스트, left+1, 종료인덱스)
quickSort(cha,num, 0, n-1)
for i in range (0,n):
    for j in range(0,n):
        if cha[i]==cha[j]:
            if arr[i]>arr[j]:
                num[i],num[j]=num[j],num[i]
for i in range(0,k):
    print(num[i])