# Author: Alex Arizola
# Assignment 6 | 6/07/2022
# Program / Dictionary

# TO USE math.floor
import math

weeklyTemps = { # DICTIONARY OF EACH DAY OF THE WEEK WITH TEMPERATURE PLACEHOLDERS
    # Weekday Name: Temperature Placeholder,
    'Monday': 0,
    'Tuesday': 0,
    'Wednesday': 0,
    'Thursday': 0,
    'Friday': 0,
    'Saturday': 0,
    'Sunday': 0
}

# WHEN TRIGGERED, ASK USER FOR TEMPERATURE OF EACH WEEK DAY
def AskUserForWeeklyTemperatures():
    # GO THROUGH EACH WEEKDAY AND ASK FOR THE TEMPERATURE
    for weekdayName in weeklyTemps.keys():
        temperatureInput = input('Enter the temperature for ' + weekdayName + ': ')

        if temperatureInput != '':
            weeklyTemps[weekdayName] = int(temperatureInput)
            print('You entered the temperature of ' + temperatureInput + ' for ' + weekdayName)
        else:
            weeklyTemps[weekdayName] = 0
            print('You did not enter a correct temperature for ' + weekdayName + ' so it was set to a default of 0!')

    # ONCE ALL WEEKDAYS HAVE TEMPERATURES RECORDED, GET THE COLDEST
    coldestTemperature = min(weeklyTemps.values())
    for weekdayName, weekdayTemperature in weeklyTemps.items():
        if weekdayTemperature == coldestTemperature:
            print(weekdayName + ' was the coldest day with a temperature value of ' + str(weekdayTemperature) + '.')
            break

    # ONCE ALL WEEKDAYS HAVE TEMPERATURES RECORDED, GET THE WARMEST
    warmestTemperature = max(weeklyTemps.values())
    for weekdayName, weekdayTemperature in weeklyTemps.items():
        if weekdayTemperature == warmestTemperature:
            print(weekdayName + ' was the warmest day with a temperature value of ' + str(weekdayTemperature) + '.')
            break

    # GET AVERAGE TEMPERATURE OF THE WEEK
    averageTemperature = sum(weeklyTemps.values()) / float(len(weeklyTemps))
    print('Average temperature of the week is:', math.floor(averageTemperature))

    # GET DAYS WHERE TEMPERATURES WILL BE HIGHER THAN AVERAGE
    higherThanAverageForecast = 'The following days are higher than the average temperature: '
    for weekdayName, weekdayTemperature in weeklyTemps.items():
        if weekdayTemperature > averageTemperature:
            higherThanAverageForecast = higherThanAverageForecast + weekdayName + ', '

    # FINALLY OUTPUT THE DAYS HIGHER THAN AVERAGE
    print(higherThanAverageForecast)

# TRIGGERS UPON SCRIPT EXECUTION
AskUserForWeeklyTemperatures()
