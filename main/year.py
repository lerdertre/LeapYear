import function

OrdinaryYear = []
LeapYear_1 = []
LeapYear_2 = []

for year in range(1,10001):
    a = function.fun(year)
    if a == True:
        if year%100 == 0:
            LeapYear_1.append(year)
        else:
            LeapYear_2.append(year)
    else:
        OrdinaryYear.append(year)
    year+=1
