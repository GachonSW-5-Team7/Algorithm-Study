def alphabetScore(score):
    if score >= 90:
        return 'A'
    elif 90 > score and score >= 80:
        return 'B'
    elif 80 > score and score >= 70:
        return 'C'
    elif 70 > score and score >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''
    
    scoretp = list(map(list, zip(*scores)))
    
    print(scoretp)
    
    for idx in range(len(scoretp)):
        maxVal = max(scoretp[idx])
        maxIdx = []
        minVal = min(scoretp[idx])
        minIdx = []
        
        for checkIdx, val in enumerate(scoretp[idx]):
            if val == maxVal:
                maxIdx.append(checkIdx)
            
            if val == minVal:
                minIdx.append(checkIdx)

        if idx in maxIdx and len(maxIdx) == 1:
            del scoretp[idx][idx]
        elif idx in minIdx and len(minIdx) == 1:
            del scoretp[idx][idx]
        
        answer = answer + alphabetScore((sum(scoretp[idx])/len(scoretp[idx])))
            
        
    return answer