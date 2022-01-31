import sys
import csv
from datetime import datetime


def readData(filename):

    allFiles = []

    with open(filename) as file:
        csv_reader = csv.DictReader(file, delimiter=",")
        for entry in csv_reader:
            # O(1)
            cookieName = entry["cookie"]
            dateFrom = entry["timestamp"][0:10]
            # timeFrom = entry['timestamp'][11:16]
            cookieDate = datetime.strptime(
                dateFrom, "%Y-%m-%d"
            )  # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
            allFiles.append([cookieName, cookieDate])

    return allFiles


def closestDate(allCookies, tDate):
    tDate = datetime.strptime(tDate, "%Y-%m-%d")
    matchedCookies = {
        # cookieName: occur
    }

    maxOccur = 0
    ans = ['N/A']

    for cookieName, cookieDate in allCookies:
        if cookieDate == tDate:
            if maxOccur == 0:
                maxOccur+=1;
                ans = [cookieName]
            if cookieName in matchedCookies.keys():
                matchedCookies[cookieName] += 1
            else:
                matchedCookies[cookieName] = 1
            if maxOccur < matchedCookies[cookieName]:
                maxOccur = matchedCookies[cookieName]
                ans = [cookieName]
            elif maxOccur == matchedCookies[cookieName] and cookieName not in ans:
                ans.append(cookieName)
    
    return ans


if __name__ == "__main__":
    filename = sys.argv[1]
    readDates = readData(filename)
    print(readDates)
    tDate = sys.argv[-1]
    ans = closestDate(readDates, tDate)
    for i in ans:
        # print(i + "\n")
        pass
