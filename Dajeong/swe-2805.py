T = int(input())
 
for test_case in range(1, T + 1):
    sum = 0
    length = int(input())
    key = length // 2
    for i in range(key + 1):
        line = input()
        for j in range( key - i, key + i +1):
            sum += int(line[j])
    for i in range(key - 1, -1, -1):
        line = input()
        for j in range( key - i, key + i +1):
            sum += int(line[j])
     
    print("#%d %d" %(test_case, sum))