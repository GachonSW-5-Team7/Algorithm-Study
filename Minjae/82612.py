def solution(price, money, count):
    answer = 0

    for i in range(1, count+1):
        currentPrice = price * i

        if currentPrice > money:
            answer = answer + (currentPrice - money)
            money = 0
        elif money == 0:
            answer = answer + currentPrice
        else:
            money = money - currentPrice

    return answer