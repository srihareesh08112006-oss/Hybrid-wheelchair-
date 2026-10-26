def compute_assist(torque, speed, battery_pct, current,
                   ratio=0.5, max_speed=6.0, low_batt=20, max_current=15):
    """Return (assist_command, state)."""
    if current > max_current:
        return 0.0, "fault"
    if torque <= 0 or speed >= max_speed:
        return 0.0, "assist"
    assist = torque * ratio
    if battery_pct < low_batt:
        assist *= battery_pct / low_batt * 0.5
    return assist, "assist"
