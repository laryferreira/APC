num_1,num_2 = input().split(',')
num_1 = int(num_1)
num_2 = int(num_2)
if num_2 > num_1:
    for v in range(num_2-num_1):
        for i in range(num_1,num_2+1, v+1):
            print(i, end=' ')
        print()
else:
    for v in range(num_1-num_2):
        for i in range(num_2, num_1+1, v+1):
            print(i, end=' ')
        print()
