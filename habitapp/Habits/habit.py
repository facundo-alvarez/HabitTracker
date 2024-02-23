from datetime import date, datetime
from abc import ABC, abstractmethod
from Exceptions.DateArgumentException import DateArgumentException

class Habit(ABC):
    """Abstract base class for defining habits.

    Attributes:
        task (str): The description of the habit.
        start (date): The start date for tracking the habit.
        finish (date): The finish date for tracking the habit.
        track_data ([datetime]): List of datetimes when the habit is tracked.
        max_streak (int): The maximum streak value for the habit.
    """
    
    def __init__(self, task:str, start:date, finish:date, track_data:[datetime], max_streak:int) -> None:
        self.type = None
        self.task = task
        self.start = start
        self.finish = finish
        self.periodicity = []
        self.track_data = track_data
        self.max_streak = max_streak
    
    def __str__(self) -> str:
        """String representation of the habit."""
        
        return self.task

    @abstractmethod
    def is_tracking(self, date:date) -> bool:
        """Check if the habit is being tracked on a specific date.

        Args:
            date (date): The date to check.

        Returns:
            bool: True if the habit is being tracked, False otherwise.
            
        """
        return date >= self.start and date <= self.finish
    
    @abstractmethod
    def get_streak(self) -> int:
        """Get the streak value for the habit.

        Raises:
            Exception: If the habit is not being tracked on the current date.

        Returns:
            int: The streak value for the habit.
            
        """
        
        if date.today() < self.start or date.today() > self.finish:
            raise Exception("Can't calculate streak on not traked habit")

    def mark_done(self, date:date) -> None:
        """Mark the habit as done on a specific date.

        Args:
            date (date): The date when the habit is marked as done.

        Raises:
            DateArgumentException: If the habit is not being tracked on the given date.
            Exception: If the habit is already marked as done on the given date.
            
        """
        
        if not self.is_tracking(date):
            raise DateArgumentException("Habit is not on the date")

        found = False
        for habit_date in self.track_data:
            if habit_date.date() == date:
                found = True
                break

        if found:
            raise Exception("Habit already marked as done")
        
        current_datetime = datetime.now()
        combined_datetime = datetime.combine(date, current_datetime.time())

        self.track_data.append(combined_datetime)
        
    def mark_undone(self, date:date) -> None:
        """Mark the habit as undone on a specific date.

        Args:
            date (date): The date when the habit is marked as undone.

        Raises:
            DateArgumentException: If the habit is not being tracked on the given date.
            Exception: If the habit is not marked as done on the given date.
            
        """
        
        if not self.is_tracking(date):
            raise DateArgumentException("Habit is not on the date")

        found = False
        for habit_date in self.track_data:
            if habit_date.date() == date:
                self.track_data.remove(habit_date)
                found = True
                break

        if not found:
            raise Exception("Habit is not marked as done")

    def _set_max_streak(self, streak:int) -> None:
        """Set the maximum streak value for the habit.

        Args:
            streak (int): The streak value to set.

        Raises:
            None
            
        """
        
        if streak > self.max_streak:
            self.max_streak = streak
            