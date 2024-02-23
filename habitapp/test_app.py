import pytest
import dataio
import json 
from analytics import *
from Habits.habit import Habit
from datetime import date, datetime


### Analytics module TESTS

@pytest.fixture
def get_traker_data() -> [Habit]:
    return dataio.load_data()
    
def test_get_tracked_habits(get_traker_data):
    assert len(get_tracked_habits(get_traker_data)) == 5 
    
def test_get_tracked_habits_return():
    assert all(isinstance(habit, Habit) for habit in get_tracked_habits([]))
    
def test_get_habits_by_period(get_traker_data):
    assert len(get_habits_by_period(Periodicity.DAILY, get_traker_data)) == 1
    
def test_get_longest_streak(get_traker_data):
    assert get_longest_streak(get_traker_data) == 6 #This can fail due to not checking on time the streak

def test_get_longest_run_streak(get_traker_data):
    assert get_longest_run_streak(get_traker_data[0]) == 3 #This can fail due to not checking on time the streak





### Analytics module TESTS

# Sample data
task = "Exercise"
start_date = date(2023, 1, 1)
finish_date = date(2023, 1, 7)
track_data = [datetime(2023, 1, 1), datetime(2023, 1, 3)]
max_streak = 5

# Mock Habit subclass
class MockHabit(Habit):
    def __init__(self, task, start, finish, track_data, max_streak):
        super().__init__(task, start, finish, track_data, max_streak)

    def is_tracking(self, date: date) -> bool:
        return date >= self.start and date <= self.finish

    def get_streak(self) -> int:
        return len(self.track_data)


# Test Habit class methods
def test_is_tracking():
    habit = MockHabit(task, start_date, finish_date, track_data, max_streak)
    assert habit.is_tracking(date(2023, 1, 1)) == True
    assert habit.is_tracking(date(2023, 1, 8)) == False

def test_get_streak():
    habit = MockHabit(task, start_date, finish_date, track_data, max_streak)
    assert habit.get_streak() == 2

def test_mark_done():
    habit = MockHabit(task, start_date, finish_date, track_data, max_streak)
    habit.mark_done(date(2023, 1, 5))
    assert len(habit.track_data) == 3

def test_mark_undone():
    habit = MockHabit(task, start_date, finish_date, track_data, max_streak)
    habit.mark_undone(date(2023, 1, 5))
    assert len(habit.track_data) == 2