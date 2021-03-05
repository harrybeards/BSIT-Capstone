from calendar import HTMLCalendar

from .models import Meal


class Calendar(HTMLCalendar):
    def __init__(self, events=None):
        super(Calendar, self).__init__()
        self.events = events

    def formatday(self, day, weekday, events):
        """
        Return a day as a table cell.
        """
        events_from_day = events.filter(day__day=day)
        events_html = "<ul>"
        for event in events_from_day:
            events_html += event.title + "<br>"
        events_html += "</ul>"

        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)

    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """

        events = Meal.objects.filter(day__month=themonth)

        v = []
        a = v.append
        a('<table border="1" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, events))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)


# class Calendar(HTMLCalendar):
#     def __init__(self, year=None, month=None):
#         self.year = year
#         self.month = month
#         super(Calendar, self).__init__()
#
#     def formatday(self, day, meals):
#         meals_per_day = meals.filter(start_time__day=day)
#         d = ''
#         for meal in meals_per_day:
#             d += f'<li class="calendar_list"> {meal.get_absolute_url}</li>'
#         if day != 0:
#             return f'<td><span class="date">{day}</span><ul>{d}</ul></td>'
#         return '<td></td>'
#
#     def formatweek(self, theweek, meals):
#         week = ''
#         for d, weekday in theweek:
#             week += self.formatday(d, meals)
#         return f'<tr>{week}</tr>'
#
#     def formatmonth(self, withyear=True):
#         meals = Meal.objects.filter(start_time__year=self.year, start_time__month=self.month)
#         cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
#
#         cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
#         cal ++ f'{self.formatweekheader()}\n'
#
#         for week in self.monthdays2calendar(self.year, self.month):
#             cal += f'{self.formatweek(week, meals)}\n'
#         return cal
