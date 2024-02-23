from datetime import date, datetime
from Habits.habit import Habit
from Enums.dayofweek import DayOfWeek
from Enums.periodicity import Periodicity
import datetime
import calendar

class WeeklyHabit(Habit):
    """Represents a weekly habit, a subclass of Habit.

    Attributes:
        type (Periodicity): The periodicity type of the habit (WEEKLY).
        periodicity ([DayOfWeek]): List of days of the week when the habit is scheduled.
        
    """
    
    def __init__(self, task: str, start: date, finish: date, periodicity:[DayOfWeek], track_data:[datetime], max_streak:int) -> None:
        super().__init__(task, start, finish, track_data, max_streak)
        self.type = Periodicity.WEEKLY
        self.periodicity = periodicity

    def is_tracking(self, date:date) -> bool:
        """Check if the habit is being tracked on a specific date (override).

        Args:
            date (date): The date to check.

        Returns:
            bool: True if the habit is being tracked, False otherwise.
            
        """
        
        if not super().is_tracking(date):
            return False

        weekday_names =[day.upper() for day in calendar.day_name]

        return weekday_names[date.weekday()] in [day.value for day in self.periodicity]

    def get_streak(self) -> int:
        """Get the streak value for the habit (override)."""
        
        super().get_streak()
        
        streak = 0
        current_day = date.today()
        
        track_dates = {habit_date.date() for habit_date in self.track_data}
        
        if current_day in self.track_data:
            streak += 1
        
        while current_day >= self.start: 
            current_day = current_day - datetime.timedelta(days=1)
            
            if not int(current_day.weekday()) in [enum.value for enum in self.periodicity]:
                continue

            if current_day in track_dates:
                streak += 1
            else:
                self._set_max_streak(streak)
                return streak
        
        self._set_max_streak(streak)
        return streak
