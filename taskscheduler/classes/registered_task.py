"""This module covers some of the api from the RegisteredTask scripting object.
https://learn.microsoft.com/en-us/windows/win32/taskschd/registeredtask
"""

class RegisteredTask:
    def __init__(self, rtask_obj):
        self.rtask = rtask_obj
        self.taskdef = self.rtask.Definition
        self.reg_info = self.taskdef.RegistrationInfo

    def info(self) -> dict:
        """Information on registered task."""
        return {
            "name":self.rtask.Name,
            "enabled":self.rtask.Enabled,
            "task_state":self.rtask.State,
            "next_run_time":self.rtask.NextRunTime,
            "last_run_time":self.rtask.LastRunTime,
            "last_task_result":self.rtask.LastTaskResult,
            "number_of_missed_runs":self.rtask.NumberOfMissedRuns,
            "task_path":self.rtask.Path,
            "author":self.reg_info.Author,
            "registration_date":self.reg_info.Date,
            "task_description":self.reg_info.Description,
            "task_source":self.reg_info.Source
        }

    def update_registration_info(self, task_description: str):
        """Updates the registration info for a task.

        Parameter:
            task_description (`str`): Description of a task.
        
        Support:
            Only supports updating the task description.

        Returns:
            TaskDefinition object.
        """
        self.reg_info.Description = task_description
        return self.taskdef
