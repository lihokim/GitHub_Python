# a = f'{"python":!^12}'
# print(a)


# a = "{0:!^12}".format("python")
# print(a)


# t1=(1,2,3)
# print(t1+(4,))


# money=2000
# if money>=3000:
#     print("택시")
# else:
#     print("도보")


# pocket=[]
# if 'card' not in pocket:
#     print("도보")
# else:
#     print("버스") 


# score=50
# message="success" if score>=60 else "failure"
# print(message)


# treehit=0
# while treehit<10:
#     treehit+=1
#     print("나무를 {}번 찍었습니다".format(treehit))
# print("나무 넘어갑니다")


# number=0
# prompt=""" 
#     1.Add
#     2.Del
#     3.List
#     4.Quit


#     Enter number: """
# while number!=4:
#     print(prompt)
#     number=int(input())


##커피자판기 구현
# coffee=10
# while True:
#     money=int(input("돈을 넣어 주세요:"))
#     if money>=300:
#         coffee-=1
#         if money==300: print("커피 나왔습니다\n")
#         else: print("커피나왔습니다 거스름돈은 {}원입니다\n".format(money-300))
#     else:
#         print("돈이 부족합니다...돈만 돌려드릴게요\n")
#         print("남은 커피는 {}개입니다\n".format(coffee))
#     if coffee==0:
#         print("커피 없으므로 판매중지합니다\n")
#         break

# n=0
# while n<10:
#     if n%3==0:continue
#     else:print(n)
#     n+=1


# score=[90,25,67,45,80]
# n=0
# for i in score:
#    n+=1
#    if i>=60: print("{}번 학생은 합격입니다!!!".format(n))
#    else: print("{}번 학생은 불합격입니다...".format(n))


# sum=0
# for i in range(101):
#     sum+=i
# print(sum)


