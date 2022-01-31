import sys
import csv

def readData(filename):

    allFiles = []

    with open(filename) as file:
        csv_reader = csv.DictReader(file, delimiter=",")
        for entry in csv_reader:
            # O(1)
            cookieName = entry["cookie"]
            cookieDate = entry["timestamp"][0:10]
            cookieTime = entry['timestamp'][11:16]
            allFiles.append([cookieName, cookieDate])

    return allFiles


def closestDate(allCookies, tDate):
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
    tDate = sys.argv[-1]
    ans = closestDate(readDates, tDate)
    for i in ans:
        print(i)
