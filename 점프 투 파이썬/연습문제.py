""" 2장 연습문제
#Q1
score=[80,75,55]
print((sum(score))/len(score))

#Q2
print(13%2==0)

#Q3
pin="881120-1068234"
print(pin[0:6])
print(pin[7:])

#Q4
pin="881120-1068234"
print(pin[7])

#Q5
a="a:b:c:d"
print(a.replace(":","#"))

#Q6
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#Q7
a=['Life','is','too','short']
print(" ".join(a))

#Q8
a=(1,2,3)
print(a+(4,))

#Q9

#Q10
a={'A':90,'B':80,'C':70}
result=a.pop('B')
print(a)
print(result)

#Q11
a=[1,1,1,2,2,3,3,3,4,4,5]
print(set(a))

#Q12
"""

"""3장 연습문제"""
#Q1
result=0
i=1
while i<=1000:
    if i%3==0: continue
    result+=i
    i+=1
print(result)