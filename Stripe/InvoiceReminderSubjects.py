# Stage 1, compute send dates from a schedule

# Goal
# Given an invoice issue date and a schedule of offsets, compute the send date for each reminder.

# Function
# schedule_to_dates(issue_date: str, schedule: list) -> list[tuple[date, any]]

# Rules

# issue_date is YYYY-MM-DD.

# Each schedule entry is either an integer day offset or the string due.

# An integer offset k means send on issue_date + k days. Negative means before issue day. Zero means on the issue day.

# due means thirty days after the issue day.

# Examples

# Issue date 2025-09-01, schedule [-10, 0, 20, "due"] yields dates 2025-08-22, 2025-09-01, 2025-09-21, 2025-10-01.

# Issue date 2024-02-28, schedule [1] yields 2024-02-29 in a leap year.

# You may ask

# Should due be configurable

# Are time zones relevant or is this date only

# Stage 2, generate subjects for each entry

# Goal
# Create the subject line for each schedule item.

# Function
# subjects_for_schedule(issue_date: str, schedule: list) -> list[tuple[date, str]]

# Subject rules

# Offset less than zero, Invoice reminder, X days before issue.

# Offset equals zero, Invoice issued.

# Offset greater than zero, Invoice reminder, X days after issue.

# due, Invoice due.

# Examples

# Issue date 2025-09-01, schedule [-10, 0, 20, "due"] produces

# Invoice reminder, 10 days before issue

# Invoice issued

# Invoice reminder, 20 days after issue

# Invoice due

# Stage 3, sort and return subjects

# Goal
# Return subjects in send order.

# Function
# sorted_subjects(issue_date: str, schedule: list) -> list[str]

# Rules

# Sort by the computed send date ascending.

# If two entries share the same date, keep the input order.

# Use any stable sort that your language provides.

# Examples

# Issue date 2025-09-01, schedule [0, -3, "due", 7] returns
# ['Invoice reminder, 3 days before issue', 'Invoice issued', 'Invoice reminder, 7 days after issue', 'Invoice due']

# Stage 4, API shape and tests

# Goal
# Wrap this into a single call. List the tests you would run.

# Function
# build_invoice_subjects(issue_date: str, schedule: list) -> list[str] | { "error": str }


from datetime import datetime, timedelta, date
from typing import List, Tuple, Union, Dict, Any

# ========== Stage 1, compute send dates from a schedule ==========

def schedule_to_dates(issue_date: str, schedule: List[Union[int, str]]) -> Union[List[Tuple[date, Any]], Dict[str, str]]:
    """
    issue_date format YYYY-MM-DD
    schedule entries are integers or 'due'
    returns list of (send_date, original_entry) in input order
    """
    try:
        base = datetime.strptime(issue_date, "%Y-%m-%d").date()
    except ValueError:
        return {"error": "invalid date"}

    out: List[Tuple[date, Any]] = []
    for entry in schedule:
        if isinstance(entry, int):
            out.append((base + timedelta(days=entry), entry))
        elif isinstance(entry, str) and entry.lower() == "due":
            out.append((base + timedelta(days=30), "due"))
        else:
            return {"error": "invalid schedule entry"}
    return out


# ========== Stage 2, generate subjects for each entry ==========

def subjects_for_schedule(issue_date: str, schedule: List[Union[int, str]]) -> Union[List[Tuple[date, str]], Dict[str, str]]:
    dates = schedule_to_dates(issue_date, schedule)
    if isinstance(dates, dict):
        return dates

    subjects: List[Tuple[date, str]] = []
    for send_date, entry in dates:
        if entry == "due":
            subj = "Invoice due"
        elif isinstance(entry, int):
            if entry < 0:
                subj = f"Invoice reminder, {abs(entry)} days before issue"
            elif entry == 0:
                subj = "Invoice issued"
            else:
                subj = f"Invoice reminder, {entry} days after issue"
        else:
            return {"error": "invalid schedule entry"}
        subjects.append((send_date, subj))
    return subjects


# ========== Stage 3, sort and return subjects ==========

def sorted_subjects(issue_date: str, schedule: List[Union[int, str]]) -> Union[List[str], Dict[str, str]]:
    items = subjects_for_schedule(issue_date, schedule)
    if isinstance(items, dict):
        return items
    # Python sort is stable, ties keep input order
    items.sort(key=lambda x: x[0])
    return [subj for _, subj in items]


# ========== Stage 4, API shape ==========

def build_invoice_subjects(issue_date: str, schedule: List[Union[int, str]]) -> Union[List[str], Dict[str, str]]:
    """
    Validates input, returns subjects sorted by send date, or an error object
    """
    if not isinstance(schedule, list):
        return {"error": "schedule must be a list"}
    return sorted_subjects(issue_date, schedule)



# ========== Print checks ==========

# Stage 1
print("S1 dates basic:",
      [d.isoformat() for d, _ in schedule_to_dates("2025-09-01", [-10, 0, 20, "due"])],
      "expected ['2025-08-22', '2025-09-01', '2025-09-21', '2025-10-01']")

print("S1 leap year add one day:",
      [d.isoformat() for d, _ in schedule_to_dates("2024-02-28", [1])],
      "expected ['2024-02-29']")

print("S1 invalid entry:",
      schedule_to_dates("2025-09-01", ["soon"]),
      "expected {'error': 'invalid schedule entry'}")

print("S1 invalid date:",
      schedule_to_dates("2025-02-30", [0]),
      "expected {'error': 'invalid date'}")

# Stage 2
print("S2 subjects basic:",
      [s for _, s in subjects_for_schedule("2025-09-01", [-10, 0, 20, "due"])],
      "expected ['Invoice reminder, 10 days before issue', 'Invoice issued', 'Invoice reminder, 20 days after issue', 'Invoice due']")

# Stage 3
print("S3 sorted subjects:",
      sorted_subjects("2025-09-01", [0, -3, "due", 7]),
      "expected ['Invoice reminder, 3 days before issue', 'Invoice issued', 'Invoice reminder, 7 days after issue', 'Invoice due']")

print("S3 stable tie order kept:",
      sorted_subjects("2025-09-01", [0, 0, 0]),
      "expected ['Invoice issued', 'Invoice issued', 'Invoice issued']")

# Stage 4
print("S4 API ok:",
      build_invoice_subjects("2025-09-01", [-10, 0, 20, "due"]),
      "expected ['Invoice reminder, 10 days before issue', 'Invoice issued', 'Invoice reminder, 20 days after issue', 'Invoice due']")

print("S4 API bad schedule type:",
      build_invoice_subjects("2025-09-01", "not a list"),
      "expected {'error': 'schedule must be a list'}")
