from Habits.habit import Habit
from datetime import date, datetime
from Enums.periodicity import Periodicity
import datetime


class YearlyHabit(Habit):
    """Represents a yearly habit, a subclass of Habit.

    Attributes:
        type (Periodicity): The periodicity type of the habit (YEARLY).
        periodicity ((int, int)): Tuple representing day and month when the habit is scheduled.
        
    """
    
    def __init__(self, task:str, start:date, finish:date, periodicity:(int, int), track_data:[datetime], max_streak:int) -> None:
        super().__init__(task, start, finish, track_data, max_streak)
        self.type = Periodicity.YEARLY
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
        
        return (date.day, date.month) == self.periodicity


    def get_streak(self) -> int:
        """Get the streak value for the habit (override)."""
        
        super().get_streak()
        
        streak = 0
        current_day = date.today()
        
        track_dates = {habit_date.date() for habit_date in self.track_data}
        
        if current_day in track_dates:
            streak += 1
        
        while current_day >= self.start: 
            current_day = current_day - datetime.timedelta(days=1)
            
            if (current_day.day, current_day.month) != self.periodicity:
                continue

            if current_day in track_dates:
                streak += 1
            else:
                self._set_max_streak(streak)
                return streak
        
        self._set_max_streak(streak)
        return streak