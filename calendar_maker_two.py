"""Calender Generator
A program to generate calendar based on given month and year"""

import datetime

#define constants
days =  ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

#input year
while True:
    print("Please enter the year for which calender is needed to be generated")
    year = input("> ")
    if not year.isdecimal():
        continue
    if 0 < int(year):
        year = int(year)
        break
    print("Please enter a year.(It should be like 2023)")

#input month
while True:
    print("Please enter the month for which calendar is needed to be generated (1-12)")
    month = input("> ")
    if not month.isdecimal():
        continue
    if 0 < int(month) <= 12:
        month = int(month)
        break
    print("Please enter a valid month. It should be from (1-12)")

#generates the calendar text for the given date and month
def calender_generator():
    cal_text = "" #cal_text will store the calendar month string

    #Put the first month and year at the top of the calendar
    cal_text += " "*30 + datetime.date(year,month,1).strftime("%B, %Y") + " "*30 + "\n"

    #Week seperator line
    week_sep = "+----------" * 7 + "+\n"

    #blank line for those lines which displays no dates
    blank_line = "|          " * 7 + "|\n"

    # prints the header line of days
    cal_text += "sunday....monday....tuesday....wednesday....thursday....friday....saturday....\n"
    # current date which works as the refernce date
    current_date = datetime.date(year, month, 1)

    # returns the first date when the day is sunday
    while not current_date.weekday() == 6:
        current_date -= datetime.timedelta(days=1)

    while True: #for each week in the month
        cal_text += week_sep
        num_line = ""  # number line in the calendar which contains dates
        for i in range(7):
            num_line += "|" + f'{str(current_date.day):02}' + " "* 8
            current_date += datetime.timedelta(days=1)
        num_line += "|\n"

        cal_text += num_line
        cal_text += blank_line * 3

        #check if the month is not the current month
        if current_date.month != month:
            break

    cal_text += week_sep
    return cal_text

cal_text = calender_generator()

print(cal_text)

cal_file_name = "{}.txt".format(datetime.date(year,month,1).strftime("%B, %Y"))

with open(cal_file_name, "w") as fil:
    fil.write(cal_text)

print("Saved to {}".format(cal_file_name))


