year = 2000
month = 1
date = 1

x = {
	1:31, 
	2:28,
	3:31,
	4:30,
	5:31,
	6:30,
	7:31,
	8:31,
	9:30,
	10:31,
	11:30,
	12:31
}

def leap(year: int) -> bool:
	return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

f = open("thetribune.csv", "a")

while(year <= 2014):
    if(year == 2014 and month == 12):
        break
    link = "https://www.tribuneindia.com/%d/%d" % (year , year)
    if(month < 10):
        link += "0%d" % month
    else:
        link += "%d" % month
    if date < 10:
        link += "0%d" % date
    else:
        link += "%d" % date
    f.write("%d,%d,%d,%s/\n" % (year, month, date , link))
    date += 1
    if((not leap(year) and date == x[month]+1)):
        date = 1
        month += 1
        if(month == 13):
            month = 1
            year += 1
    elif leap(year) and month == 2 and date == 30:
        date = 1
        month += 1
        if(month == 13):
            month = 1
            year += 1
    elif leap(year) and month != 2 and date == x[month]+1:
        date = 1
        month += 1
        if(month == 13):
            month = 1
            year += 1