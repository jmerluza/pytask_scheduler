from dataclasses import dataclass

@dataclass
class MonthlyTriggerValues:
    DAYS_OF_MONTH = {
        1:1,
        2:2,
        3:4,
        4:8,
        5:16,
        6:32,
        7:64,
        8:128,
        9:256,
        10:512,
        11:1024,
        12:2048,
        13:4096,
        14:8192,
        15:16384,
        16:32768,
        17:65536,
        18:131072,
        19:262144,
        20:524288,
        21:1048576,
        22:2097152,
        23:4194304,
        24:8388608,
        25:16777216,
        26:33554432,
        27:67108864,
        28:134217728,
        29:268435456,
        30:536870912,
        31:1073741824,
        "Last":2147483648
    }

    MONTHS_OF_YEAR = {
        "January":1,
        "February":2,
        "March":4,
        "April":8,
        "May":16,
        "June":32,
        "July":64,
        "August":128,
        "September":256,
        "October":512,
        "November":1024,
        "December":2048
    }

    DAYS_OF_WEEK = {
        "Sunday":1,
        "Monday":2,
        "Tuesday":4,
        "Wednesday":8,
        "Thursday":16,
        "Friday":32,
        "Saturday":64
    }

    WEEKS_OF_MONTH = {
        "First week of the month":1,
        "Second week of the month":2,
        "Third week of the month":4,
        "Fourth week of the month":8
    }

@dataclass
class TaskActionTypes:
    """
    Task action types. API reference can be found here: 
    https://learn.microsoft.com/en-us/windows/win32/taskschd/action-type

    Attributes:
        TASK_ACTION_EXEC:
            This action performs a command-line operation. For example, the action could run a 
            script, launch an executable, or, if the name of a document is provided, find its 
            associated application and launch the application with the document.
        TASK_ACTION_COM_HANDLER:
            This action fires a handler.
        TASK_ACTION_SEND_EMAIL:
            This action sends an email message.
        TASK_ACTION_SHOW_MESSAGE:
            This action shows a message box.
                        
    """
    TASK_ACTION_EXEC = 0
    TASK_ACTION_COM_HANDLER = 5
    TASK_ACTION_SEND_EMAIL = 6
    TASK_ACTION_SHOW_MESSAGE = 7

@dataclass
class TaskCreationTypes:
    """
    Task logon types. API reference can be found here:
    https://learn.microsoft.com/en-us/windows/win32/taskschd/taskfolder-registertask

    Attributes:
        TASK_VALIDATE_ONLY:
            The Task Scheduler checks the syntax of the XML that describes the task but does not \
            register the task. This constant cannot be combined with the TASK_CREATE, \
            TASK_UPDATE, or TASK_CREATE_OR_UPDATE value

        TASK_CREATE:
            The Task Scheduler registers the task as a new task.

        TASK_UPDATE:
            The Task Scheduler registers the task as an updated version of an existing task. When \
            a task with a registration trigger is updated, the task will \
            execute after the update occurs.

        TASK_CREATE_OR_UPDATE:
            The Task Scheduler either registers the task as a new task or as an updated version \
            if the task already exists. Equivalent to TASK_CREATE | TASK_UPDATE.
        
        TASK_DISABLE:
            The Task Scheduler disables the existing task.

        TASK_DONT_ADD_PRINCIPAL_ACE:
            The Task Scheduler is prevented from adding the allow access-control entry (ACE) \
            for the context principal. When the TaskFolder.RegisterTask function is called with \
            this flag to update a task, the Task Scheduler service does not add the ACE for the \
            new context principal and does not remove the ACE from the old context principal.

        TASK_IGNORE_REGISTRATION_TRIGGERS:
            The Task Scheduler creates the task, but ignores the registration triggers in the \
            task. By ignoring the registration triggers, the task will not execute when it is \
            registered unless a time-based trigger causes it to execute on registration.
    """
    TASK_VALIDATE_ONLY = 1
    TASK_CREATE = 2
    TASK_UPDATE = 4
    TASK_CREATE_OR_UPDATE = 6
    TASK_DISABLE = 8
    TASK_DONT_ADD_PRINCIPAL_ACE = 16
    TASK_IGNORE_REGISTRATION_TRIGGERS = 32

@dataclass
class TaskLogonTypes:
    """
    Task logon types. API reference can be found here:
    https://learn.microsoft.com/en-us/windows/win32/taskschd/taskfolder-registertask

    Attributes:
        TASK_LOGON_NONE:
            The logon method is not specified. Used for non-NT credentials.

        TASK_LOGON_PASSWORD:
            Use a password for logging on the user. The password must be supplied at \
            registration time.

        TASK_LOGON_S4U:
            Use an existing interactive token to run a task. The user must log on \
            using a service for user (S4U) logon. When an S4U logon is used, no \
            password is stored by the system and there is no access to either the \
            network or to encrypted files.

        TASK_LOGON_INTERACTIVE_TOKEN:
            User must already be logged on. The task will be run only in an \
            existing interactive session.

        TASK_LOGON_GROUP:
            Group activation. The groupId field specifies the group.

        TASK_LOGON_SEVICE_ACCOUNT:
            Indicates that a Local System, Local Service, or Network Service \
            account is being used as a security context to run the task.

        TASK_LOGON_INTERACTIVE_TOKEN_OR_PASSWORD
            First use the interactive token. If the user is not logged on \
            (no interactive token is available), then the password is used. The password must be \
            specified when a task is registered. This flag is not recommended for new tasks \
            because it is less reliable than TASK_LOGON_PASSWORD.
    """
    TASK_LOGON_NONE = 0
    TASK_LOGON_PASSWORD = 1
    TASK_LOGON_S4U = 2
    TASK_LOGON_INTERACTIVE_TOKEN = 3
    TASK_LOGON_GROUP = 4
    TASK_LOGON_SERVICE_ACCOUNT = 5
    TASK_LOGON_INTERACTIVE_TOKEN_OR_PASSWORD = 6

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
