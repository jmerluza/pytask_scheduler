from dataclasses import dataclass

@dataclass
class TaskValueDefinitions:
    """Value definitions for task statistics"""
    TASK_RESULT_DEFINITION = {
        0:"Operation completed successfully.",
        1:"General failure.",
        2:"The system cannot find the file specified.",
        10:"System environment failure.",
        267011:"The task has not yet run.",
        2147750687:"Task scheduler is not available.",
        2147943645:"The device is not ready.",
        267009:"Task is currently running."
    }

    TASK_STATE_DEFINITION = {
        0:"UNKNOWN",
        1:"DISABLED",
        2:"QUEUED",
        3:"READY",
        4:"RUNNING"
    }


