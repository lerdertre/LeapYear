def fun(year):
    if year%4 == 0 and not year%400 == 0:
        return True
    else:
        return False
