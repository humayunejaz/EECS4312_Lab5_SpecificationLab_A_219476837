from typing import List, Dict, Tuple


def _to_minutes(t: str) -> int:
    """Convert 'HH:MM' -> minutes since midnight."""
    h, m = t.split(":")
    return int(h) * 60 + int(m)


def _to_hhmm(minutes: int) -> str:
    """Convert minutes since midnight -> 'HH:MM'."""
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"


def _overlaps(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    """
    Return True if half-open intervals [a_start, a_end) and [b_start, b_end) overlap.
    Boundaries touching is NOT overlap.
    """
    return a_start < b_end and b_start < a_end


def suggest_slots(
    events: List[Dict[str, str]],
    meeting_duration: int,
    day: str
) -> List[str]:
    """
    Suggest possible meeting start times for a given day.

    Args:
        events: List of dicts with keys {"start": "HH:MM", "end": "HH:MM"}
        meeting_duration: Desired meeting length in minutes
        day: Day string (tests pass a date like "2026-02-01"; not needed for logic here)

    Returns:
        List of valid start times as "HH:MM" sorted ascending
    """

    # Based on tests/constraints:
    WORK_START = _to_minutes("09:00")
    WORK_END = _to_minutes("17:00")
    LUNCH_START = _to_minutes("12:00")
    LUNCH_END = _to_minutes("13:00")

    # Slot granularity (tests require 15-minute increments)
    STEP = 15

    # Buffer after each event ends (tests require 15-minute buffer)
    BUFFER_AFTER_EVENT = 15

    # Build busy intervals (events within working hours) + lunch
    busy: List[Tuple[int, int]] = []

    for e in events:
        s = _to_minutes(e["start"])
        en = _to_minutes(e["end"])

        # Ignore events completely outside working hours
        if en <= WORK_START or s >= WORK_END:
            continue

        # Clamp start to working hours
        s = max(s, WORK_START)

        # Add 15-min buffer after event ends, then clamp to working hours
        en = min(en + BUFFER_AFTER_EVENT, WORK_END)

        if s < en:
            busy.append((s, en))

    # Lunch break always blocks meetings (no extra buffer mentioned by tests)
    busy.append((LUNCH_START, LUNCH_END))

    # Sort for cleanliness
    busy.sort()

    slots: List[str] = []
    latest_start = WORK_END - meeting_duration

    start = WORK_START
    while start <= latest_start:
        end = start + meeting_duration

        conflict = False
        for bs, be in busy:
            if _overlaps(start, end, bs, be):
                conflict = True
                break

        if not conflict:
            slots.append(_to_hhmm(start))

        start += STEP

    return slots
