"""Monthly Calendar Maker
This program generate a text file which shows monthly calendar of a given month and year
as given the user."""

# prints the given month and year
# print the days from monday to sunday
# printing dates
#- calculate number of days in the month and from the previous month
## calculate the day of the first date, and subtract index of the first day + 1 from 7 and then PREVIOUSMONTHS'last date - this num and then fill that number as the first number until the index and then start from 1
## for week two AND three and four :after the last date add 7 more dates with a for loop
## for week five : days = no. of days in the month - last day in week four and other days as from 1,2,3,...
### we have days list in each week right now create a list WEEKS
### for each week in WEEKS print days then \n

#-- INSTEAD OF LIST USE STRINGS AND THUS add the given number
import datetime
import calendar

print("Calendar Maker")


def main():
    #take the year as input
    print("Enter the year which calendar need to be displayed")
    while True:
        year = input("> ")
        if not year.isdecimal():
            continue
        if 1000 <= int(year) <= 9999:
            year = int(year)
            break

        print("Please enter a valid year!")

    #takes the month as input
    print("Enter the month for which calendar is to be generated")
    while True:
        month = input("> ")
        if not month.isdecimal():
            continue
        if 0 < int(month) <= 12:
            month = int(month)
            break
        print("Please enter a valid month!")

   #given month, year expressed in a specific format
   # date = datetime.date.strptime("{} {}".format(month, year), )
    given_date = datetime.date(year,month,1)
    formated_date = given_date.strftime("%B, %Y")

    #prints the specifc month,year in the calendar top
    space = 30 #gap before printing month, year on the top
    for i in range(space):
        print(" ", end="")
    print(formated_date)

    #print days
    days =  ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    intendation = 4 #gap between the next day in calendar
    days_line = "" #the line which will show the days in the calendar
    for i in range(len(days)):
        days_line += intendation * "."
        days_line += days[i]
    print(days_line)

    #print weeks
    first_week_day, num_current_days = calendar.monthrange(year,month)
    if month == 1:
        num_previous_days = 31
    else:
        previous_week_day, num_previous_days = calendar.monthrange(year,month-1)

    #calculate the number of weeks in the given month
    num_previous_dates = first_week_day

    num_weeks = int((num_previous_days + num_current_days) / 7)


    weeks = [] #stores days in all weeks of the month

    #adds weeks in a month
    for i in range(num_weeks):
        for j in range(7):
            if i==1:
                weeks[i] += "|"
                n = 1
                if j < first_week_day:
                    weeks[i] += (num_previous_days - num_previous_dates) + j
                else:
                    weeks[i] += n
                weeks[i] += (intendation +6) * " "
            else:
                last_week_date = i*7 + (7 - first_week_day)
                weeks[i] += "|"
                weeks[i] += last_week_date + i
                weeks[i] += (intendation + 6) * " "
        weeks[i] += "|"
    #blank string to be displayed
    blank_str = ""
    for i in range(7):
        blank_str += "|"
        blank_str += (intendation + 6) * " "
        blank_str +="|"

    #initial week string which appears on the top of each week string
    initial_week_str = ""
    for i in range(7):
        initial_week_str += "+"
        initial_week_str += "."* (intendation+6)*2
        initial_week_str += "+"



    #print weeks
    for week in weeks:
        print(initial_week_str)
        print(week)
        print(blank_str)
        print(blank_str)
        print(blank_str)
        print(blank_str)
        print(blank_str)
        print(initial_week_str)

main()