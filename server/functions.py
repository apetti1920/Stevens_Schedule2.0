from urllib import request
import xml.etree.ElementTree as ET

from server.Calendar import Calendars
from server.XMLtoClasses import individualClass


def getAllClasses(year: str, term: str) -> list:
    response = request.urlopen('https://web.stevens.edu/scheduler/core/core.php?cmd=getxml&term=' + year + term)
    data = response.read()
    xml = ET.fromstring(data)
    allclasses = [individualClass(child) for child in xml]

    return allclasses


def getCalendarFromClasses(classList: str, allClasses: list) -> list:
    divA = {}

    for selected in classList:
        divA[selected] = [j for j in allClasses if j.getSection() == selected]

    return Calendars(divA).getCalendars()
