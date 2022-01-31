import sys
import csv

def readData(filename):

    allFiles = []

    with open(filename) as file:
        # read csv file
        csv_reader = csv.DictReader(file, delimiter=",")
        for entry in csv_reader:
            # 2d array for the csv contents. Each element has cookie name, cookie date, cookie time (from timestamp)
            cookieName = entry["cookie"]
            cookieDate = entry["timestamp"][0:10]
            cookieTime = entry['timestamp'][11:16]
            allFiles.append([cookieName, cookieDate])

    return allFiles


def closestDate(allCookies, tDate):
    # cookies seen in loop thus far
    matchedCookies = {
        # cookieName: occur
    }

    # track max occurrence thus far, and the corresponding cookie name in ans
    maxOccur = 0
    ans = ['N/A']

    for cookieName, cookieDate in allCookies: # take the elements of the nested list
        if cookieDate == tDate:
            # for the first match
            if maxOccur == 0:
                maxOccur+=1;
                ans = [cookieName]
            
            # for future matches

            # if have seen the cookie already
            if cookieName in matchedCookies.keys():
                matchedCookies[cookieName] += 1
            # if first time seeing cookie
            else:
                matchedCookies[cookieName] = 1


            # for updating max occurrences

            if maxOccur < matchedCookies[cookieName]:
                maxOccur = matchedCookies[cookieName]
                ans = [cookieName]
            elif maxOccur == matchedCookies[cookieName] and cookieName not in ans:
                ans.append(cookieName)
    
    return ans


if __name__ == "__main__":
    filename = sys.argv[1]
    readDates = readData(filename)
    tDate = sys.argv[-1]
    ans = closestDate(readDates, tDate)
    for i in ans:
        print(i)
