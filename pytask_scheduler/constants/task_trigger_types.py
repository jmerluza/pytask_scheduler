"""This module covers the trigger type values.
https://learn.microsoft.com/en-us/windows/win32/taskschd/triggercollection-create
"""
from dataclasses import dataclass

@dataclass
class TaskTriggerTypes:
    """For creating a new trigger for a new task.
    
    Attributes:
        `TASK_TRIGGER_EVENT`: Triggers the task when a specific event occurs.
        `TASK_TRIGGER_TIME`: Triggers the task at a specific time of day.
        `TASK_TRIGGER_DAILY`: Triggers the task on a daily schedule. For example, the task starts \
            at a specific time every day, every-other day, every third day, and so on.
        `TASK_TRIGGER_WEEKLY`: Triggers the task on a weekly schedule. For example, the task \
            starts at 8:00 AM on a specific day every week or other week.
        `TASK_TRIGGER_MONTHLY`: Triggers the task on a monthly schedule. For example, the task \
            starts on specific days of specific months.
        `TASK_TRIGGER_MONTHLYDOW`: Triggers the task on a monthly day-of-week schedule. For \
            example, the task starts on a specific days of the week, weeks of the month, and \
                months of the year.
        `TASK_TRIGGER_IDLE`: Triggers the task when the computer goes into an idle state.
        `TASK_TRIGGER_REGISTRATION`: Triggers the task when the task is registered.
        `TASK_TRIGGER_BOOT`: Triggers the task when the computer boots.
        `TASK_TRIGGER_LOGON`: Triggers the task when a specific user logs on.
        `TASK_TRIGGER_SESSION_STATE_CHANGE`: Triggers the task when a specific \
            session state changes.
    """
    # TASK_TRIGGER_EVENT = 0
    TASK_TRIGGER_TIME = 1
    TASK_TRIGGER_DAILY = 2
    TASK_TRIGGER_WEEKLY = 3
    TASK_TRIGGER_MONTHLY = 4
    TASK_TRIGGER_MONTHLYDOW = 5
    # TASK_TRIGGER_IDLE = 6
    # TASK_TRIGGER_REGISTRATION = 7
    # TASK_TRIGGER_BOOT = 8
    # TASK_TRIGGER_LOGON = 9
    # TASK_TRIGGER_SESSION_STATE_CHANGE = 11