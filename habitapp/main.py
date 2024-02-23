from datetime import datetime
from sys import exception
from Habits.habit import Habit
from Habits.dailyhabit import DailyHabit
from Habits.weeklyhabit import WeeklyHabit
from Habits.monthlyhabit import MonthlyHabit
from Habits.yearlyhabit import YearlyHabit
from Enums.dayofweek import DayOfWeek
from tracker import Tracker
from analytics import get_habits_by_period, get_tracked_habits, get_longest_streak
from Enums.periodicity import Periodicity
import os
import dataio

_habit_tracker = None

def _add_daily_habit():
    print("Add a title:")
    title = input()
    
    while True:
        print("Start date (dd/mm/yyyy):")
        start_date = input()
        try:    
            start_date_parsed = datetime.strptime(start_date, '%d/%m/%Y')
        except:
            print("Invalid date")
            continue
        break
    
    while True:
        print("End date (dd/mm/yyyy):")
        end_date = input()
        try:    
            end_date_parsed = datetime.strptime(end_date, '%d/%m/%Y')
        except:
            print("Invalid date")
            continue
        break
    
    try:
        _habit_tracker.add_daily_habit(title, start_date_parsed.date(), end_date_parsed.date())
    except Exception as e:
        print(e)
        return
        
    print("Habit added!")

def _add_weekly_habit():
    print("Add a title:")
    title = input()
    
    while True:
        print("Start date (dd/mm/yyyy):")
        start_date = input()
        try:    
            start_date_parsed = datetime.strptime(start_date, '%d/%m/%Y')
        except:
            print("Invalid date")
            continue
        break
    
    while True:
        print("End date (dd/mm/yyyy):")
        end_date = input()
        try:    
            end_date_parsed = datetime.strptime(end_date, '%d/%m/%Y')
        except:
            print("Invalid date")
            continue
        break

    while True:
        print("Specify the days of week (Monday, Friday, ...)")
        days_of_week = input()
        try:
            days_of_week_parsed = days_of_week.split(',')
            day_of_week_enums = [DayOfWeek[day.strip().upper()] for day in days_of_week_parsed]
        except:
            print("Invalid format")
            continue
        break
    
    try:
        _habit_tracker.add_weekly_habit(title, start_date_parsed.date(), end_date_parsed.date(), day_of_week_enums)
    except Exception as e:
        print(e)
        return
        
    print("Habit added!")
    
def _add_monthly_habit():
    print("Add a title:")
    title = input()
    
    while True:
        print("Start date (dd/mm/yyyy):")
        start_date = input()
        try:    
            start_date_parsed = datetime.strptime(start_date, '%d/%m/%Y')
        except:
            print("Invalid date")
            continue
        break
    
    while True:
        print("End date (dd/mm/yyyy):")
        end_date = input()
        try:    
            end_date_parsed = datetime.strptime(end_date, '%d/%m/%Y')
        except:
            print("Invalid date")
            continue
        break

    while True:
        print("Specify the days (1, 2, 6, ...)")
        days_of_week = input()
        try:
            days_of_week = days_of_week.split(',')
            days_of_week_parsed = list(map(int, days_of_week))
            
        except:
            print("Invalid format")
            continue
        break
    
    try:
        _habit_tracker.add_monthly_habit(title, start_date_parsed.date(), end_date_parsed.date(), days_of_week_parsed)
    except Exception as e:
        print(e)
        return
        
    print("Habit added!")
    
def _add_yearly_habit():
    print("Add a title:")
    title = input()
    
    while True:
        print("Start date (dd/mm/yyyy):")
        start_date = input()
        try:    
            start_date_parsed = datetime.strptime(start_date, '%d/%m/%Y')
        except:
            print("Invalid date")
            continue
        break
    
    while True:
        print("End date (dd/mm/yyyy):")
        end_date = input()
        try:    
            end_date_parsed = datetime.strptime(end_date, '%d/%m/%Y')
        except:
            print("Invalid date")
            continue
        break

    while True:
        print("Specify the day and month (dd/mm)")
        day_and_month = input()
        try:
            day_and_month = day_and_month.split('/')
            
            if len(day_and_month) != 2:
                raise exception
            
            day = int(day_and_month[0])
            month = int(day_and_month[1])
        except:
            print("Invalid format")
            continue
        break
    
    try:
        _habit_tracker.add_yearly_habit(title, start_date_parsed.date(), end_date_parsed.date(), [(day, month)])
    except Exception as e:
        print(e)
        return
        
    print("Habit added!")

def _list_habits():
    if len(_habit_tracker.habits) == 0:
        print("No habits detected")
        return

    for habit in _habit_tracker.habits:
        print(habit.task)
        
def _list_today_habits():
    today_day = datetime.today().date()
    today_habits = [h for h in _habit_tracker.habits if h.is_tracking(today_day)]
    if len(today_habits) == 0:
        print("No habits detected")
        return
    
    for habit in today_habits:
        print(habit.task)

def _get_day_habits():
    selected_date_parsed = datetime.now()
    while True:
        print("Select a date (dd/mm/yyyy):")
        selected_date = input()
        try:    
            selected_date_parsed = datetime.strptime(selected_date, '%d/%m/%Y').date()
        except:
            print("Invalid date")
            continue
        break
    
    day_habits = _habit_tracker.get_date_habits(selected_date_parsed)
    
    if len(day_habits) == 0:
        print("No habits for the date")
    else:
        for habit in day_habits:
            print(habit.task)
        
def _remove_habit():
    habits_count = len(_habit_tracker.habits)
    if habits_count == 0:
        print("No habits detected")
        return
    
    print("Select an habit to delate")
    for x in range(0, habits_count):
        print(x + 1,")", _habit_tracker.habits[x].task)
    print("0) Back")
        
    index = -1
    while True:
        try:
            index = int(input()) - 1
        except:
            print("Index is not valid number")
            continue
        
        if index == -1:
            return

        if index < 0 or index > habits_count - 1:
            print("Index out of range")
            continue
        
        break
        
    _habit_tracker.remove_habit(_habit_tracker.habits[index])
    print("Habit removed!")
    
def _mark_habit_done():
    while True:
        print("Select a date (dd/mm/yyyy):")
        selected_date = input()
        try:    
            selected_date_parsed = datetime.strptime(selected_date, '%d/%m/%Y').date()
        except:
            print("Invalid date")
            continue
        break
    
    day_habits = [h for h in _habit_tracker.habits if h.is_tracking(selected_date_parsed)]
    if day_habits == 0:
        print("No habits detected")
        return
    
    print("Select an habit to mark as done")
    for x in range(0, len(day_habits)):
        print(str(x + 1) + ") " + day_habits[x].task)
    print("0) Back")
    
    index = -1
    while True:
        try:
            index = int(input()) - 1
        except:
            print("Index is not valid number")
            continue
        
        if index == -1:
            return
        
        if index < 0 or index > len(day_habits) - 1:
            print("Index out of range")
            continue
        
        break
        
    try:
        day_habits[index].mark_done(selected_date_parsed)
    except Exception as e:
        print(e)
        return
        
    print("Habit marked done!")

def _unmark_habit_done():
    while True:
        print("Select a date (dd/mm/yyyy):")
        selected_date = input()
        try:    
            selected_date_parsed = datetime.strptime(selected_date, '%d/%m/%Y').date()
        except:
            print("Invalid date")
            continue
        break
    
    today_habits = [h for h in _habit_tracker.habits if h.is_tracking(selected_date_parsed)]
    if today_habits == 0:
        print("No habits detected")
        return
    
    print("Select an habit to unmark as done")
    for x in range(0, len(today_habits)):
        print(str(x + 1) + ") " + today_habits[x].task)
    
    print("0) Back")
        
    index = -1
    while True:
        try:
            index = int(input()) - 1
        except:
            print("Index is not valid number")
            continue

        if index == -1:
            return

        if index < 0 or index > len(today_habits) - 1:
            print("Index out of range")
            continue
        
        break
        
    try:
        today_habits[index].mark_undone(selected_date_parsed)
    except Exception as e:
        print(e)
        return
        
    print("Habit unmarked done!")
    
def _get_habit_streak():
    habits_length = len(_habit_tracker.habits)
    if habits_length == 0:
        print("No habits detected")
        return
    
    print("Select an habit")
    for x in range(0, habits_length):
        print(str(x + 1) + ") " + _habit_tracker.habits[x].task)
    print("0) Back")
    
    index = -1
    while True:
        try:
            index = int(input()) - 1
        except:
            print("Index is not valid number")
            continue
        
        if index == -1:
            return
        
        if index < 0 or index > habits_length - 1:
            print("Index out of range")
            continue
        
        break
        
    try:
        print("streak:", _habit_tracker.habits[index].get_streak())
    except Exception as e:
        print(e)
        return
    
def _present_tracked_habits():
    traked_habits = get_tracked_habits(_habit_tracker.habits)
    print("Traked habits:")
    for traked in traked_habits:
        print(traked)
        
def _present_higher_streak_habit():
    print("Max streak:", get_longest_streak(_habit_tracker.habits))
    
def _present_by_periodicity():
    index = -1
    while True:
        print("Select a periodicity:")
        print("1) Daily")
        print("2) Weekly")
        print("3) Monthly")
        print("4) Yearly")
    
        try:
            index = int(input()) - 1
        except:
            print("Index is not valid number\n")
            continue
        
        if index < 0 or index > 3:
            print("Index out of range\n")
            continue
        
        break
    
    period_habits = get_habits_by_period(Periodicity(index), _habit_tracker.habits)
    
    if len(period_habits) == 0:
        print("No habits in the period\n")
        return
        
    for habit in period_habits:
        print(habit.task)
        
def _save_data():
    try:
        dataio.save_data(_habit_tracker.habits)
    except Exception as e:
        print("An error occured while saving the data. Please try again")
        return
    
    print("Saved!")
    
def _main_loop():
    while True:
        
        print("Select an option")
        print("********************\n")

        print("1) Add daily habit")
        print("2) Add weekly habit")
        print("3) Add monthly habit")
        print("4) Add yearly habit")

        print("\n********************\n")

        print("5) List all habits")
        print("6) List today habits")
        print("7) Get habits from specific day")
        print("8) Get currently tracked habits")
        print("9) Get habits by periodicity")
        
        print("\n********************\n")
        
        print("10) Mark habit done")
        print("11) Mark habit undone")
        print("12) Remove habit")

        print("\n********************\n")
        
        print("13) Get habit streak")
        print("14) Get higher habit streak")

        print("\n********************\n")
        
        print("15) Save")

        print("\n********************\n")
        
        print("0) Exit")
        
        option = input()
        os.system('cls')
        
        match option:
            case "1":
                _add_daily_habit()
            case "2":
                _add_weekly_habit()
            case "3":
                _add_monthly_habit()
            case "4":
                _add_yearly_habit()
            case "5":
                _list_habits()
            case "6":
                _list_today_habits()
            case "7":
                _get_day_habits()
            case "8":
                _present_tracked_habits()
            case "9":
                _present_by_periodicity()
            case "10":
                _mark_habit_done()
            case "11":
                _unmark_habit_done()
            case "12":
                _remove_habit()
            case "13":
                _get_habit_streak()
            case "14":
                _present_higher_streak_habit()
            case "15":
                _save_data()
            case "0":
                break
            
        print("\n***Press enter to continue***")
        input()
        os.system('cls')

data = []
try:
    data = dataio.load_data()
except FileNotFoundError:
    print("Init data not found\n")
except Exception as e:
    print("Error reading the file\n")

_habit_tracker = Tracker(data)
_main_loop()