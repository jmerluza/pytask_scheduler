from dataclasses import dataclass

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