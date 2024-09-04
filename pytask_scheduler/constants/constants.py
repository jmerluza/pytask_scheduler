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
    policies = {
        "Parallel":0,
        "Queue":1,
        "Ignore New":2,
        "Stop Existing Instance":3
    }
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

@dataclass
class EventLogType:
    """Task scheduler event level type descriptions.
    https://learn.microsoft.com/en-us/windows/win32/eventlog/event-types
    """
    DESCRIPTIONS = {
        2: "ERROR",
        3: "WARNING",
        4: "INFORMATION"
    }

@dataclass
class EventIDs:
    """Task scheduler event id descriptions.
    https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc727168(v=ws.10)
    """
    ID100 = "Task Scheduler started the instance of the task."
    ID101 = "Task Scheduler failed to start the task."
    ID102 = "Task Scheduler successfully finished the instance of the task."
    ID103 = "Task Scheduler failed to start the instance of the task."
    ID104 = "Task Scheduler failed to log on. Ensure the credentials for the task are \
        correctly specified."
    ID105 = "Task Scheduler failed to impersonate instance of the task."
    ID106 = "The task was registered by user."
    ID107 = "Task Scheduler launched the instance of the task due to a time trigger."
    ID108 = " Task Scehduler launched the instance of the task. The task was \
        triggered by an event trigger."
    ID109 = "Task Scheduler launched the instance of the task due to a registration trigger."
    ID110 = "Task Scheduler launched the instance of the task."
    ID111 = "Task Scheduler terminated the instance of the task due to exceeding the time \
        allocated for execution, as configured in the task definition. Increase the configured \
        task timr out or investigate exteranl reasons for the delay."
    ID112 = "Task Scheduler could not start the task because the network was unavailable. \
        Ensure the computer is connected to the required network as specified in the task. \
        If the task does not require network presence, remove the network condition from the \
        task registration."
    ID113 = "The Task Scheduler registered the task, but not all the specified triggers will \
        start the task. Ensure all the task triggers are valid."
    ID114 = "Task Scheduler could not launch task as scheduled. The instance is started \
        now as required by the configuration option to start the task when available, \
        if the scheduled time is missed."
    ID115 = "The Scheduler failed to roll back a transaction when updating or deleting a task."
    ID116 = "Task Scheduler saved the configuration for the task, but the credentials used to run \
        the task could not be stored. Ensure the credentials are valid and re-register the task."
    ID117 = "Task Scheduler launched the instance of the task due to an idle condition,"
    ID118 = "Task Scheduler launched the instance of the task due to system startup."
    ID119 = "Task Scheduler launched the instance of the task due to user logon."
    ID120 = "Task Scheduler launched the instance of the task due to user \
        connecting to the console."
    ID121 = "Task Scheduler launched the instance of the task due to user \
        disconnecting from the console."
    ID122 = "Task Scheduler launched the instance of the task due to the user \
        remotely connecting."
    ID123 = "Task Scheduler launched the instance of the task due to the user \
        remotely disconnecting."
    ID124 = "Task Scheduler launched the instance of the task due to the user \
        locking the computer."
    ID125 = "Task Scheduler launched the instance of the task due to the user \
        unlocking the computer."
    ID126 = "Task Scheduler failed to execute the task. Task Scheduler is \
        attempting to restart the task."
    ID127 = "Task Scheduler failed to execute the task due to a shutdown race condition. \
        Task scheduler is attempting to restart the task."
    ID128 = "Task Scheduler did not launch the task because the current time exceeds the \
        configured task end time. Extend the end time boundary for the task if required."
    ID129 = "Task Scheduler launched the instance of the task with process ID."
    ID130 = "Task Scheduler service failed to start the task due to the service being busy."
    ID140 = "The task was updated by the user."
    ID141 = "The task was deleted by the user."
    ID142 = "User disabled task."
    ID145 = "Task Scheduler woke up the computer to run a task."
    ID200 = "Task Scehduler launched the action of the task."
    ID201 = "Task Scheduler successfully completed the task, instance and action."
    ID202 = "Task Scheduler failed to complete the instance of the task with action."
    ID203 = "Task Scheduler failed to launch action in the instance of the task."
    ID204 = "Task Scehduler failed to retrieve the event triggering values for the task. \
        The event will be ignored."
    ID205 = "Task Scheduler failed to match the pattern of events for the task. \
        The event will be ignored."
    ID305 = "Task Scheduler did not send the task to task engine."
    ID322 = "Task Scheduler did not launch the task because of the instance of the same task \
        is already running."
    ID323 = "Task Scheduler stopped the instance of the task in order to launch a new instance."
    ID324 = "Task Scheduler queued the instance of the task and will launch as soon as the other \
        instance is complete."
    ID326 = "Task Scheduler did not launch the task because the computer is running on batteries. \
        If launching the task on batteries is required, change the respective flag in the task \
        configuration."
    ID327 = "Task SCheduler stopped the instance of the task because the computer is \
        switching to battery power."
    ID328 = "Task Scheduler stopped the instance of the task because the computer \
        is no longer idle."
    ID329 = "Task Scheduler stopped the instance of the task because the task timed out."
    ID330 = "Task Scheduler stopped the instance of the task as request by user."
    ID331 = "Task Scheduler will continue to execute the instance of the task even after the \
        designated timeout, due to a failure to create the timeout mechanism."
    ID332 = "Task Scheduler did not launch the task because user was not logged on when \
        the launching conditions were met. Ensure the user is logged on or change the task \
        definition to allow the task to launch when the user is logged off."
    ID400 = "The Task Scheduler service has started."
    ID401 = "The Task Scheduler service failed to start due to an error in the instance."
    ID402 = "The Task Scheduler service is shutting down."
    ID403 = "The Task Scheduler service has encountered an error."
    ID404 = "The Task Scheduler service has encountered an RPC initialization error."
    ID405 = "The Task Scheduler service has failed to initialize COM."
    ID406 = "The Task Scheduler service failed to initialize the credentials store."
    ID409 = "The Task Scheduler service failed to initialize a time change notification. \
        System time updates may not be picked by the service and \
        task schedules may not be updated."
    ID411 = "Task Scheduler service received a time system change notification."
    ID412 = "Task Scheduler service failed to launch tasks triggered by computer startup."

    DESCRIPTIONS = {
        100:ID100,
        101:ID101,
        102:ID102,
        103:ID103,
        104:ID104,
        105:ID105,
        106:ID106,
        107:ID107,
        108:ID108,
        109:ID109,
        110:ID110,
        111:ID111,
        112:ID112,
        113:ID113,
        114:ID114,
        115:ID115,
        116:ID116,
        117:ID117,
        118:ID118,
        119:ID119,
        120:ID120,
        121:ID121,
        122:ID122,
        123:ID123,
        124:ID124,
        125:ID125,
        126:ID126,
        127:ID127,
        128:ID128,
        129:ID129,
        130:ID120,
        140:ID140,
        141:ID141,
        142:ID142,
        145:ID145,
        200:ID200,
        201:ID201,
        202:ID202,
        203:ID203,
        204:ID204,
        205:ID205,
        305:ID305,
        322:ID322,
        323:ID323,
        324:ID324,
        326:ID326,
        327:ID327,
        328:ID328,
        329:ID329,
        330:ID330,
        331:ID331,
        332:ID332,
        400:ID400,
        401:ID401,
        402:ID402,
        403:ID403,
        404:ID404,
        405:ID405,
        406:ID406,
        409:ID409,
        411:ID411,
        412:ID412
    }
