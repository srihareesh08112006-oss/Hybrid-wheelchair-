import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "software"))
from control import compute_assist

def test_no_push():
    assert compute_assist(0, 1, 90, 0)[0] == 0

def test_normal_assist():
    assert compute_assist(4, 1, 90, 2)[0] == 2

def test_speed_limit():
    assert compute_assist(5, 6.0, 90, 2)[0] == 0

def test_low_battery_reduces():
    assert compute_assist(4, 1, 10, 2)[0] < 2

def test_overcurrent_fault():
    assert compute_assist(4, 1, 90, 16) == (0.0, "fault")
