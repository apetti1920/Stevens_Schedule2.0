import itertools
from collections import defaultdict


class Calendars:
    def __init__(self, classlist):
        self.allCombos = self.getAllCombos(classlist)
        self.filteredCombos = self.removeOverlaps(self.allCombos)

    def getAllCombos(self, classlist)->itertools.product:
        temp = []
        for class1 in classlist:
            group = defaultdict(list)

            for obj in classlist[class1]:
                group[obj.activity].append(obj)

            temp.append(group.values())

        temp2 = []
        for i in temp:
            for j in i:
                temp2.append(j)

        temp3 = itertools.product(*temp2)
        return temp3

    def removeOverlaps(self, classlist)->list:
        temp1 = list(classlist)
        temp2 = temp1

        for i in temp2:
            allclasses = list(itertools.chain.from_iterable([j.Meetings for j in i]))

            for j in allclasses:
                for k in allclasses:
                    overlap = max(j['StartTime'], k['StartTime']) < min(j['EndTime'], k['EndTime'])
                    try:
                        if (j != k) and overlap:
                            temp1.remove(i)
                    except:
                        pass

        return temp1

    def getCalendars(self)->list:
        return self.filteredCombos
