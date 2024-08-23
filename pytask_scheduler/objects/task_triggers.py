"""This module covers topics from the Trigger scripting objects.
https://learn.microsoft.com/en-us/windows/win32/taskschd/trigger
"""
from typing import Literal
from datetime import datetime
from pytask_scheduler import TaskTriggerTypes

class TaskTrigger:
    def __init__(self, taskdef_obj):
        self.taskdef = taskdef_obj
        self.trigger = self.taskdef.Triggers

    def __set_start_boundary(self, start_date: datetime.date, start_time: datetime.time):
        self.trigger.StartBoundary = datetime.combine(start_date, start_time).isoformat()

    def __set_cadence(self, trigger_type: int):
        self.trigger.Create(trigger_type)

    def create_daily_trigger(
        self,
        start_date: datetime.date,
        start_time: datetime.time,
        days_interval: int
    ):
        """Starts a task based on a daily schedule. 
        https://learn.microsoft.com/en-us/windows/win32/taskschd/dailytrigger
        
        Parameters:
            start_date (`datetime.date`): Date when the trigger is activated.
            start_time (`datetime.time`): Time when the trigger is activated.
            days_interval (`int`): Sets the interval between the days in the schedule. \
                An interval of 1 produces a daily schedule, an interval of 2 produces an \
                every-other day schedule.
        """
        self.__set_cadence(TaskTriggerTypes.TASK_TRIGGER_DAILY)
        self.__set_start_boundary(start_date, start_time)
        self.trigger.DaysInterval = days_interval
        return self.taskdef

    def create_weekly_trigger(
        self,
        start_date: datetime.date,
        start_time: datetime.time,
        weeks_interval: int,
        days_of_week: int
    ):
        """Starts a task based on a weekly schedule. For example, the task starts at 8:00 AM \
            on a specific day of the week every week or every other week.
            https://learn.microsoft.com/en-us/windows/win32/taskschd/weeklytrigger

        Parameters:
            start_date (`datetime.date`): Date when the trigger is activated.
            start_time (`datetime.time`): Time when the trigger is activated.
            weeks_interval (`int`): Sets the interval between the weeks in the schedule. \
                An interval of 1 produces a weekly schedule, an interval of 2 produces an \
                every-other week schedule.
        """
        self.__set_cadence(TaskTriggerTypes.TASK_TRIGGER_WEEKLY)
        self.__set_start_boundary(start_date, start_time)
        self.trigger.WeeksInterval = weeks_interval
        self.trigger.DaysOfWeek = days_of_week
        return self.taskdef

    def create_monthly_trigger(
        self,
        trigger_type: Literal["month","dow"],
        start_date: datetime.date,
        start_time: datetime.time,
        days_of_month: int,
        days_of_week: int,
        months_of_year: int,
        weeks_of_month: int
    ):
        """Starts a task based on a monthly schedule or a monthly day-of-week schedule.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/monthlytrigger
        
        Parameters:
            trigger_type (`Literal['month', 'dow']`): Type of monthly trigger.
            start_date (`datetime.date`): Date when the trigger is activated.
            start_time (`datetime.time`): Time when the trigger is activated.
            days_of_month (`int`): Sets the days of the month during which the task runs.
            days_of_week (`int`): Sets the days of the week during which the task runs. 
            months_of_year (`int`): Sets the months of the year during which the task runs.
            weeks_of_month (`int`): Sets the weeks of the month during which the task runs.
        
        Examples:
            The `month` trigger type can start a task on a specific day of specific months.
            The `dow` trigger type can start a task every first Thursday of specific months.
        
        """
        self.__set_start_boundary(start_date, start_time)
        match trigger_type:
            case "month":
                self.__set_cadence(TaskTriggerTypes.TASK_TRIGGER_MONTHLY)
                self.trigger.DaysOfMonth = days_of_month
                self.trigger.MonthsOfYear = months_of_year
            case "dow":
                self.__set_cadence(TaskTriggerTypes.TASK_TRIGGER_MONTHLYDOW)
                self.trigger.DaysOfWeek = days_of_week
                self.trigger.MonthsOfYear = months_of_year
                self.trigger.WeeksOfMonth = weeks_of_month
        return self.taskdef

    def create_one_time_trigger(
        self,
        start_date: datetime.date,
        start_time: datetime.time
    ):
        """Starts a task at as specific date and time.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/timetrigger

        Parameters:
            start_date (`datetime.date`): Date when the trigger is activated.
            start_time (`datetime.time`): Time when the trigger is activated.
        """
        self.__set_cadence(TaskTriggerTypes.TASK_TRIGGER_TIME)
        self.__set_start_boundary(start_date, start_time)
        return self.taskdef
