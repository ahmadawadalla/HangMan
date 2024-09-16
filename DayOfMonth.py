def daysChecker(maxYear,month,day):
    year = 1753
    days = 0
    week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while year <= maxYear:
        daysOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
        if year % 100 != 0 or year % 400 == 0:
            if year % 4 == 0:
                daysOfMonth[1] += 1
        for i in range(len(daysOfMonth)):
            if year == maxYear and i == month - 1:
                days += day - 1
                return (week[days % 7])
            days += daysOfMonth[i]
        year += 1

month,day,year = input('Enter (MM/DD/YYYY): ').split('/')
print('\n' + daysChecker(int(year),int(month),int(day)))