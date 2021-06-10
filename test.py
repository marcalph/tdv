def feasible(bloomDays, day,k) -> bool:
    bonquets, flowers = 0, 0
    for bloom in bloomDays:
        if bloom > day:
            flowers = 0
        else:
            print(flowers, bonquets)
            bonquets += (flowers + 1) // k
            flowers = (flowers + 1) % 2
    return bonquets >= 1

days = [1,3,10,2,1,3,10,2,1,3,10,2,1]
feasible(days,day=3, k=1)