from dataclasses import dataclass

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