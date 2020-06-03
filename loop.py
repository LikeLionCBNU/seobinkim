#0 ~ 100 까지의 숫자 중에서 3과 4로 끝나지 않는 숫자가 출력되도록 하시오.

# while문
i = 0
while True:
    if i > 100: 
        break
    if (i-3)%10 == 0 or (i-4)%10 == 0: 
        i+=1
        continue
    else: 
        print(i)
    i+=1

print("")

#for문
numbers = range(101)

for i in numbers:
    if (i-3)%10 == 0 or (i-4)%10 == 0: 
        continue
    else: 
        print(i)



