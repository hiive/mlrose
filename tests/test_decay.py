"""Unit tests for decay.py"""

# Author: Genevieve Hayes
# Modified: Kyle Nakamura
# License: BSD 3 clause

try:
    import mlrose_hiive
except ImportError:
    import sys
    sys.path.append("..")

from mlrose_hiive import GeomDecay, ArithDecay, ExpDecay, CustomSchedule


def test_geom_above_min():
    """Test geometric decay evaluation function for case where result is above the minimum"""
    schedule = GeomDecay(init_temp=10, decay=0.95, min_temp=1)
    x = schedule.evaluate(5)
    assert round(x, 5) == 7.73781


def test_geom_below_min():
    """Test geometric decay evaluation function for case where result is below the minimum"""
    schedule = GeomDecay(init_temp=10, decay=0.95, min_temp=1)
    x = schedule.evaluate(50)
    assert x == 1


def test_arith_above_min():
    """Test arithmetic decay evaluation function for case where result is above the minimum"""
    schedule = ArithDecay(init_temp=10, decay=0.95, min_temp=1)
    x = schedule.evaluate(5)
    assert x == 5.25


def test_arith_below_min():
    """Test arithmetic decay evaluation function for case where result is below the minimum"""
    schedule = ArithDecay(init_temp=10, decay=0.95, min_temp=1)
    x = schedule.evaluate(50)
    assert x == 1


def test_exp_above_min():
    """Test exponential decay evaluation function for case where result is above the minimum"""
    schedule = ExpDecay(init_temp=10, exp_const=0.05, min_temp=1)
    x = schedule.evaluate(5)
    assert round(x, 5) == 7.78801


def test_exp_below_min():
    """Test exponential decay evaluation function for case where result is below the minimum"""
    schedule = ExpDecay(init_temp=10, exp_const=0.05, min_temp=1)
    x = schedule.evaluate(50)
    assert x == 1


def test_custom():
    """Test custom evaluation function"""
    def custom_schedule(t, c):
        return t + c
    kwargs = {'c': 10}
    schedule = CustomSchedule(custom_schedule, **kwargs)
    x = schedule.evaluate(5)
    assert x == 15
