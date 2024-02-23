from datetime import datetime
import json
from Enums.dayofweek import DayOfWeek
from Habits.habit import Habit
from Habits.dailyhabit import DailyHabit
from Habits.weeklyhabit import WeeklyHabit
from Habits.monthlyhabit import MonthlyHabit
from Habits.yearlyhabit import YearlyHabit
from Habits.habitencoder import HabitEncoder

def load_data():
    """Load habit data from a JSON file.

    Returns:
        habits ([Habit]): A list of Habit objects loaded from the JSON file.
    """
    habits = []

    with open("init.json", "r") as read_file:
        data = json.load(read_file)

    for habit in data:
        
        dict_habit = json.loads(habit)
        task = dict_habit["task"]
        start_date = datetime.fromisoformat(dict_habit["start"]).date()
        finish_date = datetime.fromisoformat(dict_habit["finish"]).date()
        tracking_data = [datetime.fromisoformat(tracking) for tracking in dict_habit["trackData"]]
        max_streak = dict_habit["maxstreak"]

        if dict_habit["type"] == "DAILY":
            habits.append(DailyHabit(task, start_date, finish_date, tracking_data, max_streak)) 
        elif dict_habit["type"] == "WEEKLY":
            periodicity = dict_habit["periodicity"]
            periodicity_parsed = [DayOfWeek(day.strip().upper()) for day in periodicity]
            habits.append(WeeklyHabit(task, start_date, finish_date, periodicity_parsed, tracking_data, max_streak)) 
        elif dict_habit["type"] == "MONTHLY":
            periodicity = dict_habit["periodicity"]
            periodicity_parsed = list(map(int, periodicity))
            habits.append(MonthlyHabit(task, start_date, finish_date, periodicity_parsed, tracking_data, max_streak)) 
        elif dict_habit["type"] == "YEARLY":
            periodicity = dict_habit["periodicity"]
            periodicity_parsed = tuple(periodicity)
            habits.append(YearlyHabit(task, start_date, finish_date, periodicity_parsed, tracking_data, max_streak))   

    return habits

def save_data(habits: [Habit]):
    """Save habit data to a JSON file.

    Args:
        habits ([Habit]): A list of Habit objects to be saved.
    """
    
    with open('init.json', 'w') as f:
        json.dump(habits, f, cls=HabitEncoder, indent = 4)
    
