import re

text = input("Paste text here:")
#search and grouped it into month,date and year

dateRegex = re.compile(r'([0-3]\d)/([0-1]\d)/([1-2]\d\d\d)')
mo = dateRegex.findall(text)
print(mo)

numDates = len(mo)
x=0

dates = []

#Check whether the dates are valid or not
while x < numDates:
    # if february
    if int(mo[x][1]) == 2:
        #if leap year
        if int(mo[x][2]) % 100 == 0:
            if int(mo[x][2]) % 400 == 0:
                if int(mo[x][0]) <= 29:
                   dates.append(mo[x][0] + "/" + mo[x][1] + "/" + mo[x][2])
            else:
                if int(mo[x][0]) <= 28:
                    dates.append(mo[x][0] + "/" + mo[x][1] + "/" + mo[x][2])
        elif int(mo[x][2]) % 4 == 0:
                if int(mo[x][0]) <= 29:
                    dates.append(mo[x][0] + "/" + mo[x][1] + "/" + mo[x][2])
    #if 30 days
    elif int(mo[x][1]) == 4 or int(mo[x][1]) == 6 or int(mo[x][1]) == 9 or int(mo[x][1]) == 11: 
        if int(mo[x][0]) <= 30:
            dates.append(mo[x][0] + "/" + mo[x][1] + "/" + mo[x][2])
    #if 31 days
    elif int(mo[x][1]) == 1 or int(mo[x][1]) == 3 or int(mo[x][1]) == 7 or int(mo[x][1]) == 8 or int(mo[x][1]) == 10 or int(mo[x][1]) == 12 : 
        if int(mo[x][0]) <= 31:
            dates.append(mo[x][0] + "/" + mo[x][1] + "/" + mo[x][2])
    x = x + 1


print("Dates Detected:")
print(dates)


