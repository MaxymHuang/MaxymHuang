import csv
def getdata(filename):
    actualdata = []
    with open(filename, 'r', encoding = 'UTF-8') as appdata:
        next(appdata)
        tempdata = list(csv.reader(appdata))
        for row in tempdata:
            actualdata.append(row)
    return actualdata

def countup(data):
    results = []
    appletvcount = 0
    desktopcount = 0
    iPadcount = 0
    iPhonecount = 0
    iPodcount = 0
    for i in range(4, len(data)):
        if data[i][1] == '-':
            appletvcount += 0
        else:
            appletvcount += float(data[i][1])
        if data[i][2] == '-':
            desktopcount += 0
        else:
            desktopcount += float(data[i][2])
        if data[i][3] == '-':
            iPadcount += 0
        else:
            iPadcount += float(data[i][3])
        if data[i][4] == '-':
            iPhonecount += 0
        else:
            iPhonecount += float(data[i][4])
        if data[i][5] == '-':
            iPodcount += 0
        else:
            iPodcount += float(data[i][5])
    results.append(appletvcount)
    results.append(desktopcount)
    results.append(iPadcount)
    results.append(iPhonecount)
    results.append(iPodcount)
    return  results

file = input('enter file name: ')
names = ['apple TV', 'Desktop', 'iPad', 'iPhone', 'iPod']
stats = getdata(file)
numbers = countup(stats)
finalvalues = {key:val for key, val in zip(names, numbers)}
downloadsum = sum(numbers)
print('Your results are: ' +str(finalvalues) +' and the total download count is: ' +str(downloadsum))


