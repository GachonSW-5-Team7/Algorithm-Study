
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
def solution(scores):

    average = 0
    answer = ''
    arr=[]

    for i in range(len(scores)):
        for j in range(len(scores)):
            arr.append(scores[j][i])
        print(arr)

        if (arr.count(max(arr)) == 1) and (scores[i][i] == max(arr)):
            arr.remove(max(arr))
            average = sum(arr)/len(arr)
            answer += grading(average)
        elif (arr.count(min(arr)) == 1) and (scores[i][i] == min(arr)):
            arr.remove(min(arr))
            average = sum(arr)/len(arr)
            answer += grading(average)
        else:
            average = sum(arr)/len(arr)
            answer += grading(average)

        arr=[]

    return answer

def grading(score):

    if score >= 90:
        answer = 'A'
    elif score >=80:
        answer = 'B'
    elif score >=70:
        answer = 'C'
    elif score >=50:
        answer = 'D'
    else:
        answer = 'F'

    return answer