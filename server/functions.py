from urllib import request
import ssl
import xml.etree.ElementTree as ET

from server.Calendar import Calendars
from server.XMLtoClasses import individualClass


def getAllClasses(year: str, term: str) -> list:
    context = ssl._create_unverified_context()
    response = request.urlopen('https://web.stevens.edu/scheduler/core/core.php?cmd=getxml&term=' + year + term, context=context)
    data = response.read()
    xml = ET.fromstring(data)
    allclasses = []
    for child in xml:
        try:
            allclasses.append(individualClass(child))
        except Exception as e:
            pass

    return allclasses


def getAllClassNames(classes: list) -> list:
    x = [x.getSection() for x in classes]
    return list(set(x))


def getCalendarFromClasses(classList: str, allClasses: list) -> list:
    divA = {}

    for selected in classList:
        divA[selected] = [j for j in allClasses if j.getSection() == selected]

    return Calendars(divA).getCalendars()