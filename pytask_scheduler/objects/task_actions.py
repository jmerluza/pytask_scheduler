"""This module covers topics from the Action scripting object.
https://learn.microsoft.com/en-us/windows/win32/taskschd/action
"""
from pytask_scheduler import TaskActionTypes

class TaskAction:
    def __init__(self, taskdef_obj):
        self.action = taskdef_obj.Actions

    def __set_action_type(self, action_type: int):
        self.action.Create(action_type)

    def create_execution_action(
        self,
        argument: str,
        filepath: str|None="",
        working_dir: str|None=""
    ):
        """Creates an action that executes a command-line operation. For example, \
            can execute a batch file script.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/execaction

        Parameters:
            argument (`str`): Sets the arguments associated with the command-line operation.
            filepath (`str`): Sets the path to an executable file.
            working_dir (`str`): Sets the directory that contains either the executable file \
            or the files that are used by the executable file.
        """
        self.__set_action_type(TaskActionTypes.TASK_ACTION_EXEC)
        self.action.Path = filepath
        self.action.Arguments = argument
        self.action.WorkingDirectory = working_dir

    def create_com_handler_action(self):
        """Creates an action that fires a handler.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/comhandleraction
        """
        raise NotImplementedError("Create com handle action has not been implemented")

    def create_send_email_action(self):
        """Creates an action that send an email message.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/emailaction
        """
        raise NotImplementedError("Create com handle action has not been implemented")

    def create_show_message_action(self):
        """Creates an action that shows a message box when a task is activated.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/showmessageaction
        """
        raise NotImplementedError("Create com handle action has not been implemented")
