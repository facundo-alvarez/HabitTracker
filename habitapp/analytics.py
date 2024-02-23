from datetime import date
from Habits.habit import Habit
from Enums.periodicity import Periodicity

def get_tracked_habits(habits:[Habit]) -> [Habit]:
    """Filter habits that are currently being tracked.

    Args:
        habits (List[Habit]): List of habits to filter.

    Returns:
        List[Habit]: List of habits that are currently being tracked.
        
    """
    
    return [habit for habit in habits if habit.start <= date.today() and habit.finish >= date.today()]

def get_habits_by_period(periodicity:Periodicity, habits:[Habit]) -> [Habit]:
    """Filter habits based on their periodicity type.

    Args:
        periodicity (Periodicity): The periodicity type to filter habits.
        habits (List[Habit]): List of habits to filter.

    Returns:
        List[Habit]: List of habits with the specified periodicity type.
        
    """
    
    return [habit for habit in habits if habit.type == periodicity]

def get_longest_streak(habits:[Habit]) -> int:
    """Get the longest streak value among currently tracked habits.

    Args:
        habits (List[Habit]): List of habits.

    Returns:
        int: The current longest streak value among currently tracked habits.
        
    """
    
    return max([(traked_habits.get_streak()) for traked_habits in get_tracked_habits(habits)])

def get_longest_run_streak(habit:Habit) -> int:
    """Get the longest run streak for a given habit.

    Args:
        habits (Habit): Habit to check.

    Returns:
        int: The longest run streak value for a given habit.
        
    """
    historic_streak = habit.max_streak
    current_streak = habit.get_streak()

    return max([historic_streak, current_streak])