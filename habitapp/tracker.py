from datetime import date
from Enums.dayofweek import DayOfWeek
from Habits.dailyhabit import DailyHabit
from Habits.weeklyhabit import WeeklyHabit
from Habits.monthlyhabit import MonthlyHabit
from Habits.yearlyhabit import YearlyHabit
from Habits.habit import Habit
import string

class Tracker(object):
    """Tracks and manages habits for a specified period.

    Attributes:
        habits (List[Habit]): List of habits being tracked.
        
    """
    
    def __init__(self, habits_data:[Habit]) -> None:
        """Initialize the Tracker with a list of habits.

        Args:
            habits_data (List[Habit]): List of habits to initialize the tracker.
            
        """
        
        self.habits:[Habit] = habits_data

    def add_daily_habit(self, task:string, start:date, finish:date) -> None:
        """Add a new daily habit to the tracker.

        Args:
            task (str): Description of the habit.
            start (date): Start date for tracking the habit.
            finish (date): Finish date for tracking the habit.

        Raises:
            Exception: If the finish date is before the start date.
            
        """
        
        if finish < start:
            raise Exception("Finish date can't be before start date")
        
        self.habits.append(DailyHabit(task, start, finish, [], 0))

    def add_weekly_habit(self, task:string, start:date, finish:date, days_of_week:[DayOfWeek]) -> None:
        """Add a new weekly habit to the tracker.

        Args:
            task (str): Description of the habit.
            start (date): Start date for tracking the habit.
            finish (date): Finish date for tracking the habit.
            days_of_week (List[DayOfWeek]): Days of the week when the habit is scheduled.
            
        """
        
        self.habits.append(WeeklyHabit(task, start, finish, days_of_week, [], 0))

    def add_monthly_habit(self, task:string, start:date, finish:date, days:[int]) -> None:
        """Add a new monthly habit to the tracker.

        Args:
            task (str): Description of the habit.
            start (date): Start date for tracking the habit.
            finish (date): Finish date for tracking the habit.
            days (List[int]): Days of the month when the habit is scheduled.
            
        """
        
        self.habits.append(MonthlyHabit(task, start, finish, days, [], 0))

    def add_yearly_habit(self, task:string, start:date, finish:date, dates:[(int,int)]) -> None:
        """Add a new yearly habit to the tracker.

        Args:
        
            task (str): Description of the habit.
            start (date): Start date for tracking the habit.
            finish (date): Finish date for tracking the habit.
            dates (List[(int, int)]): Specific dates day and month when the habit is scheduled.
            
        """
        
        self.habits.append(YearlyHabit(task, start, finish, dates, [], 0))

    def remove_habit(self, habit:Habit) -> None:
        """Remove a habit from the tracker.

        Args:
            habit (Habit): The habit to be removed.
            
        """
        
        self.habits.remove(habit)

    def get_date_habits(self, date:date) -> [Habit]:
        """Get habits scheduled for a specific date.

        Args:
            date (date): The date to check.

        Returns:
            List[Habit]: List of habits scheduled for the specified date.
            
        """
        
        return [habit for habit in self.habits if habit.is_tracking(date)]
   