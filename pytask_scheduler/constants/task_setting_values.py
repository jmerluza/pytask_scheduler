from dataclasses import dataclass

@dataclass
class TaskInstancePolicy:
    """
    Sets the policy that defines how task scheduler deals with multiple instances of the task.
    https://learn.microsoft.com/en-us/windows/win32/taskschd/tasksettings-multipleinstances
    """
    TASK_INSTANCES_PARALLEL = 0
    TASK_INSTANCES_QUEUE = 1
    TASK_INSTANCES_IGNORE_NEW = 2
    TASK_INSTANCES_STOP_EXISTING = 3

@dataclass
class TaskRestartIntervals:
    """
    Sets a value that specifies how long the task scheduler will attempt to restart the task.
    https://learn.microsoft.com/en-us/windows/win32/taskschd/tasksettings-restartinterval
    """
    intervals = {
        "1 minute":"PT1M",
        "5 minutes":"PT5M",
        "10 minutes":"PT10M",
        "15 minutes":"PT15M",
        "30 minutes":"PT30M",
        "1 hour":"PT1H",
        "2 hours":"PT2H"
    }

@dataclass
class TaskExecutionLimit:
    """
    Sets a value that specifies the amount of time that is allowed to complete the task.\
    by default, a task will be stopped 72 hours after it starts to run.
    https://learn.microsoft.com/en-us/windows/win32/taskschd/tasksettings-restartinterval
    """
    limits = {
        "1 hour":"PT1H",
        "2 hours":"PT2H",
        "4 hours":"PT4H",
        "6 hours":"PT6H",
        "8 hours":"PT8H",
        "12 hours":"PT12H",
        "1 day":"PT1D",
        "3 days":"PT3D",
    }
