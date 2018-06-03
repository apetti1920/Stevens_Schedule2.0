import datetime

class individualClass:
    def __init__(self, sectionxml):
        attributes = sectionxml.attrib
        try:
            self.nextSunday = nextSunday()  # find the date of next sunday
            self.dayConvertion = {'M': 1, 'T': 2, 'W': 3, 'R': 4, 'F': 5, 'S': 1, 'U': 1}

            self.Title = attributes['Title']

            if len(attributes['Section'].split(' ')) > 1:
                self.Section = {'Name': attributes['Section'].split(' ')[0],
                                'Number': attributes['Section'].split(' ')[1][:3],
                                'Letter': attributes['Section'].split(' ')[1][3:]}
            else:
                self.Section = {'Name': attributes['Section'][0:4],
                                'Number': attributes['Section'][4:7],
                                'Letter': attributes['Section'][7:]}

            self.CallNumber = attributes['CallNumber']
            self.Instructor = attributes['Instructor1']
            self.Activity, self.Site, self.Meetings = self.createMeetings(
                [i for i in sectionxml.getchildren() if i.tag == 'Meeting'])
        except Exception as e:
            pass

    def getSection(self) -> str:
        return self.Section['Name'] + ' ' + self.Section['Number']

    def createMeetings(self, meetings) -> tuple:
        site = []
        meetinglist = []
        activitylist = []
        for meeting in meetings:
            attributes = meeting.attrib
            site.append(attributes['Site'])

            if attributes['Site'] == 'Castle Point' and attributes['Day'] != 'TBA':
                for day in attributes['Day']:
                    date = self.nextSunday + datetime.timedelta(self.dayConvertion[day])
                    starttime = attributes['StartTime'][:-1].split(':')
                    starttime = date.replace(hour=int(starttime[0]), minute=int(starttime[1]), second=int(starttime[2]),
                                             microsecond=0)
                    endtime = attributes['EndTime'][:-1].split(':')
                    endtime = date.replace(hour=int(endtime[0]), minute=int(endtime[1]), second=int(endtime[2]),
                                           microsecond=0)

                    meetinglist.append({'Building': attributes['Building'], 'Room': attributes['Room'],
                                        'StartTime': starttime, 'EndTime': endtime})

                    activitylist.append(attributes['Activity'])

        return list(set(activitylist))[0], set(site), meetinglist

    def __str__(self) -> str:
        return self.getSection() + self.Section['Letter']


def nextSunday() -> datetime:
    d = datetime.datetime.now()
    while d.weekday() != 6:
        d += datetime.timedelta(1)

    return d
