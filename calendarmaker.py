"""Monthly Calendar Maker
This program generate a text file which shows monthly calendar of a given month and year
as given the user."""

import sys
import datetime
import calendar

print("Calendar Maker")

o = sys.stdout #original standard output

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

    with open("calendar {}.txt".format(formated_date),'w') as f:
        sys.stdout = f
        #prints the specifc month,year in the calendar top
        space = 60 #gap before printing month, year on the top
        for i in range(space):
            print(" ", end="")
        print(formated_date)

        #print days
        days =  ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        intendation = 18 #gap between the next day in calendar
        days_line = "" #the line which will show the days in the calendar
        for i in range(len(days)):
            days_line += (intendation -5) * "."
            days_line += days[i]
        print(days_line)

        #print weeks
        first_week_day, num_current_days = calendar.monthrange(year,month)
        if month == 1:
            num_previous_days = 31
        else:
            previous_week_day, num_previous_days = calendar.monthrange(year,month-1)

        #calculate the number of weeks in the given month
        if first_week_day == 6:
            first_week_day = 0
        else:
            first_week_day += 1

        num_previous_dates = first_week_day
        num_weeks = (num_previous_dates + num_current_days) / 7
        if num_weeks > int((num_previous_dates + num_current_days) / 7):
            num_weeks =  int((num_previous_dates + num_current_days) / 7) +1

        weeks = [] #stores days in all weeks of the month

        #adds weeks in a month
        for i in range(num_weeks): # for each week
            weeks.append("")  # add an empty week
            n = '01'
            m = 1
            for j in range(7): # for each day in the week
                if i==0: #for the first week
                    weeks[i] += "|"
                    if j < first_week_day:
                        weeks[i] += str((num_previous_days - num_previous_dates) + j)
                    else:
                        weeks[i] += n
                    weeks[i] += intendation * " "
                    m += 1
                    n = '0{}'.format(m)
                else:
                    last_week_date = (i-1)*7 + (8 - first_week_day)
                    weeks[i] += "|"
                    if last_week_date + j -1  >= num_current_days:
                        weeks[i] += "  "
                    elif last_week_date + j -1 < 9:
                        weeks[i] += "0{}".format(last_week_date + j)
                    else:
                        weeks[i] += str(last_week_date + j) #add corresponding date to the string
                    weeks[i] += intendation * " "
            weeks[i] += "|"
        #blank string to be displayed
        blank_str = ""
        for i in range(7):
            blank_str += "|"
            blank_str += (intendation + 2) * " "
        blank_str += "|"

        #initial week string which appears on the top of each week string
        initial_week_str = ""
        for i in range(7):
            initial_week_str += "+"
            initial_week_str += "."* (intendation+2)

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
    sys.stdout = o
    print("saved to calendar {}.txt".format(formated_date))

main()