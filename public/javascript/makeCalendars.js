function makeCalendar(events) {
    var calendar = {
        header: {
            left: '',
            center: '',
            right: ''
        },
        events: events,
        defaultView: 'agendaWeek',
        columnFormat: 'ddd',
        duration: '00:15:00',
        minTime: '8:00:00',
        maxTime: '21:00:00',
        allDaySlot: false,
        height: 'auto'
    };

    return calendar;
}

function makeEvent(title, start, end, color){
    return {title: title, start: start, end: end, color: color}
}

