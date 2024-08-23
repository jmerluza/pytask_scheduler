from dataclasses import dataclass

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
