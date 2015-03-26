def leap_year(year):
    #the ==0 tests for equality
    if (year % 400) ==0:
        return True
    elif (year % 100) ==0:
        return False
    elif (year % 4)==0:
        #return prints whether true or false
        return True
    else:
        return False
for year in range(1999,2017):
    print(year,leap_year(year))
