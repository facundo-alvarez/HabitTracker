from datetime import date
from abc import ABC, abstractmethod
from Habits.habit import Habit
from Habits.dailyhabit import DailyHabit
from Habits.weeklyhabit import WeeklyHabit
from Habits.monthlyhabit import MonthlyHabit
from Habits.yearlyhabit import YearlyHabit
from Exceptions.DateArgumentException import DateArgumentException
import json

class HabitEncoder(json.JSONEncoder):
    """Custom JSON Encoder for Habit classes."""
    
    def default(self, obj):
        if isinstance(obj, DailyHabit):
            return self._encode_daily_habit(obj)
        elif isinstance(obj, WeeklyHabit):
            return self._encode_weekly_habit(obj)
        elif isinstance(obj, MonthlyHabit):
            return self._encode_monthly_habit(obj)  
        elif isinstance(obj, YearlyHabit):
            return self._encode_yearly_habit(obj)
            
    def _encode_daily_habit(self, obj:DailyHabit):
        data = {
            "type": obj.type.name,
            "task": obj.task,
            "start": obj.start.isoformat(),
            "finish": obj.finish.isoformat(),
            "periodicity": obj.periodicity,
            "trackData": [track_date.isoformat() for track_date in obj.track_data],
            "maxstreak": obj.max_streak
            }
        return json.dumps(data)
    
    def _encode_weekly_habit(self, obj:WeeklyHabit):
        data = {
            "type": obj.type.name,
            "task": obj.task,
            "start": obj.start.isoformat(),
            "finish": obj.finish.isoformat(),
            "periodicity": [periodicity.value for periodicity in obj.periodicity],
            "trackData": [track_date.isoformat() for track_date in obj.track_data],
            "maxstreak": obj.max_streak
            }
        return json.dumps(data)
    
    def _encode_monthly_habit(self, obj:MonthlyHabit):
        data = {
            "type": obj.type.name,
            "task": obj.task,
            "start": obj.start.isoformat(),
            "finish": obj.finish.isoformat(),
            "periodicity": [periodicity for periodicity in obj.periodicity],
            "trackData": [track_date.isoformat() for track_date in obj.track_data],
            "maxstreak": obj.max_streak
            }
        return json.dumps(data)
    
    def _encode_yearly_habit(self, obj:YearlyHabit):
        data = {
            "type": obj.type.name,
            "task": obj.task,
            "start": obj.start.isoformat(),
            "finish": obj.finish.isoformat(),
            "periodicity": obj.periodicity,
            "trackData": [track_date.isoformat() for track_date in obj.track_data],
            "maxstreak": obj.max_streak
            }
        return json.dumps(data)