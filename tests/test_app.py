import pytest
from ..habitapp.analytics import get_tracked_habits
from ..habitapp.Habits import Habit

def test_get_tracked_habits():
    assert type(get_tracked_habits([])) == [Habit]

